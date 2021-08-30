import subprocess
import time
from pathlib import Path

import pyautogui

from lib.logger import get_logger


class Timeline:
    def __init__(self, timeline_manager, name, program_path: Path = None, program_name=None, logger=None):
        self.manager = timeline_manager
        self.name = name
        self.resource_pool: Path = self.manager.resource_pool.joinpath(self.name + "/")
        self.resource_pool.mkdir(parents=True, exist_ok=True)
        self.program = program_path
        self.process = None
        if not program_name:
            self.program_name = program_path.stem if program_path else "Desktop"
        self.steps = []
        self.requirements = None
        self.data = {}
        self.selected_index = 0

        self.logger = logger if logger else get_logger(self.name)

    def register_resource(self, key, resource):
        self.data[key] = resource

    def run_timeline(self, delay=0.1):
        """Open source program as child process and execute steps in timeline.

        :param delay: Additional sleep between steps
        """
        if self.program:
            self.logger.info(f"Timeline {self.name} is running program {self.program_name}")
            self.process = self.run_source()
            self.make_window_active()
        else:
            self.logger.warning("No program designated, running without sanity check")

        for step in self.steps:
            # Check if process is still running
            if self.process:
                self.process.poll()

                if self.process.returncode:
                    self.logger.info("Program is not running, timeline exiting..")
                    return
            try:
                step.execute()
            except Exception as e:
                self.logger.error(f"{step.name} Failed: {e}")

            time.sleep(delay)

    def run_source(self, startup: float = 1) -> subprocess.Popen:
        """Run the source program as a subprocess and attempt to make the window active

        Args:
            startup: About how long startup takes for the intended application

        Returns:
            Popen object, source program as a child process
        """
        process = subprocess.Popen(self.program.as_posix())
        time.sleep(startup)
        return process

    def make_window_active(self, tries: int = 3, interval: float = 0.5):
        """Check current open windows and grab matching window

        Args:
            tries: how many times to attempt window grab
            interval: time between tries
        """
        source_window = pyautogui.getWindowsWithTitle(self.program_name)[0]
        self.logger.debug(f"found window {source_window}")
        source_window.activate()
        while tries >= 0 and pyautogui.getActiveWindow() != source_window:
            self.logger.debug("source window not active, trying to reset")
            time.sleep(interval)
            source_window.activate()
            tries -= 1
        if pyautogui.getActiveWindow() != source_window:
            self.logger.debug(f"Could not make source window active. Abort to avoid mistakes!")
            raise ChildProcessError

    def add_step(self, new_step):

        self.logger.debug(f"Adding {new_step.name}")
        self.steps.append(new_step)

    def remove_step(self):
        self.steps.pop(self.selected_index)
        self.selected_index -= 1

        for i, step in enumerate(self.steps):
            step.index = i

    # TODO: Leave this on roadmap
    def add_condition(self, condition, success, failure):
        if condition:
            success()
        else:
            failure()

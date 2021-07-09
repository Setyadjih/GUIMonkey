import subprocess
import time
from pathlib import Path

import pyautogui


class Timeline:
    def __init__(self, guimonkey, name=None, program_path: Path = None):
        self.gm = guimonkey
        self.name = name
        self.resource_pool: Path = self.gm.resource_pool.joinpath(self.name + "/")
        self.resource_pool.mkdir(parents=True, exist_ok=True)
        self.program = program_path
        # TODO: Allow custom setting of program name
        self.program_name = program_path.stem
        self.steps = []
        self.requirements = None
        self.data = {}
        self.selected_index = 0

    def register_resource(self, key, resource):
        self.data[key] = resource

    def run_timeline(self):
        if self.program:
            print("Running program")
            process = self.run_source()
            self.make_window_active()
        else:
            print("No program designated, running without sanity check")

        for step in self.steps:
            # Check if process is still running
            if self.program:
                poll = process.poll()
            else:
                poll = None

            # poll returns None if all is good
            if poll is None:
                try:
                    step.execute()
                except Exception as e:
                    print(f"{step.name} Failed: {e}")
            else:
                print("Program is not running, timeline exiting..")
                return

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
        print(f"found window {source_window}")
        source_window.activate()
        while tries >= 0 and pyautogui.getActiveWindow() != source_window:
            print("source window not active, trying to reset")
            time.sleep(interval)
            source_window.activate()
            tries -= 1
        if pyautogui.getActiveWindow() != source_window:
            print(f"Could not make source window active. Abort to avoid mistakes!")
            raise ChildProcessError

    def add_step(self, step_class, *args, **kwargs):
        new_step = step_class(self, *args, **kwargs)
        new_step.index = len(self.steps)
        while new_step.name in self.steps:
            new_step.name += str(new_step.index)

        print(f"Adding {new_step.name}")
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

import subprocess

import pyautogui
pyautogui.useImageNotFoundException()


class GUIMonkey:
    def __init__(self):
        self.resources = None
        self.timelines = dict()

    def new_timeline(self, name, source):
        if name in self.timelines.keys():
            print("Timeline already exists, please choose a different name")
            return None

        new_timeline = Timeline(name, source)
        self.timelines[name] = new_timeline
        return self.timelines[name]

    def set_resource_pool(self, path):
        self.resources = path
        self.check_resources()

    def add_resource(self):
        pass

    def create_timeline(self):
        pass


class Timeline:
    def __init__(self, name=None, program_path=None):
        self.name = name
        self.program = program_path
        self.steps = None
        self.requirements = None
        self.data = {}

    def run_timeline(self):
        print("Running program")
        try:
            subprocess.Popen(self.program)
        except Exception:
            print("Failed to launch program! Aborting...")

        for step in self.steps:

            # TODO: this might be smoother with functools.partial
            if step.flags["require"]:
                require_data = step.flags["require_data"]
                data_key, pass_data = step.execute(require_data)
            else:
                data_key, pass_data = step.execute()

            if step.flags['passthrough']:
                self.data[data_key] = pass_data

    def add_step(self):
        pass

    def add_delay(self):
        pass

    # TODO: Leave this on roadmap
    def add_condition(self, condition, success, failure):
        if condition:
            success()
        else:
            failure()



import subprocess
from pathlib import Path

class Timeline:
    def __init__(self, guimonkey, name=None, program_path=None):
        self.gm = guimonkey
        self.name = name
        self.resource_pool: Path = self.gm.resource_pool.joinpath(self.name+"/")
        self.resource_pool.mkdir(parents=True, exist_ok=True)
        self.program = program_path
        self.steps = []
        self.requirements = None
        self.data = {}

    def register_resource(self, key, resource):
        self.data[key] = resource

    def run_timeline(self):
        if self.program:
            print("Running program")
            process = subprocess.Popen(self.program)
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
                    print(f"{step.type} Failed: {e}")
            else:
                print("Program is not running, timeline exiting..")
                return

    def add_step(self, step_class):
        self.steps.append(step_class(self))

    def remove_step(self, index):
        self.steps.pop(index+1)

    # TODO: Leave this on roadmap
    def add_condition(self, condition, success, failure):
        if condition:
            success()
        else:
            failure()


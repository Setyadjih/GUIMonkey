from pathlib import Path
import shutil

from Timelines import Timeline


class GUIMonkeyCore:
    """Core Engine to manage Timelines and resource pool directory"""
    def __init__(self):
        self.resource_pool = Path("./resources")
        self.timelines = {}

    def create_timeline(self, name, source=None):
        if name in self.timelines.keys():
            print("Timeline already exists, please choose a different name")
            return None

        new_timeline = Timeline(name, source)
        self.timelines[name] = new_timeline

    def delete_timeline(self, name):
        del self.timelines[name]

    # Resource pool updating might be done during loop. That might be better
    # than trying to manage items from the central GUI

    def set_resource_pool(self, path):
        self.resource_pool = path
        # self.check_resource_pool()

    def check_resource_pool(self):
        for file in self.resource_pool.rglob("*.*"):
            # TODO: Generate UI thumbnails and tags
            self.register_resource(file)

    def add_resource(self, source, dest):
        # Copy file or folder from original location to resource pool
        shutil.copy2(source, dest)
        self.register_resource(dest)

    def register_resource(self, resource):
        # TODO: Generate UI thumbnail and tags
        pass
from pathlib import Path
import shutil

from lib.logger import get_logger
from GUIMonkey.Timelines import Timeline


class TimelineManager:
    """Core Engine to manage Timelines and resource pool directory"""

    def __init__(self):
        self.resource_pool = Path("../resources")
        self.timelines = {}
        self.logger = get_logger()

    def create_timeline(self, name, source: Path = None) -> Timeline:
        self.logger.info(f"Creating Timeline {name}, with source: {source}")

        if name in self.timelines.keys():
            self.logger.warning("Timeline already exists, please choose a different name")
            raise FileExistsError

        new_timeline = Timeline(self, name, source)
        self.timelines[name] = new_timeline

        return self.timelines[name]

    def delete_timeline(self, name):
        self.logger.debug(f"Deleting Timeline: {name}")
        del self.timelines[name]

    # Resource pool updating might be done during loop. That might be better
    # than trying to manage items from the central GUI

    def set_resource_pool(self, path):
        self.resource_pool = path
        self.check_resource_pool()

    def check_resource_pool(self):
        for file in self.resource_pool.rglob("*.*"):
            self.register_resource(file)

    def add_resource(self, source, dest):
        # Copy file or folder from original location to resource pool
        shutil.copy2(source, dest)
        self.register_resource(dest)

    def register_resource(self, resource):
        # TODO: Generate UI thumbnail and tags
        pass


if __name__ == "__main__":
    gm = TimelineManager()

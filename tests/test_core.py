from rich import print
from rich.progress import track

from GUIMonkey.GUIMonkeyCore import TimelineManager


def test_core_init():
    """Test initialization"""
    test_timeline_name = "Test Timeline"

    tm = TimelineManager()
    timeline = tm.create_timeline(test_timeline_name)

    assert timeline.name == test_timeline_name





from rich import print
from rich.progress import track

from GUIMonkey.GUIMonkeyCore import TimelineManager
from GUIMonkey import Steps

def test_core_init():
    """Test initialization"""
    name = "Test Timeline"

    tm = TimelineManager()
    timeline = tm.create_timeline(name)

    assert timeline.name == name


def test_step_add():
    """Test adding steps to a timeline"""
    name = "Test Steps"

    manager = TimelineManager()
    timeline = manager.create_timeline(name)

    steps = [Steps.Delay(), Steps.KeyPress("win"), Steps.Write("Test")]

    for step in track(steps, description="Adding steps..."):
        timeline.add_step(step)

    assert len(timeline.steps) == len(steps)

    timeline.run_timeline()


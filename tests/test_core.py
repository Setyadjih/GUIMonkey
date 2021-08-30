from pathlib import Path
import os
import time

from rich import print
from rich.progress import track

from GUIMonkey.GUIMonkeyCore import TimelineManager
from GUIMonkey import Steps, Timelines

from lib.logger import get_logger

LOGGER = get_logger()


def test_core_init():
    """Test initialization"""
    LOGGER.info("Running core Init test...")
    name = "Test Timeline"

    tm = TimelineManager()
    timeline = tm.create_timeline(name)

    assert timeline.name == name


def test_step_add():
    """Test adding steps to a timeline"""
    LOGGER.info("Running step add test...")
    name = "Test Steps"

    manager = TimelineManager()
    timeline = manager.create_timeline(name)

    steps = [Steps.Delay(), Steps.KeyPress("win"), Steps.Write("Test")]

    for step in track(steps, description="Adding steps..."):
        timeline.add_step(step)

    assert len(timeline.steps) == len(steps)

    timeline.run_timeline()


def test_notepad_typing():
    LOGGER.info("Running Notepad typing test...")
    text = "notepad typing succeeeded?"

    test_file_out = Path(r"D:\OneDriveLF\PycharmProjects\GUIMonkey\tests\test_dir\typing_text_temp.txt")

    def notepad_type_text():
        tm = TimelineManager()
        timeline: Timelines.Timeline = tm.create_timeline("Typing test", source=Path(r"C:\WINDOWS\system32\notepad.exe"))

        timeline.add_step(Steps.Write(text, step_name="Write Text"))
        timeline.add_step(Steps.KeyPress("s", "ctrl", step_name="Save"))
        timeline.add_step(Steps.Delay(1))
        timeline.add_step(Steps.Write(test_file_out.stem, step_name="Write filename"))

        test_dir = test_file_out.parent.absolute().as_posix()
        timeline.add_step(Steps.KeyPress("l", "ctrl", step_name="Go to address"))
        timeline.add_step(Steps.Write(test_dir, step_name="Write Dir"))
        timeline.add_step(Steps.KeyPress("enter"))
        timeline.add_step(Steps.KeyPress("s", "alt"))

        timeline.run_timeline()

    notepad_type_text()

    LOGGER.debug(f"Checking if file is saved to {test_file_out.absolute()}")
    time.sleep(2)
    assert test_file_out.exists()

    LOGGER.debug(f"Checking file contents are correct")
    if test_file_out.exists():
        with open(test_file_out) as notepad_out:
            line = notepad_out.readline()
            assert line == text

        os.remove(test_file_out)

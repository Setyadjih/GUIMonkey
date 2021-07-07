from pathlib import Path
import os

# TODO: this architecture doesn't seem right. Let's see if there's a better way to organize the application files
from GUIMonkey.GUIMonkeyCore import TimelineManager
from GUIMonkey.Timelines import Timeline
from GUIMonkey.Steps import Write, KeyPress, Delay


def notepad_type_text(text: str, test_dir_path: Path):
    tm = TimelineManager()
    timeline: Timeline = tm.create_timeline("Typing test", source=Path(r"C:\WINDOWS\system32\notepad.exe"))

    timeline.add_step(Write, text, step_name="Write Text")
    timeline.add_step(KeyPress, "s", "ctrl", step_name="Save")
    timeline.add_step(Delay, 1)
    timeline.add_step(Write, test_dir_path.stem, step_name="Write filename")

    test_dir = test_dir_path.parent.absolute().as_posix()
    timeline.add_step(KeyPress, "l", "ctrl", step_name="Go to address")
    timeline.add_step(Write, test_dir, step_name="Write Dir")
    timeline.add_step(KeyPress, "enter")
    timeline.add_step(KeyPress, "s", "alt")

    timeline.run_timeline()


def test_notepad_typing():
    text = "notepad typing succeeeded?"

    test_file_out = Path(r"D:\OneDriveLF\PycharmProjects\GUIMonkey\tests\test_dir\typing_text_temp.txt")

    notepad_type_text(text, test_file_out)

    print(f"Checking if file is saved to {test_file_out.absolute()}")
    assert test_file_out.exists()

    if test_file_out.exists():
        with open(test_file_out) as notepad_out:
            line = notepad_out.readline()
            assert line == text

        os.remove(test_file_out)




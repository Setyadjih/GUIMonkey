from GUIMonkey import GUIMonkeyCore
from GUIMonkey.Timelines import Timeline
from GUIMonkey.Steps import WaitForImage, ClickOnButton, KeyPress, Delay, Write, \
    WaitForLoading, MoveToButton

CLO_PATH = r"D:\Program Files\CLO Network OnlineAuth 6.0.594\CLO_Network_OnlineAuth_x64.exe"
TEST_FOLDER = r"D:\OneDriveLF\test_files\clo_test"
TEST_FILE = r"women_10_sweater.Zprj"


def clo_usage():
    gm = GUIMonkeyCore.TimelineManager()
    gm.set_resource_pool(path="./resources")

    clo_test: Timeline = gm.create_timeline("CLO Test", source=CLO_PATH)

    # TODO: Should ideally be registering from GUIMonkey
    clo_test.register_resource("Welcome", "./resources/CLO_welcome.png")
    clo_test.register_resource("File", "resources/buttons/CLO_file.png")

    clo_test.add_step(WaitForImage("./resources/CLO_welcome.png", 60))
    clo_test.add_step(ClickOnButton("resources/buttons/CLO_file.png", 2))

    clo_test.add_step(KeyPress('o', 'ctrl'))
    clo_test.add_step(Delay(1))

    clo_test.add_step(KeyPress("l", 'ctrl'))
    clo_test.add_step(Write(TEST_FOLDER, enter=True))

    clo_test.add_step(KeyPress('n', 'alt'))
    clo_test.add_step(Write(TEST_FILE))
    clo_test.add_step(KeyPress('o', 'alt'))

    clo_test.add_step(WaitForLoading("resources/CLO_loading.png"))
    clo_test.add_step(ClickOnButton("resources/buttons/CLO_render.png"))
    clo_test.add_step(MoveToButton("resources/buttons/CLO_current_colorway_fnx.png"))

    clo_test.run_timeline()


if __name__ == "__main__":
    clo_usage()
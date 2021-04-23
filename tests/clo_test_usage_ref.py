import subprocess
import time

import pyautogui
pyautogui.useImageNotFoundException()

# TODO: split off into seperate tests for fnx and gltf files
# TODO: Add support for sequential file tests
# TODO: Check if software is already open


def press_with_mod(mod, key):
    pyautogui.keyDown(mod)
    pyautogui.press(key)
    pyautogui.keyUp(mod)


def wait_till_found(image, timeout=30):
    """Wait 5 seconds and then check for image on screen until timeout.
    Returns image center if found, None if timed out"""
    start = time.time()
    current = time.time()

    while current - start < timeout:
        time.sleep(5)
        try:
            image_loc = pyautogui.locateCenterOnScreen(
                image,
                confidence=0.9
            )
            print("Found!")
            return image_loc
        except pyautogui.ImageNotFoundException:
            print("Did not find image...")
            current = time.time()

    print("Search timed out, returning...")
    return None


def clo_test(clo_exec, test_folder, test_file):
    print("Running program")
    try:
        subprocess.Popen(clo_exec)
    except Exception:
        print("Failed to launch program! Aborting...")

    launched = wait_till_found("resources/CLO_welcome.png", timeout=60)
    if not launched:
        print("failed to launch before timeout")
        return

    file_button = pyautogui.locateCenterOnScreen(
        "resources/buttons/CLO_file.png", confidence=0.9
    )
    pyautogui.click(file_button[0], file_button[1])
    pyautogui.click(file_button[0], file_button[1])

    # Trigger hotkey for project open dialog
    press_with_mod('ctrl', 'o')
    time.sleep(1)

    # Go into addressbar and input CLO test folder
    press_with_mod('ctrl', 'l')
    pyautogui.write(test_folder)
    pyautogui.press('enter')

    # input Designated test file
    press_with_mod('alt', 'n')
    pyautogui.write(test_file)
    press_with_mod('alt', 'o')
    time.sleep(3)

    pyautogui.useImageNotFoundException(False)

    extra_dialogue = pyautogui.locateCenterOnScreen(
        "resources/ClO_open_project_dialogue.png",
        confidence=0.9
    )
    if extra_dialogue:
        ok_button = pyautogui.locateCenterOnScreen(
            "resources/buttons/CLO_ok.png",
            confidence=0.9
        )
        pyautogui.click(ok_button)

    trigger = 0
    while trigger < 3:
        load1 = pyautogui.locateCenterOnScreen(
            "resources/CLO_loading.png",
            confidence=0.9
        )
        if load1:
            print("found loading, waiting...")
            trigger = 0
            pyautogui.moveTo(load1)
            time.sleep(3)
        else:
            print("Did not find loading, triggering")
            trigger += 1
            time.sleep(1)

    print("detected end of loading, continuing")

    pyautogui.useImageNotFoundException()

    render = pyautogui.locateCenterOnScreen(
        "resources/buttons/CLO_render.png",
        confidence=0.9
    )
    pyautogui.click(render)
    fnx = pyautogui.locateCenterOnScreen(
        "resources/buttons/CLO_current_colorway_fnx.png",
        confidence=0.9
    )
    pyautogui.click(fnx)


if __name__ == "__main__":
    # DEBUG PARAMS -----
    clo_test(
    r"D:\Program Files\CLO Network OnlineAuth 6.0.594\CLO_Network_OnlineAuth_x64.exe"
    r"C:\Users\hugosetyadji\OneDrive - Li & Fung\test_files\clo_test",
    r"women_10_sweater.Zprj"
    )

    clo_test(
        r"C:\Program Files\CLO Network OnlineAuth 5.60\CLO_Network_OnlineAuth_x64.exe",
        r"C:\Users\hugosetyadji\OneDrive - Li & Fung\test_files\clo_test",
        r"women_10_sweater.Zprj"
    )
    # DEBUG PARAMS -----
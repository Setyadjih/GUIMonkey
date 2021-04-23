import time

import pyautogui


class StepBase:
    """Base class for steps. We mainly want the execute interface"""
    def __init__(self, type=None, resource=None):
        if not type:
            type = self.__class__
        self.type = type
        self.resource = resource
        self.flags = {'passthrough': False}

    def execute(self):
        pass


class KeyPress(StepBase):
    def __init__(self, key, mod=None):
        super(KeyPress, self).__init__()
        self.key = key
        self.mod = mod

    def execute(self):
        if self.mod:
            pyautogui.keyDown(self.mod)
            pyautogui.press(self.key)
            pyautogui.keyUp(self.mod)
        else:
            pyautogui.press(self.key)


class WaitForImage(StepBase):
    def __init__(self, image, next_step, timeout=30):
        super(WaitForImage, self).__init__()
        self.image = image
        self.timeout = timeout
        self.flags['passthrough'] = True

        # TODO: figure out system for data passthrough
        self.next = next_step

    def execute(self):
        start = time.time()
        current = time.time()
        image_loc = None

        while current - start < self.timeout:
            time.sleep(5)
            image_loc = pyautogui.locateCenterOnScreen(
                self.image,
                confidence=0.9
            )
            if image_loc:
                print("Found!")
                return "image_loc", image_loc
            else:
                current = time.time()
                print(f"Did not find image...{current}/{self.timeout}")

        print("Search timed out, returning...")
        return "image_loc", image_loc


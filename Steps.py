import time

import pyautogui


class StepBase:
    """Base class for steps. We mainly want the execute interface"""
    def __init__(self, step_name=None, resource=None):
        if not step_name:
            step_name = self.__class__.__name__
        self.name = step_name
        self.resource = resource
        self.flags = {
            # Require Flags
            'require': False,
            'require_key': None,
            
            # output Flags
            'output': False,
            'output_key': None,
        }

    def execute(self):
        print(f"Executing {self.type}...")

    def require_data(self, require_bool=False, require_key=None):
        self.flags['require'] = require_bool
        self.flags['require_key'] = require_key

    def output_data(self, pass_bool=False, output_key=None):
        self.flags['output'] = pass_bool
        self.flags['output_key'] = output_key


class KeyPress(StepBase):
    def __init__(self, key="a", mod=None):
        super(KeyPress, self).__init__()
        self.key = key
        self.mod = mod

    def execute(self):
        super(KeyPress, self).execute()
        if self.mod:
            pyautogui.keyDown(self.mod)
            pyautogui.press(self.key)
            pyautogui.keyUp(self.mod)
        else:
            pyautogui.press(self.key)


class WaitForImage(StepBase):
    def __init__(self, image_key, timeout=30):
        super(WaitForImage, self).__init__()
        self.require_data(True, image_key)
        self.timeout = timeout
        self.image = image_key
        self.output_data(True, "image_loc")

        # TODO: figure out system for data output

    def execute(self):
        super(WaitForImage, self).execute()
        start = time.time()
        current = time.time()
        image_loc = None

        while current - start < self.timeout:
            time.sleep(3)
            image_loc = pyautogui.locateCenterOnScreen(
                self.image,
                confidence=0.9
            )
            if image_loc:
                print("Found!")
                return image_loc
            else:
                current = time.time()
                print(f"Did not find image...{int(current - start)}/{self.timeout}")

        print("Search timed out, returning...")
        return image_loc


class Delay(StepBase):
    def __init__(self, delay):
        super(Delay, self).__init__()
        self.delay = delay

    def execute(self):
        super(Delay, self).execute()
        time.sleep(self.delay)


class MoveToButton(StepBase):
    def __init__(self, button):
        super(MoveToButton, self).__init__()
        self.button = button

    def execute(self):
        super(MoveToButton, self).execute()
        button_loc = pyautogui.locateCenterOnScreen(
            self.button, confidence=0.9
        )
        pyautogui.moveTo(button_loc[0], button_loc[1])


class ClickOnButton(StepBase):
    def __init__(self, button, click_num=1):
        super(ClickOnButton, self).__init__()
        self.require_data(True, "image_loc")
        self.button = button
        self.click_num = click_num

    def execute(self):
        super(ClickOnButton, self).execute()
        button = pyautogui.locateCenterOnScreen(self.button, confidence=0.9)
        for i in range(self.click_num):
            pyautogui.click(button[0], button[1])


class Write(StepBase):
    def __init__(self, text, enter=False):
        super(Write, self).__init__()
        self.text = text
        self.enter = enter

    def execute(self):
        super(Write, self).execute()
        pyautogui.write(self.text)
        if self.enter:
            pyautogui.press('enter')


class WaitForLoading(StepBase):
    def __init__(self, loading_image, trigger_max=3):
        super(WaitForLoading, self).__init__()
        self.loading_image = loading_image
        self.trigger_max = trigger_max

    def execute(self):
        super(WaitForLoading, self).execute()
        trigger = 0
        while trigger < self.trigger_max:
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
                trigger += 1
                time.sleep(1)
                print(f"Did not find loading, triggering ({trigger} / "
                      f"{self.trigger_max})")

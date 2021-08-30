import time
from abc import ABC, abstractmethod

import pyautogui

from lib.logger import get_logger


class StepBase(ABC):
    """Base class for steps. We mainly want the execute interface"""

    @abstractmethod
    def __init__(self, step_name: str = None, logger=None):
        self.name = step_name if step_name else self.__class__.__name__

        self.data = None
        self.flags = {
            # Require Flags
            "require": False,
            "require_key": None,
            # output Flags
            "output": False,
            "output_key": None,
        }
        self.logger = logger if logger else get_logger(self.name)

    @abstractmethod
    def execute(self):
        self.logger.debug(f"Executing {self.name}...")


# TODO: This system seems fragile. How should in and out data be handled?
    def require_data(self, require_bool=False, require_key=None):
        self.flags["require"] = require_bool
        self.flags["require_key"] = require_key

    def output_data(self, pass_bool=False, output_key=None):
        self.flags["output"] = pass_bool
        self.flags["output_key"] = output_key


class KeyPress(StepBase):
    def __init__(self,  key="a", mod=None, step_name=None, logger=None):
        super(KeyPress, self).__init__(step_name, logger)
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
    def __init__(self,  image=None, timeout=30, step_name=None, logger=None):
        super(WaitForImage, self).__init__(step_name, logger)
        self.timeout = timeout
        self.image = image
        self.require_data(True, "image")
        self.output_data(True, "image_loc")

        # TODO: figure out system for data output

    def execute(self):
        super(WaitForImage, self).execute()

        start = time.time()
        current = time.time()
        image_loc = None

        while current - start < self.timeout:
            time.sleep(3)
            image_loc = pyautogui.locateCenterOnScreen(self.image, confidence=0.9)
            if image_loc:
                self.logger.debug("Found!")

                return image_loc
            else:
                current = time.time()
                self.logger.debug(f"Did not find image...{int(current - start)}/{self.timeout}")

        self.logger.warning("Search timed out, returning...")
        return image_loc


class Delay(StepBase):
    def __init__(self,  delay=0.5, step_name=None, logger=None):
        super(Delay, self).__init__(step_name, logger)
        self.delay = delay

    def execute(self):
        super(Delay, self).execute()
        time.sleep(self.delay)


class MoveToButton(StepBase):
    def __init__(self,  button, step_name=None, logger=None):
        super(MoveToButton, self).__init__(step_name, logger)
        self.button = button

    def execute(self):
        super(MoveToButton, self).execute()
        button_loc = pyautogui.locateCenterOnScreen(self.button, confidence=0.9)
        pyautogui.moveTo(button_loc[0], button_loc[1])


class ClickOnButton(StepBase):
    def __init__(self,  button, click_num=1, step_name=None, logger=None):
        super(ClickOnButton, self).__init__(step_name, logger)
        self.require_data(True, "image_loc")
        self.button = button
        self.click_num = click_num

    def execute(self):
        super(ClickOnButton, self).execute()
        button = pyautogui.locateCenterOnScreen(self.button, confidence=0.9)
        for i in range(self.click_num):
            pyautogui.click(button[0], button[1])


class Write(StepBase):
    def __init__(self,  text, enter=False, step_name=None, logger=None):
        super(Write, self).__init__(step_name, logger)
        self.text = text
        self.enter = enter

    def execute(self):
        super(Write, self).execute()
        pyautogui.write(self.text)
        if self.enter:
            pyautogui.press("enter")


class WaitForLoading(StepBase):
    def __init__(self,  loading_image, trigger_max=3, step_name=None, logger=None):
        super(WaitForLoading, self).__init__(step_name, logger)
        self.loading_image = loading_image
        self.trigger_max = trigger_max

    def execute(self):
        super(WaitForLoading, self).execute()
        trigger = 0
        while trigger < self.trigger_max:
            load1 = pyautogui.locateCenterOnScreen("resources/CLO_loading.png", confidence=0.9)
            if load1:
                self.logger.debug("found loading, waiting...")
                trigger = 0
                pyautogui.moveTo(load1)
                time.sleep(3)
            else:
                trigger += 1
                time.sleep(1)
                self.logger.debug(f"Did not find loading, triggering ({trigger} / " f"{self.trigger_max})")

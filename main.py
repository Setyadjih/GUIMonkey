import subprocess
import time

import pyautogui
pyautogui.useImageNotFoundException()


class Timeline:
    def __init__(self):
        self.program = None
        self.steps = None
        self.requirements = None

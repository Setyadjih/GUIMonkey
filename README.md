# GUIMonkey
GUI Automation and testing toolkit based on pyautogui and PySide6.

The main application creates and manages Timelines, separate units of each 
desired test or automation

Timelines are made of Steps, which are executed in sequential order. The 
steps are a wrapper for PyAutoGui commands, bundling common instructions 
together into a block.

# Roadmap
* More Steps for functionality and flexibility
* PySide6 UI to manage and create different Timelines
  * Drag and Drop steps to add and rearrange
  * Create step presets for future reuse
* Command-line tool for remote execution of Timelines
  * Screenshot to log failures and results

# Notable Dependencies
Python==3.9\
PySide6==6.0.3\
PyAutoGui==0.9.52\
opencv-python==4.5.1.48\
Pillow==8.2.0

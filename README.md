Python Required

To run this Python script every time you start your computer, follwo theese steps
(For Windows)
Method 1:

Convert the script into an executable (optional but recommended). 
You can use PyInstaller to do this:
""
pip install pyinstaller
pyinstaller --onefile your_script.py
""

This will generate an executable file in the dist folder.

Method 2:

Create a shortcut to the Python script:
Right-click on your desktop (or any folder), and select New > Shortcut.

Name the shortcut, the same as your main file

Double-click the shortcut to make sure it runs the script and shows the popup with a random quote.

Shell Startup:

Press Win + R, type shell:startup, and press Enter. This opens the Windows Startup folder.
Copy the Python script /the shortcut or its executable to this folder.
(Make sure it runs via the terminal)
Every time you start your PC, the script will run and display a random quote in a popup window


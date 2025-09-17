A minimal, sleek Python desktop app to manage and display motivational quotes. 
Add your favorite quotes and have them shown to you at the start of powering on 
through a stylish popup.

Features

- Edit and save up to 5 quotes
- Random popup display with --popup flag
- Simple GUI for editing quotes
- Clean and modern dark-blue themed interface
- quotes.json stores your quotes and is created and managed by the app.

Notes

You can run the script directly with Python, or build it into a standalone executable for sharing.
On Windows/macOS, you can use system startup folders or login items to launch the app on boot.
On Linux, use a .desktop file in your autostart config.

How to use:

On terminal
- python motivaiton.py (GUI)
- python motivation.py --popup (Random Qoute Popop)

Packaging into a Standalone App (Optional)

Windows
1. Install PyInstaller (pyinstaller --onefile motivation.py)
2. Find motivation.exe inside the dist/ folder.
2.1 Create a Shortcut with --popup
2.2 Navigate to dist/ and right-click motivation.exe → "Create shortcut".
2.3 Right-click the shortcut → Properties.
2.4 In Target, add --popup at the end: ("C:\Path\To\motivation.exe" --popup)
2.5 To make it launch on startup:
Press Win + R, type shell:startup, and hit Enter.
Move your shortcut into that folder.


Linux 
1. pyinstaller --onefile motivation.py
2. Add to Startup:
3. Create a .desktop file in ~/.config/autostart/:
  [Desktop Entry]
  Type=Application
  Exec=/path/to/motivation --popup
  Hidden=false
  NoDisplay=false
  X-GNOME-Autostart-enabled=true
  Name=Motivation
  Comment=Show a motivational popup on startup

3.1
   chmod +x ~/.config/autostart/motivation.desktop


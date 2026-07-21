# Raspberry Pi Touchscreen Colour App

A fullscreen app for the display connected as the Raspberry Pi's primary
desktop screen (normally HDMI0). Each USB touchscreen press changes the colour.

## Run it

On the Raspberry Pi, open a terminal in this directory and run:

```sh
chmod +x run_touchscreen.sh
./run_touchscreen.sh
```

USB touchscreens usually appear as a mouse automatically, so no touch-specific
Python package is required. Press `Esc` on a keyboard to exit. Space also changes
the colour for testing.

If Tkinter is missing, install it with:

```sh
sudo apt update
sudo apt install python3-tk
```

## Start automatically after desktop login

```sh
mkdir -p ~/.config/autostart
nano ~/.config/autostart/touchscreen-colours.desktop
```

Paste the following, replacing `/home/pi/KioskBot-RPI` with the actual project
directory:

```ini
[Desktop Entry]
Type=Application
Name=Touchscreen Colours
Exec=/home/pi/KioskBot-RPI/run_touchscreen.sh
Terminal=false
```

HDMI0 should be configured as the primary display in Raspberry Pi OS Screen
Configuration. The app uses that primary desktop screen.

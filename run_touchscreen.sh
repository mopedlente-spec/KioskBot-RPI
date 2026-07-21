#!/bin/sh
# Raspberry Pi OS normally runs the first graphical desktop on display :0.
export DISPLAY="${DISPLAY:-:0}"
exec python3 "$(dirname "$0")/touchscreen_colors.py"

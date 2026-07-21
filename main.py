#!/usr/bin/env python3
"""
Fullscreen touchscreen color-changer for Raspberry Pi 5.
Runs directly on the framebuffer via SDL's kmsdrm driver - no X11/Wayland
or window manager required.

Tap the screen: background changes to a random color.
Press ESC (if a keyboard is attached) or Ctrl+C in the terminal to quit.
"""

import os
import random
import sys

# Force SDL to draw directly via KMS/DRM (no X server, no window manager).
# If this doesn't work on your setup, try "fbcon" or "directfb" instead.
os.environ.setdefault("SDL_VIDEODRIVER", "kmsdrm")

# Uncomment and adjust if you need to target a specific DRM device/connector
# (useful if you ever re-enable both HDMI outputs):
# os.environ.setdefault("SDL_KMSDRM_DEVICE_INDEX", "0")

import pygame  # noqa: E402  (import after setting env vars)


def random_color(exclude=None):
    """Pick a random RGB color, avoiding repeats of the current one."""
    while True:
        color = tuple(random.randint(0, 255) for _ in range(3))
        if color != exclude:
            return color


def main():
    pygame.init()
    pygame.mouse.set_visible(False)  # hide cursor on a touchscreen kiosk

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = screen.get_size()

    bg_color = random_color()
    screen.fill(bg_color)
    pygame.display.flip()

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            # Regular mouse/touch-as-mouse click (works via evdev on X11/console)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bg_color = random_color(exclude=bg_color)
                screen.fill(bg_color)
                pygame.display.flip()

            # True multitouch finger events (SDL reports these on kmsdrm too)
            elif event.type == pygame.FINGERDOWN:
                bg_color = random_color(exclude=bg_color)
                screen.fill(bg_color)
                pygame.display.flip()

        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pygame.quit()
        sys.exit(0)
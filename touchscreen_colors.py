#!/usr/bin/env python3
"""Fullscreen Raspberry Pi touchscreen colour changer."""

import random
import tkinter as tk


COLOURS = (
    "#EF4444",  # red
    "#F97316",  # orange
    "#FACC15",  # yellow
    "#22C55E",  # green
    "#06B6D4",  # cyan
    "#3B82F6",  # blue
    "#8B5CF6",  # violet
    "#EC4899",  # pink
)


class ColourScreen:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Touchscreen Colours")
        self.root.attributes("-fullscreen", True)
        self.root.configure(cursor="none")

        self.current_colour = random.choice(COLOURS)
        self.label = tk.Label(
            self.root,
            text="TOUCH THE SCREEN",
            font=("DejaVu Sans", 42, "bold"),
            fg="white",
            bg=self.current_colour,
        )
        self.label.pack(fill="both", expand=True)

        # A USB touchscreen normally reports touches as mouse-button presses.
        self.root.bind("<ButtonPress-1>", self.change_colour)
        self.root.bind("<space>", self.change_colour)
        self.root.bind("<Escape>", lambda _event: self.root.destroy())

    def change_colour(self, _event: object = None) -> None:
        choices = [colour for colour in COLOURS if colour != self.current_colour]
        self.current_colour = random.choice(choices)
        self.label.configure(bg=self.current_colour)

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    ColourScreen().run()

"""A sample GUI."""

# pylint: disable=wildcard-import,unused-wildcard-import

from tkinter import *
from tkinter.ttk import *  # type: ignore

import log

from . import utils


class Application:
    """A sample class."""

    def __init__(self):
        log.info("Starting the application...")

        # Configure the root window
        self.root = Tk()
        self.root.title("Feet to Meters")
        self.root.minsize(400, 150)

        # Initialize elements
        self.feet = StringVar()
        self.meters = StringVar()
        frame = self.init(self.root)
        frame.pack(fill=BOTH, expand=1)

        # Start the event loop
        self.root.mainloop()

    def init(self, root):
        padded = {'padding': 5}
        sticky = {'sticky': NSEW}

        # Configure grid
        frame = Frame(root, **padded)  # type: ignore
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)

        def frame_inputs(root):
            frame = Frame(root, **padded)  # type: ignore

            # Configure grid
            frame.rowconfigure(0, weight=1)
            frame.rowconfigure(1, weight=1)
            frame.columnconfigure(0, weight=1)
            frame.columnconfigure(1, weight=1)
            frame.columnconfigure(2, weight=1)

            # Place widgets
            entry = Entry(frame, width=7, textvariable=self.feet)
            entry.grid(column=1, row=0)
            entry.focus()
            label = Label(frame, text="feet")
            label.grid(column=2, row=0)
            label = Label(frame, text="is equivalent to")
            label.grid(column=0, row=1)
            label = Label(frame, text="meters")
            label.grid(column=2, row=1)
            label = Label(frame, textvariable=self.meters)
            label.grid(column=1, row=1)

            return frame

        def frame_commands(root):
            frame = Frame(root, **padded)  # type: ignore

            # Configure grid
            frame.rowconfigure(0, weight=1)
            frame.columnconfigure(0, weight=1)

            # Place widgets
            button = Button(frame, text="Calculate", command=self.calculate)
            button.grid(column=0, row=0)
            self.root.bind('<Return>', self.calculate)

            return frame

        def separator(root):
            return Separator(root)

        # Place widgets
        frame_inputs(frame).grid(row=0, **sticky)
        separator(frame).grid(row=1, padx=10, pady=5, **sticky)
        frame_commands(frame).grid(row=2, **sticky)

        return frame

    def calculate(self, event=None):
        log.debug("Event: %s", event)
        meters = utils.feet_to_meters(self.feet.get())
        if meters is not None:
            self.meters.set(meters)


def main():
    log.init()
    Application()


if __name__ == '__main__':  # pragma: no cover
    main()

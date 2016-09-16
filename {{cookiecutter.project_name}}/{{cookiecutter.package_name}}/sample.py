"""A sample module."""

{%- if cookiecutter.python_major_version == "3" %}
import tkinter as tk
from tkinter import ttk
{%- else %}
import Tkinter as tk
import ttk
{%- endif %}
import logging


log = logging.getLogger(__name__)


class Application(object):
    """A sample class."""

    def __init__(self):
        log.info("Starting the application...")

        # Configure the root window
        self.root = tk.Tk()
        self.root.title("Feet to Meters")
        self.root.minsize(400, 150)

        # Initialize elements
        self.feet = tk.StringVar()
        self.meters = tk.StringVar()
        frame = self.init(self.root)
        frame.pack(fill=tk.BOTH, expand=1)

        # Start the event loop
        self.root.mainloop()

    def init(self, root):
        padded = {'padding': 5}
        sticky = {'sticky': tk.NSEW}

        # Configure grid
        frame = ttk.Frame(root, **padded)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)

        def frame_inputs(root):
            frame = ttk.Frame(root, **padded)

            # Configure grid
            frame.rowconfigure(0, weight=1)
            frame.rowconfigure(1, weight=1)
            frame.columnconfigure(0, weight=1)
            frame.columnconfigure(1, weight=1)
            frame.columnconfigure(2, weight=1)

            # Place widgets
            entry = ttk.Entry(frame, width=7, textvariable=self.feet)
            entry.grid(column=1, row=0)
            entry.focus()
            label = ttk.Label(frame, text="feet")
            label.grid(column=2, row=0)
            label = ttk.Label(frame, text="is equivalent to")
            label.grid(column=0, row=1)
            label = ttk.Label(frame, text="meters")
            label.grid(column=2, row=1)
            label = ttk.Label(frame, textvariable=self.meters)
            label.grid(column=1, row=1)

            return frame

        def frame_commands(root):
            frame = ttk.Frame(root, **padded)

            # Configure grid
            frame.rowconfigure(0, weight=1)
            frame.columnconfigure(0, weight=1)

            # Place widgets
            button = ttk.Button(frame, text="Calculate", command=self.calculate)
            button.grid(column=0, row=0)
            self.root.bind('<Return>', self.calculate)

            return frame

        def separator(root):
            return ttk.Separator(root)

        # Place widgets
        frame_inputs(frame).grid(row=0, **sticky)
        separator(frame).grid(row=1, padx=10, pady=5, **sticky)
        frame_commands(frame).grid(row=2, **sticky)

        return frame

    def calculate(self, event=None):
        log.debug("Event: %s", event)
        try:
            value = float(self.feet.get())
        except ValueError:
            log.error("Unable to convert to float: %s", self.feet.get())
        else:
            self.meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)


def function(value):
    """A function with branches to demonstrate branch coverage reporting."""
    if value is True:
        return 'True'
    elif value is False:
        return 'False'
    else:
        return 'None'


def function_with_network_stuff():
    """A sample function that might take a long time to test."""
    return True


def function_with_disk_stuff():
    """A sample function that might take a long time to test."""
    return False

# Winbox

![image](https://img.shields.io/github/languages/code-size/hazyfossa/winbox?style=flat&label=size)
[![image](https://img.shields.io/pypi/v/winbox.svg)](https://pypi.python.org/pypi/winbox)
[![image](https://img.shields.io/pypi/l/winbox.svg)](https://pypi.python.org/pypi/winbox)
[![image](https://img.shields.io/pypi/pyversions/winbox.svg)](https://pypi.python.org/pypi/winbox)

A lightweight helper for creating windows message boxes.
Built to be as slim as possible. No dependencies, except Python itself!

Useful when you:

- only need a message-box notification in your app, nothing more.
- want a simple GUI for your script, without the complexity of a full framework.
- are writing a background service and need to notify the user, without unexpectedly opening a terminal.

# Example

```py
from winbox import Box, Type, Response, Icon

box = Box("Example App", type=Type.YESNO, icon=Icon.QUESTION)

response = box.send("Is this example working?")

match response:
    case Response.YES:
        print("Great!")
    case Response.NO:
        print("Uh-oh...")
```

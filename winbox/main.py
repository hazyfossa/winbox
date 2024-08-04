import ctypes
from dataclasses import dataclass
from enum import IntEnum
from platform import system
from threading import Thread
from typing import Callable, Literal, overload

if system() != "Windows":
    raise ImportError("Winbox is only available on Windows.")


def _box(title: str, text: str, flag: int, window: int = 0):
    return ctypes.windll.user32.MessageBoxW(window, text, title, flag)


class Type(IntEnum):
    OK = 0
    OKCANCEL = 1
    ABORTRETRYIGNORE = 2
    YESNOCANCEL = 3
    YESNO = 4
    RETRYCANCEL = 5


class Response(IntEnum):
    OK = 1
    CANCEL = 2
    ABORT = 3
    RETRY = 4
    IGNORE = 5
    YES = 6
    NO = 7
    TRYAGAIN = 10
    CONTINUE = 11


class Icon(IntEnum):
    NONE = 0
    ERROR = 16
    QUESTION = 32
    WARNING = 48
    INFO = 64


class Modality(IntEnum):
    APP = 0
    SYSTEM = 4096
    TASK = 8192


DefaultButton = Literal[1, 2, 3, 4]
default_button_flags: dict[DefaultButton, int] = {1: 0, 2: 256, 3: 512, 4: 768}


@dataclass
class Box:
    title: str
    type: Type
    default_message: str | None = None
    icon: Icon = Icon.NONE
    modality: Modality = Modality.APP
    default_button: DefaultButton = 1
    window: int | None = None

    @overload
    def send(self, message: str | None, callback: Callable[[Response], None]) -> None: ...

    @overload
    def send(self, message: str | None, callback: Literal[None] = None) -> Response: ...

    def send(self, message: str | None = None, callback: Callable[[Response], None] | None = None) -> Response | None:
        if callback:
            Thread(target=lambda: callback(self.send(message))).start()
            return

        message = message or self.default_message

        if message is None:
            raise Exception("Message isn't specified.")

        flag = self.type | self.icon | self.modality | default_button_flags[self.default_button]

        return _box(self.title, message, flag)

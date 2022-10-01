# -*- coding: utf-8 -*-

# Developed by Ahegao Devs
# Written by: SantaSpeen
# Licence: MIT
# (c) ahegao.ovh 2022

from _typeshed import SupportsWrite
from asyncio import AbstractEventLoop
from typing import AnyStr, NoReturn


class ConsoleIO:

    @staticmethod
    def write(s: AnyStr): ...

    @staticmethod
    def write_err(s: AnyStr): ...

    @staticmethod
    def read(): ...


class Console(object):

    def __init__(self,
                 prompt_in: str = ">",
                 prompt_out: str = "]:",
                 not_found: str = "Command \"%s\" not found in alias.",
                 file: SupportsWrite[str] or None = Console,
                 debug: bool = False,
                 async_loop: AbstractEventLoop = None) -> NoReturn:

        self.get_IO: ConsoleIO = ConsoleIO
        self.is_run: bool = False

    def __getitem__(self, item): ...
    @property
    def alias(self) -> dict: ...
    def add(self, key: str, func, argv: bool = False, man: str = "No have manual message") -> dict:...
    def log(self, s: AnyStr, r='\r') -> NoReturn: ...
    def __lshift__(self, s: AnyStr) -> NoReturn:
        self.write(s)
    def write(self, s: AnyStr, r='\r') -> NoReturn: ...
    def logger_hook(self) -> NoReturn: ...
    def builtins_hook(self) -> NoReturn: ...
    def run(self) -> NoReturn: ...
    def run_while(self, whl) -> NoReturn:...
    async def async_run(self) -> NoReturn: ...
    async def async_run_while(self, whl) -> NoReturn: ...

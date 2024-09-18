from typing import Optional

class IO:
    _prompt: str

    def __init__(self, kargs: list[str]) -> None:
        self._kargs = kargs

    def output(self) -> Optional[str]:
        return self._prompt if self._prompt else None

    def input(self, prompt: str) -> None:
        if type(prompt) != str:
            raise TypeError(prompt)
        self._prompt = prompt

    def get_kargs(self) -> Optional[list[str]]:
        return self._kargs if len(self._kargs) > 0 else None
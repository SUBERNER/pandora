import Massma
import os


def full(source: str, *, deep_search: bool = False, inverse_search: bool = False, chance: float = 1) -> list[str]:
    try:
        pass
    except Exception as e:
        Massma.Display.audio.error_result(source, "full", e)
        return []


def name(source: str) -> list[str]:
    try:
        pass
    except Exception as e:
        Massma.Display.audio.error_result(source, "name", e)
        return []


def content(source: str) -> list[str]:
    try:
        pass
    except Exception as e:
        Massma.Display.audio.error_result(source, "content", e)
        return []
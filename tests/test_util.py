"""
Test utilities
Updated for GitHub: October 2022
"""


def function_exists(obj: object, func: str) -> bool:
    has_attr = hasattr(obj, func)
    has_call = hasattr(getattr(obj, func), '__call__')
    return has_attr and has_call
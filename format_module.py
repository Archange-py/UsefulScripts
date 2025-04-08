"""
A script containing a single function for introspection
of python modules and their functions.
"""

from types import ModuleType, FunctionType

from typing import Optional, Any

from inspect import signature

from pathlib import Path


def GetAndFormateModule(module: str | Path, /, verbose: bool = True) -> Optional[ModuleType]:
    """A function for introspection of python modules and their functions
    with display in stdout.

    Args:
        module (str | Path): The name of the module if it's in the current directory, or the global path to access it.
        verbose (bool, optional): Indicates whether the function will display various information about the module. Defaults to True.

    Returns:
        Optional[ModuleType]: Returns the module loaded as input.
    """
    try:
        module: ModuleType = __import__(module)

    except ImportError:
        print(f"Module {module} not found in the current directory. Maybe you can use its global path.")

        return

    if verbose:
        not_private_objects: list[Any] = [
            obj for obj in dir(module)
            if not obj.startswith(('__', '_'))
        ]

        functions: list[FunctionType] = [
            getattr(module, obj) for obj in not_private_objects
            if type(getattr(module, obj)) is FunctionType
        ]

        signatures: str = "".join([
            f"(function) {func.__name__} • {str(signature(func))}\n\n{'' if func.__doc__ is None else '   ' + func.__doc__}\n"
            for func in functions
        ])

        docstring: str = "   ".join(module.__doc__.splitlines(True))

        print(f"Module '{module.__name__}' :\n{docstring}\n{signatures}".replace('\n\n\n', '\n\n'))

    return module

import os


def get_hook_dirs():
    """Provides PyInstaller hooks provided by this distribution.

    This is referenced by the hook registration entry point that is provided
    when the package is installed from `setup.cfg`.
    https://pyinstaller.readthedocs.io/en/stable/hooks.html

    Returns:
        list: Contains the path to this directory, where the PyInstaller hooks are located.
    """
    return [os.path.dirname(__file__)]

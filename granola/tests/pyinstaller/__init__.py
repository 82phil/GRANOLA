import os


def get_PyInstaller_tests():
    """Provides PyInstaller the tests provided by this distribution.

    This is referenced by the hook registration entry point that is provided
    when the package is installed from `setup.cfg`.
    https://pyinstaller.readthedocs.io/en/stable/hooks.html

    Returns:
        list: Contains the path to this directory, where the PyInstaller tests are located.
    """
    return [os.path.dirname(__file__)]

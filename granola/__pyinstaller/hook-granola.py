""" PyInstaller hook, used by PyInstaller when it is freezing this package """
# https://pyinstaller.readthedocs.io/en/stable/hooks.html
# https://pyinstaller-sample-hook.readthedocs.io/en/latest/index.html

from PyInstaller.utils.hooks import copy_metadata

# Preserve the package metadata from pySerial so the version can be identified
datas = copy_metadata("pyserial")

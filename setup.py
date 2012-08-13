# setup.py
from distutils.core import setup
import py2exe

setup(console=["eCIP.py"],     windows = [
        {
            "script": "eCIP.py",
            "icon_resources": [(1, "Icon.ico")]
        }
    ],options = { "py2exe":{"dll_excludes":["MSVCP90.dll"],"optimize": 2, "includes": ["sip", "PyQt4.QtGui"]}})


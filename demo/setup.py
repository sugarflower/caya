import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"

#exe化したいファイルをscriptに指定する
exe = Executable(
    script="ThreeD.py",
    shortcut_name = "テストプログラム",
    shortcut_dir = "ProgramMenuFolder",
    icon="setsu.ico",
    base=base
    )


includefiles = ["res"]
includes = []
excludes = ["PyQt4","PyQt5","numpy","PyInstaller","PySide2"]
packages = ["pygame",]


setup(name = "ThreeD demo",
      version="0.1",
      description="Demo",
      author = "JaneRoe",
      options={
          "build_exe":{
              "includes":includes, 
              "excludes":excludes,
              "packages":packages,
              "include_files":includefiles
              }
          },
      executables=[exe]
      )

import ctypes
import os

# Get the current working directory
current_directory = os.getcwd()
# Construct the full path to the DLL
dll_path = os.path.join(current_directory, "qJXcUpPEoTWdBAeu.game")
myDll = ctypes.cdll.LoadLibrary(dll_path)
#!flask/bin/python
from flask import Flask
from flask import render_template
import json
import os
import ctypes
from ctypes import wintypes
import time
# import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)
app = Flask(__name__)

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
  _fields_ = (("dx",          wintypes.LONG),
              ("dy",          wintypes.LONG),
              ("mouseData",   wintypes.DWORD),
              ("dwFlags",     wintypes.DWORD),
              ("time",        wintypes.DWORD),
              ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
  _fields_ = (("wVk",         wintypes.WORD),
              ("wScan",       wintypes.WORD),
              ("dwFlags",     wintypes.DWORD),
              ("time",        wintypes.DWORD),
              ("dwExtraInfo", wintypes.ULONG_PTR))

def __init__(self, *args, **kwds):
  super(KEYBDINPUT, self).__init__(*args, **kwds)
  # some programs use the scan code even if KEYEVENTF_SCANCODE
  # isn't set in dwFflags, so attempt to map the correct code.
  if not self.dwFlags & KEYEVENTF_UNICODE:
    self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                          MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
  class _INPUT(ctypes.Union):
    _fields_ = (("ki", KEYBDINPUT),
                ("mi", MOUSEINPUT),
                ("hi", HARDWAREINPUT))
  _anonymous_ = ("_input",)
  _fields_ = (("type",   wintypes.DWORD),
              ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
  if result == 0:
    raise ctypes.WinError(ctypes.get_last_error())
  return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
  LPINPUT,       # pInputs
  ctypes.c_int)  # cbSize

def PressKey(hexKeyCode):
  x = INPUT(type=INPUT_KEYBOARD,
            ki=KEYBDINPUT(wVk=hexKeyCode))
  user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
  x = INPUT(type=INPUT_KEYBOARD,
            ki=KEYBDINPUT(wVk=hexKeyCode,
            dwFlags=KEYEVENTF_KEYUP))
  user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

@app.route('/buzz/')
def main():
  return render_template("index.html")

@app.route('/buzz/buttons/<int:player>')
def buttons(player):
  with open('button_mappings/player_' + str(player) + '.json') as f:
    player_mappings = json.load(f)
  return render_template("buttons.html", player_mappings=player_mappings, server_url=os.environ.get("WEB_SERVER_URL"))

@app.route('/buzz/trigger/<string:key>')
def trigger(key):
  PressKey(int(key, 0))
  ReleaseKey(int(key, 0))
  return ""

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))

import time
import ctypes 

ApplicationToClose = "Application Name.exe"

while True:
    window = ctypes.c_char_p(bytes())
    ActiveWindowHandle = ctypes.windll.user32.GetForegroundWindow()
    ctypes.windll.user32.GetWindowTextA(ActiveWindowHandle, window, 255)
    if ApplicationToClose in str(window.value):
        ctypes.windll.user32.PostMessageA(ActiveWindowHandle, 16, 0, 0)
        print("Application Closed"%(ApplicationToClose))
        time.sleep(0.1)
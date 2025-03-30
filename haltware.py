import time
import ctypes 

ApplicationToClose = "Notepad" # sample application to close

while True:
    window = ctypes.create_string_buffer(255)
    ActiveWindowHandle = ctypes.windll.user32.GetForegroundWindow()
    
    # Get the window title
    ctypes.windll.user32.GetWindowTextA(ActiveWindowHandle, window, 255)
    
    # Check if the application title matches
    if ApplicationToClose.encode() in window.value:
        ctypes.windll.user32.PostMessageA(ActiveWindowHandle, 16, 0, 0)  # Send WM_CLOSE message
        print(f"Application Closed: {ApplicationToClose}")
        time.sleep(1)  # Increased sleep time to reduce CPU usage
    else:
        time.sleep(5)  # Reduce polling frequency when no match is found

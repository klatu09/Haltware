# Haltware
This Python script runs automatically when the computer starts and prevents a specific application from opening. It continuously monitors active processes and terminates the target application if detected. Useful for parental control, productivity enforcement, or system security. 

I increased the sleep time to reduce the CPU and the polling frequency when the app desired or inputted in the code is not in the task manager.


This is an improved version of the script of programming-matrix.

youtube video: https://www.youtube.com/watch?v=SMIvPE-37-0


██╗  ██╗██╗      █████╗ ████████╗██╗   ██╗
██║ ██╔╝██║     ██╔══██╗╚══██╔══╝██║   ██║
█████╔╝ ██║     ███████║   ██║   ██║   ██║
██╔═██╗ ██║     ██╔══██║   ██║   ██║   ██║
██║  ██╗███████╗██║  ██║   ██║   ╚██████╔╝
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ 
                                          


✦ Project 2: Haltware
✦ Author: K1atu
✦ Motto: "you get some, you hack some"

# Haltware
Silent. A bit Untraceable. Efficient.


# DISCLAIMER 
I am not responsible for any of your actions. This GitHub repository is made for educational purposes only.


##  Signature  
💀 Crafted by **K1atu** 

## How to use?

 1. First convert the py file into an executable file
 2. in cmd run the ff command, pip install pyinstaller
 3. cd to directory, in my case i put it into my desktop
 4. pyinstaller --noconsole --onefile "python file"
 5. Paste the exe file into this directory "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup" - this ensures that it runs every after window is open, so you don't have to manually run it.


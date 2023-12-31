import tkinter as tk
from tkinter import font
import userMode
import cv2
from PIL import Image, ImageTk
import adminMode

title = "Capstone"
fontChoice = 'Arial'
bgcolor = "#EBE6D9"
#Change both if you want to adjust the size of the window
windowSize = "900x500"
windowSizeX = 810
windowSizeY = 500

#to be changed later!
definedUser = "admin"
definedPassword = "nimda"




def welcomeScreen():
    for widget in root.winfo_children():
        widget.destroy()
    pickText = tk.Label(root, text = "Please pick a user type:", font=(fontChoice, 40), bg=bgcolor)
    pickText.pack(pady=20)

    frame = tk.Frame(root, bg=bgcolor)
    frame.pack(expand=True)

    #Buttons
    adminButton = tk.Button(frame, text="Admin Mode", command=adminScreen, bg="red", fg="white", font=font.Font(family=fontChoice, size=32))
    adminButton.pack(side=tk.LEFT, padx=10)
    userButton = tk.Button(frame, text="User Mode", command=start_userMode, bg="green", fg="white", font=font.Font(family=fontChoice, size=32))
    userButton.pack(side=tk.LEFT, padx=10)

def start_userMode():
    root.destroy()
    userMode.start_app()

def adminScreen():
    # clear screen
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("900x270")

    def credentialsCheck(username, password):
        if(username == definedUser and password == definedPassword):
            print("here")
            root.destroy()
            adminMode.start_app()
        elif(password != definedPassword or username != definedUser):
            prompt = tk.Label(root, text = "Password does not match User Information!", fg="red", font = (fontChoice, 20))
            prompt.pack(pady=10,anchor=tk.W)

    adminText = tk.Label(root, text = "Admin Mode:", font = (fontChoice, 35), bg=bgcolor)
    adminText.pack(anchor=tk.W)

    prompt = tk.Label(root, text = "Please Enter your username and password.", font = (fontChoice, 20),bg=bgcolor)
    prompt.pack(pady=10,anchor=tk.W)

    #text entry frame
    entryFrame = tk.Frame(root,bg=bgcolor)
    entryFrame.rowconfigure(0, weight=1)
    entryFrame.rowconfigure(1, weight=1)
    entryFrame.columnconfigure(0, weight=1)
    entryFrame.columnconfigure(1, weight=3)

    userNameText = tk.Label(entryFrame, text = "Username:", font = (fontChoice, 25),bg=bgcolor)
    userNameText.grid(row=0, column=0, sticky=tk.E)
    userNameEntry = tk.Entry(entryFrame, font = (fontChoice, 25))
    userNameEntry.grid(row=0, column=1, sticky=tk.E+tk.W)

    passwordText = tk.Label(entryFrame, text = "Password:", font = (fontChoice, 25),bg=bgcolor)
    passwordText.grid(row=1, column=0, sticky=tk.E)
    passwordEntry = tk.Entry(entryFrame, font = (fontChoice, 25))
    passwordEntry.grid(row=1, column=1, sticky=tk.E+tk.W)

    enterButton = tk.Button(entryFrame, text = "Enter", command = lambda:credentialsCheck(userNameEntry.get(), passwordEntry.get()), font = (fontChoice, 30))
    enterButton.grid(row=2, column=1, sticky=tk.E+tk.W)

    entryFrame.pack(padx = 30, fill='x')



def mainScreen():
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry(windowSize)

    cap = cv2.VideoCapture(0)

    videoFrame = tk.Frame(root, borderwidth=2, relief='solid')
    videoFrame.pack(padx=10, pady=10)

    canvasWidth = 400
    canvasHeight = 300
    canvas = tk.Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()

    def updateVideo():
        #cap.get(3) = width of video, cap.get(4) = height of video
        ret, frame = cap.read()
        if ret:
            #4:3 aspect ratio
            croppedWidth = int((4/3) * cap.get(4))

            difference = int((cap.get(3) - croppedWidth))
            displacement = int(difference / 2)

            croppedVideoFrame = frame[0:int(cap.get(4)), 0+displacement:int(cap.get(3) - displacement)]
            croppedVideoFrame = cv2.resize(croppedVideoFrame, (canvasWidth, canvasHeight))
            croppedVideoFrame = cv2.cvtColor(croppedVideoFrame, cv2.COLOR_BGR2RGB)

            photo = ImageTk.PhotoImage(image=Image.fromarray(croppedVideoFrame))

            canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            canvas.image = photo
        
        root.after(20, updateVideo)

    updateVideo()
    #videoDisplay()
    #videoHolder = tk.Label(root)


    
#Base window creation
root = tk.Tk()

#Background Color
root.configure(bg=bgcolor)

#Window size
root.geometry(windowSize)
#Window title
root.title(title)

welcomeScreen()

root.mainloop()


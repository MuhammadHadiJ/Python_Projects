import piexif
import customtkinter as tk
from customtkinter import *

Window = tk.CTk()
Window.geometry("800x500")
Window.title("Meta Data Editor")
set_appearance_mode("dark")

MainFrame = tk.CTkFrame(Window,width=750,height=425,fg_color="#6F4E37")
MainFrame.pack_propagate(False)
MainFrame.place(x=25,y=50)
CompanyLogo = CTkLabel(Window,text="MetaData Editor",text_color="#FDFFFC",font=("Versa Versa",24))
CompanyLogo.place(x=295,y=12)

Options = tk.CTkComboBox(MainFrame,values=["Read                                                                   ", "Write", "Transplant"],width=320)
Options.place(x=110,y=15)
OptionsLabel = tk.CTkLabel(MainFrame,text="Tool Options:",text_color="#FDFFFC",font=("Roboto",14))
OptionsLabel.place(x=20,y=15)

def SelectFile(event):
    PathEntery.unbind("<FocusIn>")
    filepath = filedialog.askopenfilename(title="Select File")
    if filepath:
        PathEntery.delete(0,tk.END)
        PathEntery.insert(0,filepath)
        GetMetaData()
    Window.focus()
    Window.after(1000, lambda: PathEntery.bind("<FocusIn>", SelectFile))
    Window.focus()

PathEntery = tk.CTkEntry(MainFrame,width=400,placeholder_text="Click here to select path...")
PathEnteryLabel = tk.CTkLabel(MainFrame,text="Enter Image Path:",text_color="#FDFFFC",font=("Roboto",14))
ReadResult = tk.CTkLabel(MainFrame,text="Image Meta Data:",text_color="#FDFFFC",font=("Roboto",14))
ReadFrame = tk.CTkFrame(MainFrame,width=710,height=290,fg_color="#242424")
ReadFrameText = tk.CTkLabel(ReadFrame,text="File not selected yet..." ,text_color="#FDFFFC",font=("Roboto",14),justify="left")

def GetMetaData():
    path = PathEntery.get()
    MetaData = piexif.load(path)
    Make = MetaData["0th"][piexif.ImageIFD.Make].decode('utf-8')
    Model = MetaData["0th"][piexif.ImageIFD.Model].decode('utf-8')
    DateTime = MetaData["0th"][piexif.ImageIFD.DateTime].decode('utf-8')
    ShutterSpeed = MetaData["Exif"][piexif.ExifIFD.ShutterSpeedValue]
    ISOo = MetaData["Exif"][piexif.ExifIFD.ISOSpeedRatings]
    Aperture = MetaData["Exif"][piexif.ExifIFD.FNumber]
    Focal = MetaData["Exif"][piexif.ExifIFD.FocalLength]
    Software = MetaData["0th"][piexif.ImageIFD.Software].decode('utf-8')
    Flash = MetaData["Exif"][piexif.ExifIFD.Flash]
    ColourSpace = MetaData["Exif"][piexif.ExifIFD.ColorSpace]
    ReadFrameText.configure(text="Make: "+Make+"\nModel: "+Model+"\nDate & Time: "+DateTime+"\nShutter Speed: "+str(ShutterSpeed)+
                            "\nISO: "+str(ISOo)+"\nAperture: "+str(Aperture)+"\nFocalLegnth (Zoom): "+str(Focal)+"\nSoftware: "+Software
                            +"\nFlash: "+str(Flash)+"\nColour Space: "+str(ColourSpace))

def ReadMode():
    PathEnteryLabel.place(x=20,y=50)
    PathEntery.place(x=140,y=50)
    PathEntery.bind("<FocusIn>",SelectFile)
    ReadResult.place(x=20,y=85)
    ReadFrame.place(x=20,y=120)
    ReadFrameText.place(x=20,y=15)

def SetMainUi(CurrentSetOption):
    if Options.get() == "Read                                                                   ":
        ReadMode()
        print("Current selected option is Read!")
    if Options.get() == "Write":
        print("Current selected option is Write!")
    if Options.get() == "Transplant":
        print("Current selected option is Transplant!")
    
    print(CurrentSetOption)

SetMainUi("Read")
Options.configure(command = SetMainUi)

Window.mainloop()
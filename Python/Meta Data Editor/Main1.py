import customtkinter as tk
from customtkinter import *

window = tk.CTk()
window.geometry("800x500")
window.title("JiwBooks")
set_appearance_mode("dark")

CompanyLogo = CTkLabel(window,text="Jiw Books",text_color="#FDFFFC",font=("Versa Versa",24))
CompanyLogo.place(x=340,y=12)
MainFrame = CTkFrame(window,width=750,height=425,fg_color="#6F4E37")
MainFrame.pack_propagate(False)
MainFrame.place(x=25,y=50)

BookNameEntery = CTkTextbox(MainFrame,width=550,corner_radius=5, height=20, fg_color="#01161E", text_color="#FDFFFC")
BookNameEntery.place(y=15,x=175)
EnterBookNameText =CTkLabel(MainFrame,text="Enter Book Name: ",text_color="#FDFFFC",font=("Barlow Medium",18))
EnterBookNameText.place(y=15,x=20)
EnterBookAuthourText = CTkLabel(MainFrame,text="Enter Authour Name: ",text_color="#FDFFFC",font=("Barlow Medium",18))
EnterBookAuthourText.place(y=60,x=20)
BookAuthourEntery = CTkTextbox(MainFrame,width=530,corner_radius=5, height=20, fg_color="#01161E", text_color="#FDFFFC")
BookAuthourEntery.place(y=60,x=197)
BookTypes = ["Not Sure","Course Book","Fiction","Non-Fiction"]
EnterBookType = CTkComboBox(MainFrame,values=BookTypes,width=562,corner_radius=5,fg_color="#01161E",text_color="#FDFFFC",state="readonly")
EnterBookType.place(y=105,x=165)
EnterBookTypeText = CTkLabel(MainFrame,text="Enter Book Type: ",text_color="#FDFFFC",font=("Barlow Medium",18))
EnterBookTypeText.place(x=20,y=105)
EnterPrefferedFileTypeText = CTkLabel(MainFrame,text="Enter Preffered File Type: ",text_color="#FDFFFC",font=("Barlow Medium",18))
EnterPrefferedFileTypeText.place(x=20,y=150)
FileTypes = [".PDF",".EPUB",".TXT","Any"]
EnterPrefferedFileType = CTkComboBox(MainFrame,values=FileTypes,width=500,corner_radius=5,fg_color="#01161E",text_color="#FDFFFC",state="readonly")
EnterPrefferedFileType.place(y=150,x=227)
CollectDataButton = CTkButton(MainFrame,width=130,height=50,corner_radius=10,text="Search",hover_color="#268BCF",fg_color="#2892D7",text_color="#FDFFFC",font=("Barlow Bold",24))
CollectDataButton.place(y=195,x=305)

window.mainloop()
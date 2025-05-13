import subprocess
import os
import customtkinter as CTK

def GetProfiles():
    profilecmd = subprocess.run(["cmd","/c","netsh wlan show profiles"],capture_output=True,text=True)
    f = open("Buffer.txt","w")
    f.write(profilecmd.stdout)
    Profiles = []
    f.close()
    f = open("Buffer.txt","r")
    B = 0
    for i in f:
        B += 1
        if B <= 10:
            pass
        else:
            if i.strip() == "":
                f.close()
                os.remove("Buffer.txt")
                return Profiles
            else:
                result1, result2 = i.strip().split(":")
                Profiles.append(result2.strip())

def GetPass(profile):
    Profile = profile
    output = subprocess.run(["cmd", "/c", f'netsh wlan show profile name="{profile}" key=clear'], text=True, capture_output=True)
    f = open("Buffer2.txt","w")
    f.write(output.stdout)
    f.close()
    f = open("Buffer2.txt","r")
    b=0
    PassLine = ""
    for i in f:
        b+=1
        if b <= 32 or b >= 34:
            pass
        else:
            Junk,PassLine = i.strip().split(":")
    f.close()
    if PassLine == "":
        PassLine = "Unfortunately you have pressed \"forget password\" for this Wifi network"
    return PassLine
def ProfileSelected(choice):
    Pass = GetPass(choice)
    if Pass == "Unfortunately you have pressed \"forget password\" for this Wifi network":
        PassLabel.configure(text=Pass)
    else:
        PassLabel.configure(text="The password for the Wifi is: {}".format(Pass))

app = CTK.CTk()
app.geometry("600x150")
CTK.set_appearance_mode("Dark")
CTK.set_default_color_theme("blue")
app.title("Wifi Pass Finder")

SelectProfile = CTK.CTkLabel(app,text="Select the wifi you want to find the password of:",fg_color="transparent",text_color="#EFEFEF", font=("Roboto",18))
SelectProfile.pack(pady=(10,10))
profiles = GetProfiles()
Selector = CTK.CTkOptionMenu(app,width=550,corner_radius=10,fg_color="#EFEFEF",values=profiles,command=ProfileSelected,dropdown_fg_color="#EFEFEF",dropdown_text_color="#2B2B2B",dropdown_hover_color="#CDCDCD",dropdown_font=("Roboto",13),text_color="#2B2B2B")
Selector.pack(pady=(0,5))
Selector.set("Select a wifi network")
frame = CTK.CTkFrame(app,width=550,height=30,corner_radius=10,fg_color="#1F1F1F")
frame.pack(pady=(15,0))
frame.pack_propagate(False)
PassLabel = CTK.CTkLabel(frame,text=">>> Select a wifi network first",fg_color="transparent",text_color="#EFEFEF", font=("Roboto",13))
PassLabel.pack()
app.mainloop()

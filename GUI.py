import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('500x500')

def host():
    pass

def connect():
    pass

buttonHost = customtkinter.CTkButton(master = root, text = 'Host', command = host)
buttonHost.pack(pady = 120)

buttonConnect = customtkinter.CTkButton(master = root, text = 'Connect', command = connect)
buttonConnect.pack(pady = 12)

root.mainloop()
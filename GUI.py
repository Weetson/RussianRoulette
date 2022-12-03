import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('500x500')

def host():

    def host_aplly():
        print(f'host = "{entryHost.get()}"\nport = {entryPort.get()}\nname = "{entryName.get()}"\nstyle = "host"', file = open('data.py', 'w'))
        import Game


    buttonHost.destroy()
    buttonConnect.destroy()

    labelHost = customtkinter.CTkLabel(root, 200, 30, text = 'Host')
    labelHost.pack(pady = 12)

    entryHost = customtkinter.CTkEntry(root, 140, 30)
    entryHost.pack()

    labelPort = customtkinter.CTkLabel(root, 200, 30, text = 'Port')
    labelPort.pack(pady = 12)

    entryPort = customtkinter.CTkEntry(root, 140, 30)
    entryPort.pack()

    labelName = customtkinter.CTkLabel(root, 200, 30, text = 'Name')
    labelName.pack(pady = 12)

    entryName = customtkinter.CTkEntry(root, 140, 30)
    entryName.pack()

    buttonApply = customtkinter.CTkButton(master = root, text = 'Apply', command = host_aplly)
    buttonApply.pack(pady = 12)

def connect():

    def host_aplly():
        print(f'host = "{entryHost.get()}"\nport = {entryPort.get()}\nname = "{entryName.get()}"\nstyle = "connect"', file = open('data.py', 'w'))
        import Game


    buttonHost.destroy()
    buttonConnect.destroy()

    labelHost = customtkinter.CTkLabel(root, 200, 30, text = 'Host')
    labelHost.pack(pady = 12)

    entryHost = customtkinter.CTkEntry(root, 140, 30)
    entryHost.pack()

    labelPort = customtkinter.CTkLabel(root, 200, 30, text = 'Port')
    labelPort.pack(pady = 12)

    entryPort = customtkinter.CTkEntry(root, 140, 30)
    entryPort.pack()

    labelName = customtkinter.CTkLabel(root, 200, 30, text = 'Name')
    labelName.pack(pady = 12)

    entryName = customtkinter.CTkEntry(root, 140, 30)
    entryName.pack()

    buttonApply = customtkinter.CTkButton(master = root, text = 'Apply', command = host_aplly)
    buttonApply.pack(pady = 12)


buttonHost = customtkinter.CTkButton(master = root, text = 'Host', command = host)
buttonHost.pack(pady = 120)

buttonConnect = customtkinter.CTkButton(master = root, text = 'Connect', command = connect)
buttonConnect.pack(pady = 12)

root.mainloop()
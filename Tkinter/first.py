import tkinter as tk

root = tk.Tk()
root.title("My first Tkinter app")

label = tk.Label(root,text="Hello , Tkinter")
label.pack()

root.geometry("1920x1080")

icon = tk.PhotoImage(file = 'image.png')
root.iconphoto(True , icon)
root.config(background="black")

root.mainloop()
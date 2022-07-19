# Notepad
from tkinter import *
from PIL import ImageTk, Image
from tkinter import StringVar, IntVar, scrolledtext, END, messagebox, filedialog

# Define window
root = Tk()
root.geometry('450x400')


# Define functions
def change_font(event):
    """Change the given font based off dropbox options."""
    if font_option.get() == "none":
        my_font = (font_family.get(), font_size.get())
    else:
        my_font = (font_family.get(), font_size.get(), font_option.get())

        # Change the font style
        input_text.config(font=my_font)


def new_note():
    """Create a new Note which essentially clears the screen."""
    # Use the messagebox to ask for new note
    question = messagebox.askyesno("New Note", "Are you sure you want to start a new note?")
    if question == 1:
        input_text.delete("1.0", END)


def close_note():
    question = messagebox.askyesno("Close note", "Are you sure you want to close this note?")
    if question == 1:
        root.destroy()


def save_note():
    """Save the given note.  First three lines are saved as font family, font size, and font option."""
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    text2 = str(input_text.get(1.0, END))
    f.write(font_family.get() + "\n")
    f.write(str(text2))


def open_note():
    """Open a previously saved note.  First three lines of note are font family, font size, and font option.  First set the font, then load the text."""
    input_text.delete(1.0, END)
    filetypes = (('txt', '*.txt'), ('All', '*.*'))
    f = filedialog.askopenfile(filetypes=filetypes)
    font_family.set(f.readline())
    input_text.insert(1.0, f.read())


# Define Layout and frames
menu = Frame(root, height=40, bg='#C6B38E')
menu.pack(fill=BOTH, expand=False)

text_frame = Frame(root)
text_frame.pack(fill=BOTH, expand=True)

# Layout for menu frame
newimg = PhotoImage(file="new.png")
new = Button(menu, bg='#9a9b73', text="New", fg="red", image=newimg, command=new_note)
new.grid(row=0, column=0, padx=2, pady=2)

saveimg = PhotoImage(file="save.png")
save = Button(menu, bg='#9a9b73', text='Save', image=saveimg, command=save_note)
save.grid(row=0, column=2, padx=2, pady=2)

openimg = PhotoImage(file='open.png')
open1 = Button(menu, bg='#9a9b73', text='Open', fg='red', image=openimg, command=open_note)
open1.grid(row=0, column=3, padx=2, pady=2)

closeimg = PhotoImage(file='close.png')
close = Button(menu, bg='#9a9b73', text='Close', fg='red', image=closeimg, command=close_note)
close.grid(row=0, column=4, padx=2, pady=2)

# Create a list of fonts to use
families = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambria', 'Georgia', 'MS Gothic', 'SimSun',
            'Tahoma', 'Times New Roman', 'Verdana', 'Wingdings']
font_family = StringVar()
font_family_drop = OptionMenu(menu, font_family, *families, command=change_font)
font_family.set("Terminal")
# Set the width so it will fit "times new roman" and remain constant
font_family_drop.config(width=16)
font_family_drop.grid(row=0, column=6, padx=5, pady=5)

sizes = [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
font_size = IntVar()

option = ['none', 'bold', 'italic']
font_option = StringVar()

my_font = (font_family.get(), font_size.get())

# Create input_text as a scrolltext so you can scroll through the text field.
# Set default width and height to be more than the window size so that on the smallest text size, the text field size is constant.
input_text = scrolledtext.ScrolledText(text_frame, width=1000, height=1000, bg='#E7F9A9', font=my_font)
input_text.pack()

# Run the root window's main loop
root.mainloop()
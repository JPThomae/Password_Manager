from tkinter import *
from password_generator import generate_password

BLACK = "#100F0F"
DARK_GRAY = "#0F3D3E"
TAN = "#E2DCC8"
WHITE = "#F1F1F1"


def generate():
    password = generate_password()
    password_entry.insert(0, str(password))


def add():
    if website_entry.get() and user_entry.get() and password_entry.get():
        website = website_entry.get()
        username = user_entry.get()
        password = password_entry.get()

        website_entry.delete(0, END)
        user_entry.delete(0, END)
        password_entry.delete(0, END)

        file = open("data.txt", mode="w")
        file.write(f"{website} | {username} | {password}")


def check_saved():
    data_box.place(x=125, y=225)
    data = open("data.txt")
    for line in data.readlines():
        data_box.insert(0, line)



tv = Tk()
tv.minsize(width=400, height=400)
tv.maxsize(width=400, height=400)
tv.title("Password Manager")
tv.config(bg="white")

canvas = Canvas(width=300, height=200, highlightthickness=0, bg="white")
logo = PhotoImage(file="lock_logo.png")
canvas.create_image(110, 115, image=logo)
canvas.place(x=90, y=0)

canvas2 = Canvas(width=500, height=50, highlightthickness=0, bg=DARK_GRAY)
canvas2.place(x=0, y=0)

canvas3 = Canvas(width=500, height=500, highlightthickness=0, bg=TAN)
canvas3.place(x=0, y=180)

site_text = Label(text="Website:", font=("Rockwell", 10), bg=TAN)
site_text.place(x=30, y=230)

user_text = Label(text="Email/Username:", font=("Rockwell", 10), bg=TAN)
user_text.place(x=10, y=260)

password_text = Label(text="Password:", font=("Rockwell", 10), bg=TAN)
password_text.place(x=25, y=290)

generate_button = Button(height=1, width=16, text="Generate Password", font=("Rockwell", 10),
                         relief="flat", bg=WHITE, command=generate)
generate_button.place(x=260, y=289)

add_button = Button(height=1, width=35, text="Add", font=("Rockwell", 10),
                    relief="flat", bg=WHITE, command=add)
add_button.place(x=127, y=325)

saved_button = Button(height=1, width=8, text="Saved", font=("Rockwell", 10),
                      relief="flat", bg=WHITE, command=check_saved)
saved_button.place(x=25, y=325)

website_entry = Entry(width=42, bg=WHITE)
website_entry.place(x=127, y=232)

user_entry = Entry(width=42, bg=WHITE)
user_entry.place(x=127, y=263)

password_entry = Entry(width=20, bg=WHITE)
password_entry.place(x=127, y=293)

data_box = Text(height=8, width=32)

tv.mainloop()

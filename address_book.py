import tkinter as tk

window = tk.Tk()
window.geometry("800x800")
window.title("Address Book")
"""
image = tk.PhotoImage(file="Math Club Poster.png")

bg_label = tk.Label(window, image=image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
"""
top_frame = tk.Frame(window)
top_frame.pack(side=tk.TOP)

list_frame = tk.Frame(window)
list_frame.pack(side=tk.LEFT)

info_frame = tk.Frame(window, width=500, height=200)
info_frame.pack(side=tk.RIGHT)

book_label = tk.Label(top_frame, text="My Address Book", font=("Arial", 20))
book_label.pack(padx=10, pady=10, side=tk.LEFT)

open_button = tk.Button(top_frame, text="Open", font=("Arial", 20))
open_button.pack(padx=10, pady=10, side=tk.RIGHT)

addressbox = tk.Listbox(list_frame, font=("Arial", 20), height=20)
addressbox.pack(padx=20, pady=20)

edit_button = tk.Button(list_frame, text="Edit", font=("Arial", 20))
edit_button.pack(padx=5, pady=10)

delete_button = tk.Button(list_frame, text="Delete", font=("Arial", 20))
delete_button.pack(padx=5, pady=10)

name_label = tk.Label(info_frame, text="Full Name: ", font=("Arial", 20))
name_label.place(relx=0.05, rely=0.05)

name_entry = tk.Entry(info_frame, font=("Arial", 20), width=10)
name_entry.place(relx=0.55, rely=0.05)

address_label = tk.Label(info_frame, text="Adress: ", font=("Arial", 20))
address_label.place(relx=0.05, rely=0.4)

address_entry = tk.Entry(info_frame, font=("Arial", 20), width=10)
address_entry.place(relx=0.55, rely=0.4)

mobile_label = tk.Label(info_frame, text="Mobile Number: ", font=("Arial", 20))
mobile_label.place(relx=0.05, rely=0.55)

mobile_entry = tk.Entry(info_frame, font=("Arial", 20), width=10)
mobile_label.place(relx=0.55, rely=0.55)


window.mainloop()
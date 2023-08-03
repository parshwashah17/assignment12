
import tkinter as tk
from tkinter import messagebox
from hotelmanagement.guests import add_guest, check_in_guest, check_out_guest, display_guests
from hotelmanagement.exceptions import GuestNotFoundException, GuestAlreadyCheckedInException, GuestNotCheckedInException

def display_menu():
    print("\nMenu:")
    print("1. add guest")
    print("2. check-in guest")
    print("3. check-out guest")
    print("4. display guests")
    print("5. Exit")

def handle_add_guest():
    name = gEntry.get()
    room_number = rNumber_entry.get()
    try:
        add_guest(name, room_number)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def handle_check_in_guest():
    room_number = rNumber_entry.get()
    try:
        check_in_guest(room_number)
    except (GuestNotFoundException, GuestAlreadyCheckedInException) as e:
        messagebox.showerror("Error", str(e))

def handle_check_out_guest():
    room_number = rNumber_entry.get()
    try:
        check_out_guest(room_number)
    except (GuestNotFoundException, GuestNotCheckedInException) as e:
        messagebox.showerror("Error", str(e))

def handle_display_guests():
    display_guests()

# Create the main application window
root = tk.Tk()
root.title("Hotel Management System")

# Create labels and entry fields for guest name and room number
gLabel = tk.Label(root, text="Guest Name:")
gLabel.grid(row=0, column=0, padx=10, pady=5)
gEntry = tk.Entry(root)
gEntry.grid(row=0, column=1, padx=10, pady=5)

rLabel = tk.Label(root, text="Room Number:")
rLabel.grid(row=1, column=0, padx=10, pady=5)
rNumber_entry = tk.Entry(root)
rNumber_entry.grid(row=1, column=1, padx=10, pady=5)

# Create buttons for menu options
addbutton = tk.Button(root, text="Add Guest", command=handle_add_guest)
addbutton.grid(row=2, column=0, padx=10, pady=5)

checkinbutton = tk.Button(root, text="Check In Guest", command=handle_check_in_guest)
checkinbutton.grid(row=2, column=1, padx=10, pady=5)

checkoutbutton = tk.Button(root, text="Check Out Guest", command=handle_check_out_guest)
checkoutbutton.grid(row=2, column=2, padx=10, pady=5)

displaybutton = tk.Button(root, text="Display Guests", command=handle_display_guests)
displaybutton.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

# Start the tkinter main loop
root.mainloop()

from hotelmanagement.filehandling import read_data, write_data
from hotelmanagement.exceptions import GuestNotFoundException, GuestAlreadyCheckedInException, GuestNotCheckedInException

GUEST_FILE = "guests.json"

def add_guest(name, room_number):
    data = read_data(GUEST_FILE)
    if room_number in data:
        raise ValueError("Room number already occupied.")
    data[room_number] = {"name": name, "checked_in": False}
    write_data(GUEST_FILE, data)

def check_in_guest(room_number):
    data = read_data(GUEST_FILE)
    if room_number not in data:
        raise GuestNotFoundException("Room number not found.")
    if data[room_number]["checked_in"]:
        raise GuestAlreadyCheckedInException("Guest is already checked in.")
    data[room_number]["checked_in"] = True
    write_data(GUEST_FILE, data)

def check_out_guest(room_number):
    data = read_data(GUEST_FILE)
    if room_number not in data:
        raise GuestNotFoundException("Room number not found.")
    if not data[room_number]["checked_in"]:
        raise GuestNotCheckedInException("Guest is not checked in.")
    data[room_number]["checked_in"] = False
    write_data(GUEST_FILE, data)

def display_guests():
    data = read_data(GUEST_FILE)
    print("\nGuests in the hotel:")
    for room_number, guest in data.items():
        status = "Checked In" if guest["checked_in"] else "Checked Out"
        print(f"Room {room_number}: {guest['name']} ({status})")

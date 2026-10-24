# 1. Setup Trip Info
shuttle_plate = "KDC 450B"
route = "Nairobi - Eldoret"
ticket_fare = 1200
total_seats = 14

# Data Structures
# List representing seats using 1-based indexing for simplicity, so index 0 is unused
seats = ["Empty"] * (total_seats + 1)

# Dictionary storing passenger details where key is seat_number
passengers = {}

def show_map():
    """Displays the seating map in a grid format."""
    print("\n--- Seating Map ---")
    for seat in range(1, total_seats + 1):
        if seats[seat] == "Booked":
            print(f"[X]\t", end="")
        else:
            print(f"[{seat}]\t", end="")
        
        # Using Modulo to break the line after every 3 seats for a shuttle like layout
        if seat % 3 == 0:
            print()
    print("\n-------------------")

def book_seat():
    """Handles booking a seat, validating input, and generating a receipt."""
    show_map()
    try:
        seat_no = int(input("Enter seat number to book (1-14): "))
        
        # Comparison and Logical Operations for validation
        if seat_no < 1 or seat_no > 14:
            print("Invalid seat number. Please choose between 1 and 14.")
        elif seats[seat_no] == "Booked":
            print("Seat is already taken.")
        else:
            # String Operations: cleaning and formatting
            full_name = input("Enter passenger's full name: ").strip().title()
            phone_number = input("Enter phone number: ").strip()
            national_id = input("Enter National ID: ").strip()
            
            # Format validation
            if not (phone_number.isdigit() and national_id.isdigit()):
                print("Error: Phone number and National ID must contain only numbers.")
                return

            # Update list and dictionary
            seats[seat_no] = "Booked"
            passengers[seat_no] = {
                "name": full_name,
                "phone": phone_number,
                "id": national_id
            }
            
            # Output using f-strings
            print("\n*** TICKET RECEIPT ***")
            print(f"Shuttle: {shuttle_plate}")
            print(f"Route: {route}")
            print(f"Passenger: {full_name}")
            print(f"Seat No: {seat_no}")
            print(f"Fare: {ticket_fare} KES")
            print("**********************")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
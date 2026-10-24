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
        
        # Use Modulo to break the line after every 3 seats for a shuttle layout
        if seat % 3 == 0:
            print()
    print("\n-------------------")
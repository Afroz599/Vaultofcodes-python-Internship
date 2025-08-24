import random as rd
# Initial pet attributes
happiness = 50
hunger = 50
# Feed the pet
def feed():
    global happiness, hunger
    print(f"\nYou are feeding {name}")
    # decrease hunger, small random effect
    decrease = rd.randint(10, 20)
    hunger = max(0, hunger - decrease)
    # happiness decreases slightly
    happiness = max(0, happiness - rd.randint(1, 5))
    print(f"{name}'s happiness is {happiness}%")
    print(f"{name}'s hunger level is {hunger}%")
# Play with the pet
def play():
    global happiness, hunger
    print(f"\nYou are playing with {name}")
    # increase happiness, with random boost
    increase = rd.randint(10, 20)
    happiness = min(100, happiness + increase)
    # hunger increases slightly
    hunger = min(100, hunger + rd.randint(5, 10))
    print(f"{name}'s happiness is {happiness}%")
    print(f"{name}'s hunger level is {hunger}%")
# Check status
def status():
    print(f"\n{name}'s current status:")
    print(f"Happiness: {happiness}%")
    print(f"Hunger: {hunger}%")
# Quit game
def quit_game():
    print(f"\nThanks for playing with {name}! Goodbye!")
    return False  # signal to stop the loop
# Time passes (after every few actions)
def time_passes():
    global happiness, hunger
    hunger = min(100, hunger + rd.randint(1, 5))
    happiness = max(0, happiness - rd.randint(1, 5))
# Check if game over
def check_game_over():
    if hunger >= 100:
        print(f"\nOh no! {name} got too hungry! Game Over.")
        return False
    elif happiness <= 0:
        print(f"\nOh no! {name} became too sad! Game Over.")
        return False
    return True
# Menu dictionary
choose = {
    'feed': feed,
    'play': play,
    'status': status,
    'quit': quit_game
}
# Start game
print("|-----------------------|")
print(" VIRTUAL PET SIMULATOR")
print("|-----------------------|")
name = input("Name your pet: ")
actions = 0
running = True
while running:
    print("\nEnter Your Choice: Feed | Play | Status | Quit")
    choice = input(">> ").lower()
    if choice in choose:
        # quit_game returns False to stop loop
        result = choose[choice]()
        if result is False:
            break
        actions += 1
        # Every 3 actions, time passes
        if actions % 3 == 0:
            time_passes()
        # Check if pet is too hungry/sad
        running = check_game_over()
    else:
        print("Wrong choice. Please try again.")

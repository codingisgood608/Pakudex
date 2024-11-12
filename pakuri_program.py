from pakudex import Pakudex

def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity <= 0:
                print("Please enter a valid size.")
            else:
                break
        except:
            print("Please enter a valid size.")

    pakudex = Pakudex(capacity)
    print(f"The Pakudex can hold {capacity} species of Pakuri.")

    while True:
        print("\nPakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit")

        choice = input("\nWhat would you like to do? ")

        if choice == '1':
            list_pakuri(pakudex)
        elif choice == '2':
            show_pakuri(pakudex)
        elif choice == '3':
            add_pakuri(pakudex)
        elif choice == '4':
            evolve_pakuri(pakudex)
        elif choice == '5':
            sort_pakuri(pakudex)
        elif choice == '6':
            print("Thanks for using Pakudex! Bye!")
            break
        else:
            print("Unrecognized menu selection!")
            continue

def list_pakuri(pakudex):
    size = pakudex.get_size()
    if size == 0:
        print("No Pakuri in Pakudex yet!")
    else:
        print("Pakuri In Pakudex:")
        for i, species in enumerate(pakudex.get_species_array(), 1):
            print(f"{i}. {species}")

def show_pakuri(pakudex):
    species = input("Enter the name of the species to display: ")
    stats = pakudex.get_stats(species)
    if stats:
        print(f"\nSpecies: {species}")
        print(f"Attack: {stats[0]}")
        print(f"Defense: {stats[1]}")
        print(f"Speed: {stats[2]}")
    else:
        print(f"Error: No such Pakuri!")

def add_pakuri(pakudex):
    if pakudex.get_size() >= pakudex.get_capacity():
        print("Error: Pakudex is full!")
        return
    else:
        species = input("Enter the name of the species to add: ")
        if pakudex.add_pakuri(species):
            print(f"Pakuri species {species} successfully added!")
        else:
            print("Error: Pakudex already contains this species!")

def evolve_pakuri(pakudex):
    species = input("Enter the name of the species to evolve: ")
    if pakudex.evolve_species(species):
        print(f"{species} has evolved!")
    else:
        print(f"Error: No such Pakuri!")

def sort_pakuri(pakudex):
    pakudex.sort_pakuri()
    print("Pakuri have been sorted!")

if __name__ == "__main__":
    main()
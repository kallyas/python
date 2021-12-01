# create a touple that grabs two items
import random


def names_touple():
    names = ('John', 'Paul', 'George', 'Ringo', 'Ben', 'David')
    # print two random names from the touple using random module
    print(random.choice(names), random.choice(names))
    

# create a 6-D list that prints "Six" 6-D lists
def six_d_list():
    six_d_list = [['Six' for i in range(2)] for i in range(6)]
    print(six_d_list * 6)

# create a while loop that prints up to 20 but skips 15
def skip_15():
    i = 1
    while i < 20:
        if i == 15:
            i += 1
        print(i)
        i += 1

# create a dictionary called Phonebook that prints out names and phone numbers
def phonebook():
    phonebook = {'John': '555-5555', 'Paul': '555-5555', 'George': '555-5555', 'Ringo': '555-5555', 'Ben': '555-5555', 'David': '555-5555'}
    # print a random name and phone number from the dictionary using nested for loops
    for name in phonebook:
        print(name, phonebook[name])

# main menu
def menu():
    print("""
    Todays Assignment
    1. Names touple
    2. Six-D list
    3. Skip 15
    4. Phonebook
    5. Exit
    """)

# main function
def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            names_touple()
        elif choice == '2':
            six_d_list()
        elif choice == '3':
            skip_15()
        elif choice == '4':
            phonebook()
        elif choice == '5':
            print("Goodbye")
            break
        else:
            print("Invalid choice")


main()

#ques1
'''import random

def number_guessing_game():
    secret_number = random.randint(1, 10)
    guess = None

    while guess != secret_number:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed it right.") '''

#ques 2

'''def count_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print(f"Vowels: {vowel_count}, Consonants: {consonant_count}") '''

#ques 3

''' def add_album(library, album_info):
    artist, title, year, songs = album_info
    library[title] = (artist, year, songs)
    return library

def create_playlist(library, selections):
    return [song for album, song in selections if song in library.get(album, (None, None, []))[2]]

def add_song_to_album(library, title, new_song):
    artist, year, songs = library.get(title, (None, None, []))
    if new_song not in songs:
        songs.append(new_song)
    library[title] = (artist, year, songs)
    return library

def remove_song_from_playlist(playlist, song):
    if song in playlist:
        playlist.remove(song)
    return playlist

def music_library_menu():
    library = {}
    playlist = []

    while True:
        print("\n--- Music Library Menu ---")
        print("1. Add Album")
        print("2. Create Playlist")
        print("3. Add Song to Album")
        print("4. Remove Song from Playlist")
        print("5. View Library and Playlist")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            artist = input("Artist name: ")
            title = input("Album title: ")
            year = int(input("Release year: "))
            songs = input("Enter songs (comma-separated): ").split(",")
            album_info = (artist, title, year, [s.strip() for s in songs])
            add_album(library, album_info)
            print("Album added!")

        elif choice == '2':
            selections = []
            while True:
                album = input("Album name (or 'done'): ")
                if album == 'done':
                    break
                song = input("Song name: ")
                selections.append((album, song))
            playlist = create_playlist(library, selections)
            print("Playlist created:", playlist)

        elif choice == '3':
            title = input("Album title: ")
            new_song = input("New song: ")
            add_song_to_album(library, title, new_song)
            print("Song added!")

        elif choice == '4':
            song = input("Song to remove from playlist: ")
            remove_song_from_playlist(playlist, song)
            print("Song removed.")

        elif choice == '5':
            print("Library:", library)
            print("Playlist:", playlist)

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Try again.") '''

#ques5

''' def convert_to_integer():
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        print("You entered the number:", number)
    except ValueError:
        print("That was not a valid number.")'''

#ques6

''' def get_valid_integer():
    while True:
        user_input = input("Enter an integer: ")
        try:
            number = int(user_input)
            print("You entered:", number)
            break
        except ValueError:
            print("Invalid input. Try again.")'''
#ques 7
'''class BankAccount:
    def __init__(self, acc_no, holder_name, balance=0):
        self.__acc_no = acc_no
        self.__holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def display_info(self):
        print(f"Account: {self.__acc_no}, Name: {self.__holder_name}, Balance: ₹{self.__balance}")

# Example usage
account = BankAccount("12345", "John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.display_info()'''

#ques8
'''class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def display_info(self):
        print(f"ID: {self.__emp_id}, Name: {self.__name}, Salary: ₹{self.__salary}")

    def give_hike(self, percent):
        self.__salary += self.__salary * (percent / 100)

# Example usage
emp = Employee("E001", "Alice", 50000)
emp.display_info()
emp.give_hike(10)
emp.display_info()'''
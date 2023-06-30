import time #import time module
import random #import random module
welcome_message1 = """

██████╗░░█████╗░░██████╗███████╗░█████╗░░██████╗
╚════██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
░█████╔╝██║░░██║╚█████╗░█████╗░░██║░░╚═╝╚█████╗░
░╚═══██╗██║░░██║░╚═══██╗██╔══╝░░██║░░██╗░╚═══██╗
██████╔╝╚█████╔╝██████╔╝███████╗╚█████╔╝██████╔╝
╚═════╝░░╚════╝░╚═════╝░╚══════╝░╚════╝░╚═════╝░
"""

welcome_message2 = """Welcome to the 30 Seconds game!

Instructions:
1. Roll the dice to see where you land on the board
2. Depending on the colour you landed on, you will have 30 seconds to:
   - Yellow card: Name as many easy items as possible
   - Blue card: Name as many easy to medium items as possible
   - Red card: Name as many medium to hard items as possible
3. To quit the game, type 'quit' at any time

Note:
- Please make sure that the "red_card.txt" file is saved in the same folder as this program.
- You can download the attached image of the game board in the repository directory, print it.
- You can choose your own household objects to represent each team and play.
- The timer function is set to 5 seconds for reduced waiting time and testing purposes, edit to 30 to play.
Let's get started!"""

print("\nLoading Game...")
time.sleep(1)
print("\n", welcome_message1)
time.sleep(1)
print("\n", welcome_message2)
time.sleep(5)

def roll_dice(): #create dice roll function
    print("\nRolling...")
    time.sleep(1)
    print("\n")
    print("You Rolled:", (random.randint(0, 2))) #range 0-2 , as in the game of 30 seconds, using random.randint()
    print("\n")
    return

def blue_card(): #create blue card fuction, using dictionary with k:v pairs
    cards = {
    "card 1" : ["Brad Pitt", "Linkdn", "Argentina", "Liverpool FC", "CNN"],
    "card 2" : ["Ronaldo", "Facebook", "Brazil", "Arsenal", "Sky News"],
    "card 3" : ["Messi", "Twitter", "South Africa", "Chelsea FC", "ESPN"],
    "card 4" : ["Serena Williams", "Tik Tok", "Egypt", "Al Ahly FC", "BBC"],
    "card 5" : ["Demi Moore", "Summer", "Beach", "Surfing", "Iphone"],
    "card 6" : ["Usher", "Diamonds", "Lord of the Rings", "Tennis", "Sun City"],
    "card 7" : ["Nike", "Baseball", "Ferrari", "Himalayas", "Kanye West"],
    "card 8" : ["Coca Cola", "Microwave", "Louis Vuitton", "Fruits", "Taiwan"],
    "card 9" : ["Puff Daddy", "Rocky Balboa", "George Bush", "Jumanji", "Teapot"],
    "card 10" : ["We didnt start the fire", "Great wall of china", "Polka", "Rachet", "Pindrop"],
    "card 11" : ["Aasiyah", "St Josephs School", "Art", "Tennis", "Minky"],
    "card 12" : ["Nathma", "Psycologist", "Asian", "Unisa", "Regaeton"],
    "card 13" : ["Rethar", "Handsome", "Hot", "Software Developer", "Blonde Hair"]
    }
    card_number = random.choice(list(cards.keys())) #using random.choice to choose a card and return a list
    elements = cards[card_number]
    for x in elements: #loop through elements in list and print in new lines
        print("\n", x, "\n")

def yellow_card(): #create yellow card function, using lists this time
    card_list = ["Korea", "Japan", "Sky Sports", "LFCTV", "Hello Kitty", "Bitcoin",
    "Ripple", "Teal", "Github", "Instagram", "Mxit", "Microsoft", "Meta", "USA",
    "Tennis", "FIFA", "Nelson Mandela", "Ghandi", "Malcom X", "Earth", "Tesla",
    "Venus", "Mars", "Oreos", "Milkshake", "Banana", "Ice Cream", "Waffles",
    "Matrix", "Marvel", "Superman", "Batman", "Thor", "Last of us", "Survivor",
    "Lethal Weapon", "Castle Lager", "Yeezy Slides", "Crocs", "Adidas", "Einstein",
    "Real Betis", "Galatasary", "Kim Kardashian", "Pepsi", "Lays", "Cadbury", "Teal",
    "Keanu Reeves", "Python", "Django", "AI", "Charlotte", "Bon Jovi", "Mondelez"]
    card = random.sample(card_list, k=5) #using random, choosing 5 elements
    for x in card: #loop through list and print in new lines
        print("\n", x, "\n")

def red_card(): #create red card function, this time readinf from file using with open which auto closes
    with open("red_card.txt", "r") as file:
        card_data = file.read().split(",") #read file and split by comma
        card_list = [] #create empty list
        for x in card_data: #loop through and append to list ,stripping whitespaces
            card_list.append(x.strip())
        elements = random.sample(card_list, 5) #using random to choose 5 elements
        for x in elements: #loop through list and print in new lines
            print("\n", x, "\n")

def timer(): #create timer function, countdown timer from 30 using time.sleep and end to decrement by one second on same line
    for i in range(30, 0, -1):
        print(str(i) + "seconds left", end="\r")
        time.sleep(1)
    print("", end="\r")



def program(): #main program
    while True: #prompt user for input
        print("\nType 'r' - to roll the dice")
        print("Type 'y' - for the yellow card")
        print("Type 'b' - for the blue card")
        print("Type 'rc' for the red card")
        print("Type 'quit' to exit the game\n")
        option_input = input(":")

        if option_input == 'r': #call roll_dice function
            roll_dice()

        elif option_input == 'b': #call blue_card function and timer
            time.sleep(1)
            blue_card()
            timer()
            print("***Times Up!***", end="")
            print("\n")

        elif option_input == 'y': #call yellow_card function and timer
            time.sleep(1)
            yellow_card()
            timer()
            print("***Times Up!***", end="")
            print("\n")

        elif option_input == 'rc': #call red_card function and timer
            time.sleep(1)
            red_card()
            timer()
            print("***Times Up!***", end="")
            print("\n")

        elif option_input == 'quit': #quit program using break, Goodbye note/request feedback/Author information
            time.sleep(1)
            print("""
Thanks for playing the 30 seconds game! I hope you enjoyed it.
If you have any feedback or suggestions for improvement, please let me know.
Thank you again for your support!
Best regards, Rethar Osman Abdullah
https://github.com/Rethar-yt""")
            break

        else:
            time.sleep(1)
            print("\nInvalid input, try again") #Error catching prompting user to try again

program() #call main program to run 30 seconds game

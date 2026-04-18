import time

def main():
    print("Welcome to the Word Toolkit!")
    print("")
    time.sleep(0.2)
    print("What string would you like to analyze today? ")
    userString = input('Enter: ')
    time.sleep(0.2)
    print("")
    print("What would you like to know?")
    print("1. Vowel Counter")
    print("2. Character Counter")
    print("3. Word Counter")
    print("4. Speaking/Typing Times")
    print("5. Commonality Checker")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                vowelCount(userString)
            elif choice == 2:
                charCount(userString)
            elif choice == 3:
                wordCounter(userString)
            elif choice == 4:
                readTypeTime(userString)
            elif choice == 5:
                commonCheck(userString)
            else:
                print("Please enter a valid option! Thank you!")
        except ValueError:
            print("Please enter the number that corresponds with the choice! Thank you!")

def wordCounter(userString):
    def wordCounter(userString):
    numWords = len(userString.split())
    words = userString.split()
    print("")
    print("Thinking...")
    time.sleep(0.25)
    print("")
    print(f"There are {numWords} words in that sentence!")
    print(f"The words are: {words}!")
    print("")

def readTypeTime(userString):
    print("readTypeTime stub. I read better than I type.")
    return 1998

def charCount(userString):
    print("charCount stub, reporting for duty!")
    return 99

def vowelCount(userString):
    print("vowelCount stub. University of Arizona.")
    return 8642

def commonCheck(userString):
    print("commonCheck stub? No, this is Patrick.")
    return "Kanye West"


main()

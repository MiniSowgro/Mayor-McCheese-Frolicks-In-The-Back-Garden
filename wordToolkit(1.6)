import time
userString = ""
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
charNum = 0

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
    print("6. Analyze a Different String")
    print("7. Exit Program")
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
            elif choice == 6:
                userString = newString(userString)
            elif choice == 7:
                print("Thank you for using the Word Toolkit!")
                exit()
            else:
                print("Please enter a valid option! Thank you!")
        except ValueError:
            print("Please enter the number that corresponds with the choice! Thank you!")

def wordCounter(userString):
    numWords = len(userString.split())
    words = userString.split()
    print("")
    print("Thinking...")
    time.sleep(0.25)
    print("")
    print(f"There are {numWords} word(s) in that sentence!")
    print(f"The word(s) are: {words}!")
    print("")

def readTypeTime(userString):
    numWords = len(userString.split())
    speakTimeMins = numWords / 150
    typeTimeMins = numWords / 40
    speakTimeSecs = numWords / 150 * 60
    typeTimeSecs = numWords / 40 * 60

    print("")
    print("Thinking...")
    time.sleep(0.25)
    print("")
    print(
        f"Your sentence will take {speakTimeMins} minutes to speak, or {speakTimeSecs} seconds (Based on the average speaking time of 150 words per minute)!")
    print(
        f"Your sentence will take {typeTimeMins} minutes to type, or {typeTimeSecs} (Based on the average typing time of 50 words per minute)!")
    print("")

def charCount(userString):
    charNum = len(userString)
    print("")
    print("Thinking...")
    time.sleep(0.25)
    print("")
    print(f"There seem to be {charNum} characters in that string!")


def vowelCount(userString):
    vowelNum = 0
    for letter in userString:
        if letter in vowel:
            vowelNum += 1
    print("")
    print("Thinking...")
    time.sleep(0.25)
    print('')
    print(f"There are {vowelNum} vowels in that sentence!")



def commonCheck(userString):
    import pprint
    from collections import Counter
    common = Counter(userString)
    print("")
    print("Thinking...")
    time.sleep(0.25)
    print("")

    print("The amount of times each letter appears in the string are as follows: ")

    pprint.pprint(dict(common), width=1)

def newString(userString):
    time.sleep(0.25)
    print("")
    newUserString = input("Enter your new string: ")
    return newUserString


main()

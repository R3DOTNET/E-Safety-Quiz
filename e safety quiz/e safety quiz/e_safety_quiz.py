import time
import sys

print("Welcome to the E-Safety quiz! Type START to get started!")
start = input().upper()

lives = 3
incorrect = 0

if start == "START":
    print("Welcome! You have 3 lives to start. Answer wrong and a life will be deducted. Once your live reaches 0 you will have to relaunch the program.")
elif start == "EXIT" or "STOP" or "END" or "BACK":
    sys.exit(0)

print("First question!")
time.sleep(1.7)
print("You get a browser window you cant exit which lists a number claiming your computer has a virus. What do you do?")
time.sleep(1.7)
print("A. Call the number")
time.sleep(1.7)
print("B. Dont call the number and restart your device")
time.sleep(1.7)
print("C. Overthrow the government")
ua1 = input("Please input A, B or C: ").upper()

if ua1 == "B":
    print("Correct! Next Question.")
    print(lives)
else:
    print("WOMP WOMP. No.")
    lives = lives - 1
    incorrect = incorrect + 1
    print(f"Lives: {lives}")

time.sleep(2.2)

print("Question 2.")
time.sleep(1.7)
print("If you get a call that claims to be your bank and starts asking for personal details, what do you do?")
time.sleep(1.7)
print("A. Give them everything")
time.sleep(1.7)
print("B. Hang up")
time.sleep(1.7)
print("C. Hold their family hostage until they pay ransom")
ua2 = input("Please input A, B or C: ").upper()

if ua2 == "B":
    print("Correct! Next Question.")
    print(lives)
else:
    print("WOMP WOMP. No.")
    lives = lives - 1
    incorrect = incorrect + 1
    print(f"Lives: {lives}")

time.sleep(2.2)

print("Question 3.")
time.sleep(1.7)
print("A Nigerian prince contacts you via email saying he wants to share his wealth for a small fee. What do you do")
time.sleep(1.7)
print("A. Give him everything")
time.sleep(1.7)
print("B. Delete the email")
time.sleep(1.7)
print("C. Nuke his palace")
ua3 = input("Please input A, B or C: ").upper()

if ua3 == "B":
    print("Correct! Next Question.")
    print(lives)
else:
    print("WOMP WOMP. No.")
    lives = lives - 1
    incorrect = incorrect + 1
    print(f"Lives: {lives}")
    if lives == 0:
        print("YOU LOSE, LOSER")
        sys.exit(0)

time.sleep(2.2)

print("Question 4.")
time.sleep(1.7)
print("A man claims to be captured and is reaching out by email, asking you to pay his ransom, promising a reward. You know the drill.")
time.sleep(1.7)
print("A. Give him everything")
time.sleep(1.7)
print("B. Delete the email")
time.sleep(1.7)
print("C. Romance his wife")
ua4 = input("Please input A, B or C: ").upper()

if ua4 == "B":
    print("Correct! Next Question.")
    print(lives)
else:
    print("WOMP WOMP. No.")
    lives = lives - 1
    incorrect = incorrect + 1
    print(f"Lives: {lives}")
    if lives == 0:
        print("YOU LOSE, LOSER")
        sys.exit(0)

time.sleep(2.2)

print("Question 5.")
time.sleep(1.7)
print("Steven Hawking claims to have risen from the dead and is messaging you on instagram asking for gas money. WHAT. Do you do?")
time.sleep(1.7)
print("A. Give him everything")
time.sleep(1.7)
print("B. Block and report")
time.sleep(1.7)
print("C. Throw that man out his wheelchair while screaming obcenities")
ua5 = input("Please input A, B or C: ").upper()

if ua5 == "B":
    print("Correct! Next Question.")
    print(lives)
else:
    print("WOMP WOMP. No.")
    lives = lives - 1
    incorrect = incorrect + 1
    print(f"Lives: {lives}")
    if lives == 0:
        print("YOU LOSE, LOSER")
        sys.exit(0)

time.sleep(2.2)

print("Question 6.")
time.sleep(1.7)
print("Ariana Grande says she wants to hook up for netflix and chill, reaching out on an alternate account on snapchat but needs gas money. WHAT DO YOU DO?")
time.sleep(1.7)
print("A. OH MY GOD TAKE MY MONEY ARIANA EEEEEEEE")
time.sleep(1.7)
print("B. Block and report")
time.sleep(1.7)
print("C. Say BEGONE THOT")
ua6 = input("Please input A, B or C: ").upper()

if ua6 == "B":
    print("Correct! Next Question.")
    print(lives)
else:
    print("WOMP WOMP. No.")
    lives = lives - 1
    incorrect = incorrect + 1
    print(f"Lives: {lives}")
    if lives == 0:
        print("YOU LOSE, LOSER")
        sys.exit(0)

time.sleep(2.2)

print("Question 7.")
time.sleep(1.7)
print("A Bhuddist monk texts your SMS saying he needs money to give to his god and promises eternal rewards. WHAT do YOU do?")
time.sleep(1.7)
print("A. Send him your credit card")
time.sleep(1.7)
print("B. Block the number")
time.sleep(1.7)
print("C. Deface the nearest temple (Dont do this)")
ua7 = input("Please input A, B or C: ").upper()

if ua7 == "B":
    print("Correct! Next Question.")
    print(lives)
else:
    print("WOMP WOMP. No.")
    lives = lives - 1
    incorrect = incorrect + 1
    print(f"Lives: {lives}")
    if lives == 0:
        print("YOU LOSE, LOSER")
        sys.exit(0)

print("Well done! You finished the quiz! Lets see how you did.")
time.sleep(1.5)
print(f"You got {incorrect} wrong")
time.sleep(1.5)
print(f"You ended on {lives} lives")
time.sleep(1.5)
print("And you didnt lose! Well done!")
time.sleep(1.5)
print("I'm afraid thats the end of the quiz. BYE!!!")
time.sleep(1.7)
sys.exit(0)
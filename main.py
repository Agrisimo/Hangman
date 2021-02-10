import string
import random
import time

alphabet = string.ascii_uppercase
exit_time = 2
guessed_list = []

# Open file, make a list and chose at random one word as "word"
with open("words.txt", "r") as doc:
    word_list = list(doc.read().split())
    word = random.choice(word_list).upper()

# Length of the correct word

length = len(word)
display_list = list("_" * length)
guess_count = length + 5
correct_guesses = 0

# Opening text
print("""This is a typical "Hangman" guess a word game!""")
print(f"There are {length} letters in the word!")
print(f"You have {guess_count} guesses available!")


print(word)


while guess_count != 0:
    display = " ".join(display_list)
    guess = input(f"""
Guess a word or letter!
{display}
:""").upper()
    if guess == word:
        print(f"""Congrats! You guessed right, the word was "{word.upper()}"!""")
        print(f"Game will terminate in {exit_time} second!")
        time.sleep(exit_time)
        quit()

# Invalid inputs

    if len(guess) > 1 and len(guess) < len(word):
        print("Please enter only one letter!")
        continue

    if len(guess) > len(word):
        print(f"Your guess has {len(guess)} letters!")
        print(f"There are only {length} letters in the word!")
        continue

    if len(guess) == 0:
        print("Please enter a letter or the word!")
        continue

    if guess not in alphabet and len(guess) == 1:
        print("Only english alphabet letters are accepted!")
        continue


# Wrong word guess or no letter in the word

    if len(guess) == len(word) and guess != word:
        guess_count -= 1
        print("You tried to guess the word.")
        print(f"The {guess} is not the correct word!")
        print(f"You have {guess_count} guesses left!")
        continue

    if guess not in word:
        if guess not in guessed_list:
            guess_count -= 1
            guessed_list.append(guess)
            print(f"Letter {guess} is not in the word.")
            print(f"You have {guess_count} guesses left!")
            continue
        else:
            print(f"You already tried letter {guess}, it`s  not in the word try something else!")
            continue

    if guess in word:
        if guess in guessed_list:
            print(f"""You already tried letter "{guess}", it`s on the board!""")
            continue

        if word.count(guess) > 1:
            guess_count -= 1
            guessed_list.append(guess)
            correct_guesses += word.count(guess)
            print(f"""Good job! Letter {guess} is in the word!
                        """)
            print(f"You have {guess_count} guesses left!")
            try:
                ind = word.index(guess)
                display_list[ind] = guess
                ind2 = word.index(guess, ind+1)
                display_list[ind2] = guess
                ind3 = word.index(guess, ind2+1)
                display_list[ind3] = guess
            except ValueError:
                ind = word.index(guess)
                display_list[ind] = guess
                ind2 = word.index(guess, ind + 1)
                display_list[ind2] = guess

        else:
            guess_count -= 1
            guessed_list.append(guess)
            correct_guesses += 1
            print(f"""Good job! Letter {guess} is in the word!
            """)
            print(f"You have {guess_count} guesses left!")
            ind = word.index(guess)
            display_list[ind] = guess

    if correct_guesses == len(word):
        print(f"""Congrats! You guessed right, the word was "{word.upper()}"!""")
        print(f"Game will terminate in {exit_time} second!")
        time.sleep(exit_time)
        quit()


print("""AKA - you ran out of guesses, you are hanged!""")
print(f"The correct word was {word}!")
print(f"The program will terminate in {exit_time} seconds!")
time.sleep(exit_time)
quit()

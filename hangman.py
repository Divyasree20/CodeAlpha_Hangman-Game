import random
import time
import threading

# Custom ASCII Art
welcome_art = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
🎮 Welcome to Hangman!
"""

win_art = """
🎉🎉🎉 CONGRATULATIONS! 🎉🎉🎉
  You guessed the word! 🏆
"""

lose_art = """
💀💀 GAME OVER! 💀💀
  The word was '{}' 😞
"""

# Hangman stages (ASCII Art)
hangman_stages = [
    """
       ------
       |    |
       |    
       |   
       |   
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   
       |   
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |   
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |   
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

# Dictionary of words and hints
word_hints = {
    "python": "A popular programming language 🐍",
    "developer": "Someone who writes code 💻",
    "hangman": "A classic word-guessing game 🎮",
    "programming": "The process of writing software 🏗️",
    "technology": "The application of scientific knowledge ⚙️",
    "computer": "An electronic device for processing data 🖥️",
    "algorithm": "A set of steps to solve a problem 🔢"
}

# Function to pick a random word and its hint
def get_random_word():
    word = random.choice(list(word_hints.keys()))
    hint = word_hints[word]
    return word, hint

# Function to display the word with guessed letters
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Function to get input with a timer (10 seconds per turn)
def input_with_timer(prompt, timeout):
    user_input = [None]
    
    def timer():
        time.sleep(timeout)
        if user_input[0] is None:
            print("\n⏳ Time's up! You missed your turn.")
    
    t = threading.Thread(target=timer)
    t.start()
    user_input[0] = input(prompt).lower()
    return user_input[0]

# Main Hangman game function
def hangman():
    print(welcome_art)  # Show welcome art
    
    mode = input("Do you want to play Single-player or Multiplayer? (single/multi): ").lower()
    if mode == "multi":
        print("\n👥 Multiplayer Mode: One player enters a word, the other guesses!")
    
    while True:
        if mode == "multi":
            word = input("\nPlayer 1, enter a word for Player 2 to guess: ").lower()
            hint = input("Enter a hint for this word: ")
            print("\n" * 50)  # Clears screen for Player 2
        else:
            word, hint = get_random_word()
        
        guessed_letters = set()
        attempts = 6
        
        print("\n💡 Hint:", hint)
        print(hangman_stages[0])
        print(display_word(word, guessed_letters))
        
        while attempts > 0:
            print(f"\n⏳ You have 10 seconds to guess!")
            guess = input_with_timer("\nGuess a letter: ", 10)
            
            if not guess:  # If time runs out
                attempts -= 1
                print(f"❌ Missed turn! {attempts} attempts left.")
            elif guess in guessed_letters:
                print("⚠️ You've already guessed that letter!")
                continue
            else:
                guessed_letters.add(guess)
                
                if guess in word:
                    print("✅ Good guess!")
                else:
                    attempts -= 1
                    print(f"❌ Wrong guess! {attempts} attempts left.")
            
            print(hangman_stages[6 - attempts])
            print(display_word(word, guessed_letters))
            
            if "_" not in display_word(word, guessed_letters):
                print(win_art)
                break
        else:
            print(lose_art.format(word))
        
        play_again = input("\n🔄 Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    hangman()


#NOTE:
#cd path to your folder
#python hangman.py

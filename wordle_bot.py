# Wordle bot

grey_letters = []
yellow_letters = []
green_letters = []

guess = "tales"
guessed_words = []

word_list = open('words.txt').readlines()

while(True):
    print(f"Wordle guess: {guess}")
    
    user_entry = input("Press N for next guess, E to enter your own guess, or Q to quit\n")

    if user_entry.lower() == "q":
        break
    if user_entry.lower() == "e":
        guess = input("Enter custom guess\n")
  
    guessed_words.append(guess)

    grey_letters += input("Enter grey letters\n")
    yellow_letters += input("Enter yellow letters\n")
    green_letters += input("Enter green letters\n")
   
    green_indices = {}
    for letter in green_letters:
        green_indices[letter] = guess.index(letter)
    
    yellow_indices = {}
    for letter in yellow_letters:
        yellow_indices[letter] = guess.index(letter)

    print(green_indices)
    print("Grey letters: " + str(grey_letters)) 
    print("Yellow letters: " + str(yellow_letters)) 
    print("Green letters: " + str(green_letters)) 

    word_score_yellow = {}
    word_score_green = {}
     
    for word in word_list:
        word = word.rstrip('\n')
        if word in guessed_words:
            continue
        if any(str(grey) in word for grey in grey_letters):
            continue
        if any(word[green_indices[green]] != green for green in green_letters):
            continue
        if any(word[yellow_indices[yellow]] == yellow for yellow in yellow_letters):
            continue

        guess = word
    # New guess creation
    # IF there are green letters
    # if word_score_green:
    #     guess = max(word_score_green, key=lambda key: word_score_green[key])
    # elif word_score_yellow:
    #     guess = max(word_score_yellow, key=lambda key: word_score_yellow[key])
   







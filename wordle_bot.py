# Wordle bot
guess = "tales"
guessed_words = []
grey_letters = []

word_list = open('words.txt').readlines()

user_entry = input("Press any key to start with optimal guess or press E to enter your own guess, or Q to quit\n")

if user_entry.lower() == "e":
    guess = input("Enter custom guess\n")

extra_greys = input("If you want, enter any extra grey letters\n") 
grey_letters += extra_greys

green_data = [None, None, None, None, None]
yellow_data = []

smart_guess = False
temp_yellow_save = None
word_before_smart = ""

while(True):
    if guess in guessed_words:
        raise Exception("Failed to find new word")

    print(f"Wordle guess: {guess}")
    guessed_words.append(guess)

    letter_response = input("Enter result, x for grey, y for yellow, g for green. ex: gggxg\n")
    
    # process letter response
    temp_yellows = []
    temp_greens = []
    for ind, response in enumerate(letter_response):
        if response == 'x':
            grey_letters.append(guess[ind])
        elif response == 'y':
            yellow_data.append([ind, guess[ind]])
            temp_yellows.append(guess[ind])
        elif response == 'g':
            green_data[ind] = [ind, guess[ind]]
            temp_greens.append(guess[ind])
        elif response == 'q':
            exit()
        else:
            raise Exception("Game only excepts combination of x, y, g")
    
    if temp_yellow_save:
        temp_yellows = temp_yellow_save
        guess = word_before_smart
        temp_yellow_save = None
    
    grey_letters = list(set(grey_letters))
    
    for word in word_list:
        yellow_save = False
        word = word.rstrip('\n')
        if word in guessed_words:
            continue
        
        # TODO: Make a smarter guess when we only have yellows, instead of reorder guessing
        # if len(temp_yellows) > 2 and len(temp_greens) == 0 and not smart_guess:
        #     if any(possible_grey in grey_letters for possible_grey in word):
        #         continue
        #
        #     if len(set(word)) != len(word):
        #         continue
        #
        #     if any(letter in temp_yellows for letter in word):
        #         continue
        #     yellow_count = 0
        #     for letter in word:
        #         if letter in temp_yellows:
        #             yellow_count += 1
        #
        #     if yellow_count > 2:
        #         continue
        #     else:
        #         word_before_smart = guess
        #         guess = word
        #         temp_yellow_save = temp_yellows
        #         smart_guess = True
        #         break

        stripped_word = list(word)
        
        green_failed = False
        # green_letter = ind, letter
        for green_letter in green_data:
            if green_letter:
                if word[green_letter[0]] != green_letter[1]:
                    green_failed = True
                stripped_word[green_letter[0]] = None
        if green_failed:
            continue

        yellow_failed = False
        # green_letter = ind, letter
        # all yellow index history
        for yellow_letter in yellow_data:
            if yellow_letter:
                if yellow_letter[1] == word[yellow_letter[0]]:
                    yellow_failed = True
        if yellow_failed:
            continue
        # make sure yellows from last guess are in new guess
        if any(yellow not in stripped_word for yellow in temp_yellows):
            continue
        # remove the yellows
        for ind, letter in enumerate(stripped_word):
            if letter in temp_yellows:
                stripped_word[ind] = None
        # ignore words with greys in the remaining letters
        if any(possible_grey in grey_letters for possible_grey in stripped_word):
            continue
   
        guess = word
        break 






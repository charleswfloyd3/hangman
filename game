class Hangman:
    def invalid_gamemode(self):
        import random
        import mysql.connector
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="MyfirstDB33",
            database="testDB"
        )
        cursor = connection.cursor()
        print("\nChoose your GAMEMODE\n\n[EASY/MEDIUM/HARD/ADVANCED]\n")
        mode = input("Enter: ")
        with open("hangman_words.txt") as word_file:
            words = word_file.readlines()
        word = random.choice(words)
        while True:
            if mode == "easy":
                number_of_tries = len(word) + 5
                break
            elif mode == "medium":
                number_of_tries = len(word) + 2
                break
            elif mode == "hard":
                number_of_tries = len(word) - 1
                break
            elif mode == "advanced":
                number_of_tries = 1
                break
            else:
                print("Please enter a valid gamemode...")
                self.invalid_gamemode()
        indexes = []
        blank_word = ("_ " * (len(word) - 1))
        updated_blank_word = blank_word.split(" ")
        updated_blank_word.pop(-1)
        word_in_list = word.split(" ")
        print("You have " + str(number_of_tries) + " guesses left")
        print(blank_word)
        guesses = 0
        guessed_letters = []
        listOfLetters = ["a", "b", "c", "d", "e", "f", "g", 'h', "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                         "t", "u", "v", "w", "x", "y", "z"]
        while True:
            indexes.clear()
            guessed_letter = input("Guess a letter: ")
            if guessed_letter in guessed_letters:
                print(f"\nYou already tried {guessed_letter.upper()}, please try a different letter.\n")
                print(" ".join(updated_blank_word))
            elif len(guessed_letter) > 1:
                print("\nPlease only enter one letter at a time.\n")
                print(" ".join(updated_blank_word))
            elif guessed_letter not in listOfLetters:
                print("\nPlease only enter letters.\n")
                print(" ".join(updated_blank_word))
            else:
                guesses += 1
                guessed_letters.append(guessed_letter)
                if guessed_letter in word:
                    for i in range(len(word)):
                        if word[i] == guessed_letter:
                            indexes.append(i)
                    for i in indexes:
                        updated_blank_word[i] = guessed_letter

                        print("You got one!\n")
                    print(" ".join(updated_blank_word))
                    if "_" not in "".join(updated_blank_word):
                        table = str(len(word) - 1) + "letter"
                        cursor.execute(f"SELECT * from {table}")
                        row = (cursor.fetchone())
                        old_record = row[0]
                        new_record = guesses
                        if new_record < old_record or old_record == 0:
                            sql = (f"UPDATE {table} SET numberOfGuesses = %s where numberOfGuesses = %s")
                            val = (new_record, old_record)
                            cursor.execute(sql, val)
                            print(f"\nNEW HIGH SCORE for {table} words: {guesses} guesses.\nGood Job!")
                            connection.commit()
                            playagain = input("\nDo you want to play again?: ")
                            if playagain == "yes":
                                self.playgame()
                            else:
                                break

                        else:
                            table = str(len(word)) + "letters"
                            print("\nYou guessed it. The word is " + word + ".\nYou Win!")
                            print("It took you " + str(guesses) + " tries")
                            print(
                                f"You didn't beat you old record of {old_record} for {table} words. Better luck next time")
                            playagain = input("\nDo you want to play again?: ")
                            if playagain == "yes":
                                self.playgame()
                            else:
                                break
                else:
                    number_of_tries -= 1
                    if number_of_tries == 0:
                        print("\nYou ranout of guesses")
                        print("The word was " + word.upper())
                        print("GAME OVER")
                        playagain = input("Do you want to play again?: ")
                        if playagain == "yes":
                            self.playgame()
                        else:
                            break
                    else:
                        print("\nOops, the letter " + guessed_letter + " is not in the word. Try again")
                        print("You have " + str(number_of_tries) + " guesses left\n")
                        print(" ".join(updated_blank_word))
    def playgame(self):
        import random
        import mysql.connector
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="MyfirstDB33",
            database="testDB"
        )
        cursor = connection.cursor()
        print("Welcome to Hangman\n")
        seerecords = input("Enter yes if you want to see all records: ")
        if seerecords == 'yes':
            print("")
            tables = []
            for i in range(3, 8):
                tables.append(f"{str(i)}letter")
            for table in tables:
                cursor.execute(f"SELECT * FROM {table}")
                record = cursor.fetchone()[0]
                print(f"{str(record)} is the record for {table} words.")
            connection.commit()
        deleteallrecords = input("\nDo you want to delete all records?: ")
        if deleteallrecords == "yes":
            confirm = input("Are you sure?: ")
            if confirm == "yes":
                print("\nLoading...")
                tables = []
                for i in range(3, 8):
                    tables.append(f"{str(i)}letter")
                for table in tables:
                    cursor.execute(f"TRUNCATE TABLE {table}")
                for table in tables:
                    cursor.execute(f"INSERT INTO {table} VALUES(0)")
                connection.commit()
                print("Records has been reset, have fun playing!")
        print("\nChoose your GAMEMODE\n\n[EASY/MEDIUM/HARD/ADVANCED]\n")
        mode = input("Enter: ")
        with open("hangman_words.txt") as word_file:
            words = word_file.readlines()
        word = random.choice(words)
        while True:
            if mode == "easy":
                number_of_tries = len(word) + 5
                break
            elif mode == "medium":
                number_of_tries = len(word) + 2
                break
            elif mode == "hard":
                number_of_tries = len(word)-1
                break
            elif mode == "advanced":
                number_of_tries = 1
                break
            else:
                print("\nPlease enter a valid gamemode...")
                self.invalid_gamemode()
        indexes = []
        blank_word = ("_ " * (len(word) - 1))
        updated_blank_word = blank_word.split(" ")
        updated_blank_word.pop(-1)
        word_in_list = word.split(" ")
        print("You have " + str(number_of_tries) + " guesses left")
        print(blank_word)
        guesses = 0
        guessed_letters = []
        listOfLetters = ["a", "b", "c", "d", "e", "f", "g", 'h', "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                         "t", "u", "v", "w", "x", "y", "z"]
        while True:
                indexes.clear()
                guessed_letter = input("Guess a letter: ")
                if guessed_letter in guessed_letters:
                    print(f"\nYou already tried {guessed_letter.upper()}, please try a different letter.\n")
                    print(" ".join(updated_blank_word))
                elif len(guessed_letter)>1:
                    print("\nPlease only enter one letter at a time.\n")
                    print(" ".join(updated_blank_word))
                elif guessed_letter not in listOfLetters:
                    print("\nPlease only enter letters.\n")
                    print(" ".join(updated_blank_word))
                else:
                    guesses += 1
                    guessed_letters.append(guessed_letter)
                    if guessed_letter in word:
                        for i in range(len(word)):
                            if word[i] == guessed_letter:
                                indexes.append(i)
                        for i in indexes:
                            updated_blank_word[i] = guessed_letter

                            print("You got one!\n")
                        print(" ".join(updated_blank_word))
                        if "_" not in "".join(updated_blank_word):
                            table = str(len(word)-1) + "letter"
                            cursor.execute(f"SELECT * from {table}")
                            row = (cursor.fetchone())
                            old_record = row[0]
                            new_record = guesses
                            if new_record < old_record or old_record==0:
                                sql = (f"UPDATE {table} SET numberOfGuesses = %s where numberOfGuesses = %s")
                                val = (new_record, old_record)
                                cursor.execute(sql,val)
                                print(f"\nNEW HIGH SCORE for {table} words: {guesses} guesses.\nGood Job!")
                                connection.commit()
                                playagain = input("\nDo you want to play again?: ")
                                if playagain == "yes":
                                    self.playgame()
                                else:
                                    break

                            else:
                                table = str(len(word)) + "letters"
                                print("\nYou guessed it. The word is " + word + ".\nYou Win!" )
                                print("It took you " + str(guesses) +" tries")
                                print(f"You didn't beat you old record of {old_record} for {table} words. Better luck next time")
                                playagain = input("\nDo you want to play again?: ")
                                if playagain == "yes":
                                    self.playgame()
                                else:
                                    break
                    else:
                        number_of_tries -=1
                        if number_of_tries == 0:
                            print("\nYou ranout of guesses")
                            print("The word was " + word.upper())
                            print("GAME OVER")
                            playagain = input("Do you want to play again?: ")
                            if playagain == "yes":
                                self.playgame()
                            else:
                                break
                        else:
                            print("\nOops, the letter " + guessed_letter + " is not in the word. Try again")
                            print("You have " + str(number_of_tries) + " guesses left\n")
                            print(" ".join(updated_blank_word))


h = Hangman()
h.playgame()

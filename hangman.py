from colorama import Fore
from words import word_list
import random
from stage import stages









def main():
    wrong = 0
    word = random.choice(word_list)
    board = ["_"] * len(word)
    remaining_letters = list(word)
    header()
    game(wrong, board, word, remaining_letters, stages)


def header():
    print(Fore.GREEN + '--------------------' + Fore.WHITE)
    print(Fore.MAGENTA + 'welcome to hangman' + Fore.WHITE)
    print(Fore.GREEN + '--------------------' + Fore.WHITE)






def game(wrong, board, word, remaining_letters, stages):
    win = False
    k = []


    while wrong < len(stages) - 1:
        print()
        print()
        print(board)
        print()
        print(Fore.GREEN + f'Used Letters: {k}' + Fore.WHITE)
        print()
        letter = input(Fore.BLUE + f'please choose your letter: ' + Fore.WHITE)
        if letter.isalpha() == True:
            if letter in k:
                print(Fore.RED + f'you already used the letter {letter}. Please try another one' + Fore.WHITE)
                continue
            if len(letter) == 1:
                if letter in remaining_letters:
                    if len(letter) == 1:
                        for ix, reml in enumerate(word):
                            if reml == letter:
                                letter_index = remaining_letters.index(letter)
                                board[letter_index] = letter
                                remaining_letters[letter_index] = '$'
                    k.append(letter)


            elif len(letter) != 1 and len(letter) != len(word):
                print(Fore.RED + 'you can only guess the word if you type all letters in the word as one !!!!' + Fore.WHITE)
                print(Fore.RED + 'Please try using jus one letter at a time' + Fore.WHITE)
                continue

            if len(letter) == len(word):
                m = []
                l = []
                for z in letter:
                    m.append(z)
                for zx in word:
                    l.append(zx)
                if m == l:
                    print()
                    print(Fore.LIGHTBLUE_EX + 'You win!!! Yuou Guessed the whole Word!!!' + Fore.WHITE)
                    Print()
                    print(Fore.BLUE + word.upper() + Fore.WHITE)
                    win = True
                    break
                else:
                    print('wrong')
                    continue
            else:
                wrong += 1
                print(''.join(board))
                e = wrong + 1
                print('\n'.join(stages[0:e]))

        else:
            print(Fore.MAGENTA + f"The {letter} is not a correct symbol!! please choose correct letter from the alphabet ! " + Fore.WHITE)
            continue
        if '_' not in board:
            print(Fore.BLUE + 'You win !!!!' + Fore.WHITE)
            print(''.join(board))
            win = True
            break
    if not win:

        print(Fore.RED + '\n'.join(stages[0:wrong]) + Fore.WHITE)
        print(Fore.YELLOW + 'Ha ha ha looser' + Fore.WHITE)
        print()
        print(Fore.RED + f'The word was {word.upper()} ' + Fore.WHITE)



if __name__ == '__main__':
    main()
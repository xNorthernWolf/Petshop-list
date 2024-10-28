from functions import download_lps, add_lps, remove_lps, list_lps
import sys
sys.dont_write_bytecode = True

while True:
    user_input = input('Would you like to add, remove, list, download or quit?\n').lower()

    if user_input == 'add' or user_input == 'a':
        add_lps.add()
        break
        
    elif user_input == 'remove' or user_input == 'r':
        remove_lps.remove()
        break

    elif user_input == 'list' or user_input == 'l':
        list_lps.list()
        break

    elif user_input == 'download' or user_input == 'd':
        download_lps.download()
        break

    elif user_input == 'ily':
        print("The FUCK you mean, bitch? I'm a poorly programmed Python program.                    Nah, just joking. I love you too <3.")

    elif user_input == 'quit' or user_input == 'q':
        break

    else:
        print('The argument you provided is incorrect, try again')
        
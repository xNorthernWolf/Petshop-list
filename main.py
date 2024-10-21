import os
import shutil
import re
from download_lps import download

lps_all = r'C:\Users\xNort\Desktop\Cosas varias\DevOps\Python\Petshop-list\lps_all'
lps_have = r'C:\Users\xNort\Desktop\Cosas varias\DevOps\Python\Petshop-list\lps_have'


while True:
    user_input = input('Would you like to add, remove, list, download or quit?\n').lower()

    if user_input == 'add' or user_input == 'a':
        ps_input = input('Which numbers? (e.g., 2, 3, 4)\n').lower()
        ps_list = [num.strip() for num in ps_input.split(',')]

        for ps in ps_list:
            matching_pattern = re.compile(r'^\(#' + re.escape(ps) + r'\)', re.IGNORECASE)
            positive_match = False
            for file in os.listdir(lps_all):
                file_path = os.path.join(lps_all, file)
                if matching_pattern.match(file):
                    shutil.move(file_path, lps_have)
                    print(f'successfully added {os.path.splitext(os.path.basename(file_path))[0]}')
                    positive_match = True
            if not positive_match:
                print(f'No matches for #{ps}')
        break
        
    elif user_input == 'remove' or user_input == 'r':
        ps_input = input('Which numbers? (e.g., 2, 3, 4)\n').lower()
        ps_list = [num.strip() for num in ps_input.split(',')]

        for ps in ps_list:
            matching_pattern = re.compile(r'^\(#' + re.escape(ps) + r'\)', re.IGNORECASE)
            positive_match = False
            for file in os.listdir(lps_have):
                file_path = os.path.join(lps_have, file)
                if matching_pattern.match(file):
                    shutil.move(file_path, lps_all)
                    print(f'successfully removed {os.path.splitext(os.path.basename(file_path))[0]}')
                    positive_match = True
            if not positive_match:
                print(f'No matches for #{ps}')
        break

    elif user_input == 'list' or user_input == 'l':
        lps_list = []
        file_names = os.listdir(lps_have)
        for file in file_names:
            start_index = file.find('(')
            end_index = file.find(')')
            if start_index != -1 and end_index != -1 and end_index > start_index:
                  extracted_string = file[start_index + 1:end_index]  # Extract the string between parentheses
            if extracted_string:  # Check if the extracted string is not empty
                lps_list.append(extracted_string)  # Only append non-empty strings
        print(", ".join(lps_list))
        break

    elif user_input == 'download' or user_input == 'd':
        ps_download = input('Which gen would you like to download?\n').lower()
        ps_download_list = [num.strip() for num in ps_download.split(',')]

        for ps_gen in ps_download_list:
            download(ps_gen)

    elif user_input == 'ily':
        print("The FUCK you mean, bitch? I'm a poorly programmed Python program.                    Nah, just joking. I love you too <3.")
  
    elif user_input == 'quit' or user_input == 'q':
        break

    else:
        print('The argument you provided is incorrect, try again')
        
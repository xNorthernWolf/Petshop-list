import os
import shutil
import re


lps_all = r'C:\Users\xNort\Desktop\Cosas varias\DevOps\Python\Petshop-list\lps_all'
lps_have = r'C:\Users\xNort\Desktop\Cosas varias\DevOps\Python\Petshop-list\lps_have'

def remove():
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
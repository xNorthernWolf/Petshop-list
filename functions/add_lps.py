def add():
    import os
    import shutil
    import re

    while True:
        ps_gen_input = input('From what gen is the petshop(s) you want to add?\n').lower()

        # Check if gen input is valid
        if ps_gen_input in ['1', '2', '3', '4', '5', '6', '7']:
            lps_all = rf'C:\Users\xNort\Desktop\Cosas varias\DevOps\Python\Petshop-list\lps_all\gen_{ps_gen_input}'
            lps_have = rf'C:\Users\xNort\Desktop\Cosas varias\DevOps\Python\Petshop-list\lps_have\gen_{ps_gen_input}'
            break
        else:
            print('Please provide a valid gen number.')

    # Check for the petshops
    ps_input = input('Which number(s)? (e.g., 2, 3, 4)\n').lower()
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
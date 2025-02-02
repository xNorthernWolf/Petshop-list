def remove():
    import os
    import shutil
    import re
    from config import lps_path


    while True:
        ps_gen_input = input('From what gen is the petshop(s) you want to remove?\n').lower()

        # Check if gen input is valid
        if ps_gen_input in ['1', '2', '3', '4', '5', '6', '7']:
            lps_all = lps_path + rf'/lps_all/gen_{ps_gen_input}'
            lps_have = lps_path + rf'/lps_have/gen_{ps_gen_input}'
            if ps_gen_input == '6':
                ps_wave_input = input('Which wave is the petshop you want to remove?\n').lower()
            break
        else:
            print('Please provide a valid gen number.')

    # Check for the petshops
    ps_input = input('Which number(s)? (e.g., 2, 3, 4)\n').lower()
    ps_list = [num.strip() for num in ps_input.split(',')]

    for ps in ps_list:
        matching_pattern = re.compile(r'^\(#' + re.escape(ps) + r'\)', re.IGNORECASE)
        if ps_gen_input == '6':
            matching_pattern = re.compile(r'^\(#' + re.escape(ps_wave_input) + '-' + re.escape(ps) + r'\)', re.IGNORECASE)
        elif ps_gen_input == '7':
            matching_pattern = re.compile(r'\(#.*#' + re.escape(ps) + r'\b.*\)', re.IGNORECASE)
        positive_match = False
        for file in os.listdir(lps_have):
            file_path = os.path.join(lps_have, file)
            if matching_pattern.match(file):
                shutil.move(file_path, lps_all)
                print(f'successfully removed {os.path.splitext(os.path.basename(file_path))[0]}')
                positive_match = True
        if not positive_match:
            print(f'No matches for #{ps}')
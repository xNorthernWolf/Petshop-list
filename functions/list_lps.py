def list():
    import os
    from natsort import natsorted
    from config import lps_path


    lps_have = lps_path + rf'/lps_have'
    dir_names = os.listdir(lps_have)

    for directory in dir_names:
        directory_path = os.path.join(lps_have, directory)
        lps_list = []
        print(f'{directory}:')

        for file in os.listdir(directory_path):
            start_index = file.find('(')
            end_index = file.find(')')
            if start_index != -1 and end_index != -1 and end_index > start_index:
                extracted_string = file[start_index + 1:end_index]  # Extract the string between parentheses
                if extracted_string:  # Check if the extracted string is not empty
                    lps_list.append(extracted_string)  # Only append non-empty strings
            
        if lps_list:
            sorted_list = natsorted(lps_list)
            print(", ".join(sorted_list))
        else:
            print('No petshops found')
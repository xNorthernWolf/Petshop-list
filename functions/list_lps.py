import os


lps_all = r'C:\Users\xNort\Desktop\Cosas varias\DevOps\Python\Petshop-list\lps_all'
lps_have = r'C:\Users\xNort\Desktop\Cosas varias\DevOps\Python\Petshop-list\lps_have'

def list():
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
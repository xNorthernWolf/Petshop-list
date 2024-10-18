from unittest import skip
import requests
import bs4
import re
import os


# Gets html and makes it human-readable. Also establishes the directory for the images
url = 'https://lpsmerch.com/g1/all/'
request = requests.get(url)
soup = bs4.BeautifulSoup(request.text, 'html.parser')
image_directory = r'C:\Users\xNort\Desktop\Cosas varias\DevOps\Python\Petshop list\lps_images'


# Filtering the div data (Square than contains each individual petshop info)
filtered_soup = soup.find_all('div', class_='data-item')

bottom_div = soup.find_all('div', class_='data-bottom')
top_div = soup.find_all('div', class_='data-top')

for top in top_div:
    a_tags_top =  top_div.find('a')
    img_tag = a_tags_top.find('img')
    img_url = img_tag.get('src')
    img_response = requests.get(img_url)
    img_name = os.path.join(image_directory, f"{img_response}.jpg")  # Define the image file path
    with open(img_name, 'wb') as f:
        f.write(img_response.content)  # Write the image data to the file
    print(f"Downloaded: {img_name}")  # Print the saved image path
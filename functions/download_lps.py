def download():
    import requests
    import bs4
    import re
    import os

    # Gets html and makes it human-readable. Filters the div data-item from the html (The square that stores the images and the petshop info). Establishes a directory to store the images and a set to avoid downloading duplicates. 
    ps_download = input('Which gen would you like to download?\n').lower()
    ps_download_list = [num.strip() for num in ps_download.split(',')]
    for n in ps_download_list:
        url = rf'https://lpsmerch.com/g{n}/all/'
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, 'html.parser')
        if n == '7' or n == '6':
            filtered_soup = soup.find_all('div', class_='data-item-long')
        else:
            filtered_soup = soup.find_all('div', class_='data-item')
        image_directory = rf'C:\Users\xNort\Desktop\Cosas varias\DevOps\Python\Petshop-list\lps_all\gen_{n}'
        downloaded_items = set()


        # Main loop to iterate through each element
        for element in filtered_soup:

            # Filtering the top and bottom part (Image and info)
            bottom_div = element.find_next('div', class_='data-bottom')
            top_div = element.find_next('div', class_='data-top')

            # Retrieves the name and number of each petshop
            if bottom_div:
                a_tags_bottom = bottom_div.find('a')
                lps_name = a_tags_bottom.get_text(strip=True)
                element_text = element.get_text(strip=True)
                match = re.search(r'\(([^)]*#.*?)\)', element_text)
                if match:
                    lps_number = match.group()
                lps_name_num = lps_number + ' ' + lps_name
                
                # Skip if this item has already been downloaded, else add it to the downloaded items set
                if lps_name_num in downloaded_items:
                    print(f"Skipping duplicate: {lps_name_num}")
                    continue
                else:
                    downloaded_items.add(lps_name_num)

                # Retrieves the image of each petshop
                if top_div:
                    a_tags_top =  top_div.find('a')
                    img_url = a_tags_top.get('href')
                    img_response = requests.get(img_url)
                    img_name = os.path.join(image_directory, f"{lps_name_num}.jpg")
                    with open(img_name, 'wb') as f:
                        f.write(img_response.content)
                    print(f"Downloaded: {lps_name_num}.jpg")
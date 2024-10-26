import requests
from bs4 import BeautifulSoup
import random

def get_male_first_names(url):
    response = requests.get(url)

    i = 0
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', attrs={'rules': 'none'})
        if table:
            list_of_male_firstNames = []
            
            for row in table.find_all('tr'):
                if i not in [0,1, 168]:
                    cells = row.find_all('td') 
                    # print(cells)
                    first_name = cells[2].text.strip() 
                    list_of_male_firstNames.append(first_name)
                    first_name = cells[6].text.strip() 
                    list_of_male_firstNames.append(first_name)
                    first_name = cells[10].text.strip() 
                    list_of_male_firstNames.append(first_name)
                if i == 168:
                    cells = row.find_all('td') 
                    # print(cells)
                    first_name = cells[2].text.strip() 
                    list_of_male_firstNames.append(first_name)
                    first_name = cells[6].text.strip() 
                    list_of_male_firstNames.append(first_name)
                i += 1 
            return list_of_male_firstNames
        else:
            return "Table with rules='none' not found."
    else:
        return f"Failed to retrieve the page, status code: {response.status_code}"

def get_female_first_names(url):
    response = requests.get(url)

    i = 0
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', attrs={'rules': 'none'})
        if table:
            list_of_female_firstNames = []
            
            for row in table.find_all('tr'):
                if i not in [0,1, 165]:
                    cells = row.find_all('td') 
                    # print(len(table.find_all('tr')))
                    first_name = cells[2].text.strip() 
                    list_of_female_firstNames.append(first_name)
                    first_name = cells[6].text.strip() 
                    list_of_female_firstNames.append(first_name)
                    first_name = cells[10].text.strip() 
                    list_of_female_firstNames.append(first_name)
                if i == 165:
                    cells = row.find_all('td') 
                    # print(cells)
                    first_name = cells[2].text.strip() 
                    list_of_female_firstNames.append(first_name)
                i += 1 
            return list_of_female_firstNames
        else:
            return "Table with rules='none' not found."
    else:
        return f"Failed to retrieve the page, status code: {response.status_code}"
    
def get_last_names(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table with the class name you specified
    table = soup.find('table', attrs={'class': 'table forename-table'})
    if table:
        list_of_female_surNames = []

        # Iterate over the rows of the table
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) >= 2:
                # Extract the second cell's text and add it to the list
                first_name = cells[1].text.strip()
                list_of_female_surNames.append(first_name)

        return list_of_female_surNames
    else:
        return "Table with class 'table forename-table' not found."

def get_commune_names(url):
    response = requests.get(url)
    
    if response.status_code == 200:

        soup = BeautifulSoup(response.content, "html.parser")
        tables = soup.find_all("table")
        communes = []
        for table in tables:
            for row in table.find_all("tr"):
                cells = row.find_all(["td"])
                # print(cells)
                text = cells[0].text.strip()
                if text:
                    communes.append(text)
        communes = [commune for commune in communes if commune not in {"Municipality", "Commune"}]
        
        return communes
    else:
        return f"Failed to retrieve the page, status code: {response}"

def generate_students_names(size, base_list, seed=None):

    size = int(size)

    if size > len(base_list):
        return "Size too large"
    if seed is not None:
        seed= int(seed)
        random.seed(seed)
    
    selected_names = random.choices(base_list, k=size)
    
    return selected_names

def concatenate_lists(list1, list2, list3):
    # Ensure the length of list3 is equal to the sum of list1 and list2
    # print(len(list3))
    # print(len(list1))
    # print(len(list2))
    if len(list3) != len(list1) + len(list2):
        return "The length of list3 must be equal to the sum of list1 and list2."

    result = []

    # Concatenate elements from list1 with the corresponding elements in list3
    for i in range(len(list1)):
        result.append(list1[i] +' '+ list3[i])

    # Concatenate elements from list2 with the remaining elements in list3
    offset = len(list1)
    for j in range(len(list2)):
        result.append(list2[j] +' '+ list3[offset + j])

    return result
    

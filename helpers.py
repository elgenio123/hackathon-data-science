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
    
def get_last_names(url):

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', attrs={'class': 'table forename-table'})
        if table:
            list_of_female_surNames = []
            
            for row in table.find_all('tr'):
                cells = row.find_all('td') 
                # print(row)
                if len(cells)>=2:

                    first_name = cells[1].text.strip()
                    list_of_female_surNames.append(first_name)
            return list_of_female_surNames
        else:
            return "Table with rules='none' not found."
    else:
        return f"Failed to retrieve the page, status code: {response}"

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

def concatenate_lists(list300, list140, list160):
    result = []
    
    len140 = len(list140)
    len160 = len(list160)
    
    for i in range(len(list300)):
        if i < len140:
            concatenated = list140[i] +' '+ list300[i]
        else:
            index_in_160 = i - len140
            if index_in_160 < len160:
                concatenated = list160[index_in_160] +' '+ list300[i]
            else:
                concatenated = list300[i]
                
        result.append(concatenated)
    
    return result
    

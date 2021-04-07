import requests
from bs4 import BeautifulSoup

def get_data():
    url = 'https://www.worldometers.info/coronavirus/country/portugal/'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all("div", class_="maincounter-number")  #returns a list


    # getting data from each index with span tag
    total_cases = results[0].find("span")
    total_deaths = results[1].find("span")
    recovered_cases = results[2].find("span")

    # printing the numbers we wanted
    print(total_cases.text)
    print(total_deaths.text)
    print(recovered_cases.text)


get_data()

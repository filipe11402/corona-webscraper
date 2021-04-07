import requests
from bs4 import BeautifulSoup


def get_data(country):
    url = ('https://www.worldometers.info/coronavirus/country/{}/').format(country)  #getting data based on contry paramete

    try:
        page = requests.post(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find_all("div", class_="maincounter-number")  #returns a list


        # getting data from each index with span tag
        total_cases = results[0].find("span")
        total_deaths = results[1].find("span")
        recovered_cases = results[2].find("span")

        # printing the numbers we wanted
        print("Total Cases: ", total_cases.text)
        print("Total Deaths: ", total_deaths.text)
        print("Recovered Cases: ", recovered_cases.text)

    except IndexError as list_error:  # catch error if country passed doesnt exist, the website doesnt return error code
        print("That country doesnt exist")

get_data("Portugal")  #Portugal data with Show

# beautiful soup is a library/package ->  extract the data from html webpage

import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.espncricinfo.com/series/ipl-2021-1249214/points-table-standings"
    response = requests.get(url)
    print(response.text)


    # soup is object of Beautiful soup
    # html.parser is a string that should be passed
    soup = BeautifulSoup(response.text, "html.parser")

    # find all h5 tags of class header-title lable
    tags = soup.findAll("h5", class_="header-title label")

    # it is a list

    team_names = []

    # it will print the team names
    for tag in tags:
        print(tag.text)

        team_names.append(tag.text.strip())

    # removing the first element from the list bcoz it will takes indian premier league as a team name
    print(team_names.pop(0))
    print(team_names)
    print(len(team_names))



if __name__ == '__main__':
    main()
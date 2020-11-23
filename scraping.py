import requests
from bs4 import BeautifulSoup

address = 'https://www.sportsbookreview.com'
extension = '/betting-odds/college-football'
address_list = []

html_data = requests.get(address + extension)
soup = BeautifulSoup(html_data.text, 'lxml')
for links in soup.find_all('a', class_='gradientContainer-3iN6G'):
    address_list.append(links['href'])

game_data = requests.get(address + address_list[0])
soup2 = BeautifulSoup(game_data.text, 'lxml')
container = soup2.find('div', class_='columnsContainer-2RLhf')

teams = container.find_all('span', class_='participantBox-3ar9Y')
team1 = teams[0].text
team2 = teams[1].text

print(team1, " vs ", team2)

import requests
from bs4 import BeautifulSoup

address = 'https://www.sportsbookreview.com'
extension = '/betting-odds/college-football'
address_list = []

html_data = requests.get(address + extension)
soup = BeautifulSoup(html_data.text, 'lxml')
for links in soup.find_all('a', class_='gradientContainer-3iN6G'):
    address_list.append(links['href'])

#Loop through all links
game_data = requests.get(address + address_list[0])
soup2 = BeautifulSoup(game_data.text, 'lxml')

section = soup2.find('section', class_='container-2-2cB')
date = section.find('label').text

#full game numbers
full_game = soup2.find('div', class_='container-2fbfV')

teams = full_game.find_all('span', class_='participantBox-3ar9Y')
team1 = teams[0].text
team2 = teams[1].text

lines = full_game.find_all('span', class_='opener')
team1_spread = lines[2].text[:-1]
team1_spread_odds = lines[3].text
team2_spread = lines[4].text[:-1]
team2_spread_odds = lines[5].text
team1_moneyline = lines[8].text
team2_moneyline = lines[9].text
over_under = lines[12].text[:-1]
over_odds = lines[13].text
under_odds = lines[15].text

print(date)
print(team1, " ", team1_spread, " ", team1_spread_odds)
print(team1_moneyline)
print(team2, " ", team2_spread, " ", team2_spread_odds)
print(team2_moneyline)
print(over_under, " ", over_odds, " ", under_odds)

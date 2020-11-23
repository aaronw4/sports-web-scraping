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

game_period = soup2.find_all('div', class_='container-2fbfV')

#full game numbers
full_game = game_period[0]

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

#first half numbers
first_half = game_period[1]

first_half_lines = first_half.find_all('span', class_='opener')
first_half_team1_spread = first_half_lines[2].text
first_half_team1_spread_odds = first_half_lines[3].text
first_half_team2_spread = first_half_lines[4].text
first_half_team2_spread_odds = first_half_lines[5].text
first_half_team1_moneyline = first_half_lines[8].text
first_half_team2_moneyline = first_half_lines[9].text
first_half_over_under = first_half_lines[12].text
first_half_over_odds = first_half_lines[13].text
first_half_under_odds = first_half_lines[15].text


print(date)
print(team1, " ", first_half_team1_spread, " ", first_half_team1_spread_odds)
print(first_half_team1_moneyline)
print(team2, " ", first_half_team2_spread, " ", first_half_team2_spread_odds)
print(first_half_team2_moneyline)
print(first_half_over_under, " ", first_half_over_odds, " ", first_half_under_odds)

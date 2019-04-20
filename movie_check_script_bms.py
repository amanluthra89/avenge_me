import urllib.request as urllib
from bs4 import BeautifulSoup
import time
import requests
import random

city_arr = ["mumbai"]
site = "https://in.bookmyshow.com/mumbai/movies/avengers-endgame/ET00090482"

delay = 60
SAD_DIALOGUES = ["I don't feel so good Mr Stark.", "I am Groot", "You are not the only one cursed with knowledge.", 
"I hope they remember you", "All words are made up.", "When Im done, half of humanity will still exist.", 
"I assure you, brother, the sun will shine on us again.", "The hardest choices require the strongest of wills.", 
"Lets talk about this plan of yours. I think its good, except it sucks.", "No resurrections this time.",
"I wouldnt say no to a Tuna Melt.", "Broke up? Like a band? Like the Beatles?", "Never tell me the odds - whoops, wrong movie",
"Why is Gamora?", "The rabbit is correct, and clearly the smartest one.", "Ive mastered the ability of standing so incredibly still that Ive become invisible to the eye.",
"Theres an Ant-Man and a Spider-Man?", "Oh. We are using our made-up names.", "Kick names, take ass.", "Exactly like Footloose. Is it still the greatest movie in history?",
"Fourteen million six hundred and five.", "Hey guys, you ever see that really old movie, Empire Strikes Back? When they're on the snow planet? With the walking thingies?"]

def telegram_bot_sendtext(msg):
    bot_token = '654480132:AAElQU1AhEz269a-dADYsBDi7fw04YnMiPg'
    bot_chatID = '-320332082'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + msg
    response = requests.get(send_text)
    return response.json()

while True:
  site = "https://in.bookmyshow.com/buytickets/avengers-endgame-bengaluru/movie-bang-ET00100668-MT/20190426"
  req = urllib.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
  page = urllib.urlopen(req)
  soup = BeautifulSoup(page)
  s = soup.find_all('div', {'__name'})
  for venue in s:
      string_venue = str(venue.find('a').contents[1])
      print(string_venue)
      if 'PVR' in string_venue:
          telegram_bot_sendtext("PVR BLR IMAX DEFCON RED")
  site = "https://in.bookmyshow.com/buytickets/avengers-endgame-kolhapur/movie-kolh-ET00100559-MT/20190426"
  req = urllib.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
  page = urllib.urlopen(req)
  soup = BeautifulSoup(page)
  s = soup.find_all('div', {'__name'})
  for venue in s:
      string_venue = str(venue.find('a').contents[1])
      print(string_venue)
      if 'PVR' in string_venue:
          telegram_bot_sendtext("PVR KOLHAPUR AVAILABLE - GO GO GO")    
  time.sleep(delay)
  # for city in city_arr:
  #   site = "https://in.bookmyshow.com/"+city+"/movies/avengers-endgame/ET00090482"
  #   req = urllib.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
  #   page = urllib.urlopen(req)
  #   soup = BeautifulSoup(page)
  #   soup2 = soup.find_all('div', {'action-book'})
  #   imax_soup = soup.find_all('div' ,{'format-dimensions'})
  #   message = city + " - " + random.choice(SAD_DIALOGUES) + " --- No tickets yet."
    # for div in soup2:
    #   if(div.find('a') != None):
    #     if 'Book' in div.find('a').contents[0]:
    #       message = city + " -- Tickets available! --- We're in the Endgame now!! Go Go Go!!!"
    # for div in imax_soup:
    #   for i in div.find_all('a'):
    #     if 'IMAX' in i.contents[0]:
    #       message = message + ' --- IMAX!!!!'
    #       telegram_bot_sendtext(message)
    #       break
    #     if '3D' in div.find('a').contents[0]:
    #       message = message + ' --- 3D'
    #       break
    # print(message)
  
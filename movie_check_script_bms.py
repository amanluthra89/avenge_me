import urllib.request as urllib
from bs4 import BeautifulSoup
import time
import requests
import random

city_arr = ["mumbai", "bengaluru", "kolhapur"]
site = "https://in.bookmyshow.com/mumbai/movies/avengers-endgame/ET00090482"

delay = 3600
SAD_DIALOGUES = ["I don't feel so good Mr Stark.", "I am Groot", "You are not the only one cursed with knowledge.", 
"I hope they remember you", "All words are made up.", "When Im done, half of humanity will still exist.", 
"I assure you, brother, the sun will shine on us again.", "The hardest choices require the strongest of wills.", 
"Lets talk about this plan of yours. I think its good, except it sucks.", "No resurrections this time.",
"I wouldnt say no to a Tuna Melt.", "Broke up? Like a band? Like the Beatles?", "Never tell me the odds - whoops, wrong movie",
"Why is Gamora?", "The rabbit is correct, and clearly the smartest one.", "Ive mastered the ability of standing so incredibly still that Ive become invisible to the eye.",
"Theres an Ant-Man and a Spider-Man?", "Oh. We are using our made-up names.", "Kick names, take ass.", "Exactly like Footloose. Is it still the greatest movie in history?",
"Fourteen million six hundred and five."]

def telegram_bot_sendtext(msg):
    bot_token = '654480132:AAElQU1AhEz269a-dADYsBDi7fw04YnMiPg'
    bot_chatID = '-320332082'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + msg
    response = requests.get(send_text)
    return response.json()

while True:
  for city in city_arr:
    site = "https://in.bookmyshow.com/"+city+"/movies/avengers-endgame/ET00090482"
    req = urllib.Request(site)
    page = urllib.urlopen(req)
    soup = BeautifulSoup(page)
    soup2 = soup.find_all('div', {'action-book'})
    message = city + " - " + random.choice(SAD_DIALOGUES) + " --- No tickets yet."
    for div in soup2:
      if(div.find('a') != None):
        if 'Book' in div.find('a').contents[0]:
          message = "Tickets available! --- We're in the Endgame now!! Go Go Go!!!"
    telegram_bot_sendtext(message)
  time.sleep(delay)
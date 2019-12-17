import urllib.request as urllib
from bs4 import BeautifulSoup
import time
import requests
import random

city_arr = ["mumbai"]
city = "mumbai"
# site = "https://in.bookmyshow.com/mumbai/movies/avengers-endgame/ET00090482"

delay = 100
SAD_DIALOGUES = ["I don't feel so good Mr Stark.", "I am Groot", "You are not the only one cursed with knowledge.", 
"I hope they remember you", "All words are made up.", "When Im done, half of humanity will still exist.", 
"I assure you, brother, the sun will shine on us again.", "The hardest choices require the strongest of wills.", 
"Lets talk about this plan of yours. I think its good, except it sucks.", "No resurrections this time.",
"I wouldnt say no to a Tuna Melt.", "Broke up? Like a band? Like the Beatles?", "Never tell me the odds - whoops, wrong movie",
"Why is Gamora?", "The rabbit is correct, and clearly the smartest one.", "Ive mastered the ability of standing so incredibly still that Ive become invisible to the eye.",
"Theres an Ant-Man and a Spider-Man?", "Oh. We are using our made-up names.", "Kick names, take ass.", "Exactly like Footloose. Is it still the greatest movie in history?",
"Fourteen million six hundred and five.", "Hey guys, you ever see that really old movie, Empire Strikes Back? When they're on the snow planet? With the walking thingies?"]

STAR_WARS_DIALOGUES = [
      "You must do what you feel is right, of course. \n-Obi-Wan Kenobi",
      "Mos Eisley Spaceport. You will never find a more wretched hive of scum and villainy. We must be cautious. \n-Obi-Wan Kenobi",
      "Your eyes can deceive you. Don’t trust them. \n-Obi-Wan Kenobi",
      "Remember... the Force will be with you, always. \n-Obi-Wan Kenobi",
      "In my experience, there is no such thing as luck. \n-Obi-Wan Kenobi",
      "These aren't the droids you're looking for. \n-Obi-Wan Kenobi",
      "I felt a great disturbance in the Force, as if millions of voices suddenly cried out in terror and were suddenly silenced. \n-Obi-Wan Kenobi",
      "Use the Force, Luke.\n-Obi-Wan Kenobi",
      "You can't win, Darth. If you strike me down, I shall become more powerful than you could possibly imagine. \n-Obi-Wan Kenobi",
      "That's no moon. It's a space station. \n-Obi-Wan Kenobi",
      "Luke! Don't give in to hate. That leads to the Dark Side. \n-Obi-Wan Kenobi",
      "Who's the more foolish, the fool or the fool who follows him? \n-Obi-Wan Kenobi",
      "And these blast points, too accurate for Sandpeople. Only Imperial Stormtroopers are so precise. \n-Obi-Wan Kenobi",
      "I find your lack of faith disturbing. \n-Darth Vader",
      "The circle is now complete. When I left you, I was but the learner. Now I am the master. \n-Darth Vader",
      "The Force is with you, young Skywalker, but you are not a Jedi yet. \n-Darth Vader",
      "No. I am your father. \n-Darth Vader",
      "Impressive. Most impressive. \n-Darth Vader",
      "I am altering the deal. Pray I don't alter it any further. \n-Darth Vader",
      "You underestimate the power of the Dark Side. If you will not fight, then you will meet your destiny. \n-Darth Vader",
      "You have failed me for the last time, Admiral! \n-Darth Vader",
      "The Force is strong with this one. \n-Darth Vader",
      "The ability to destroy a planet is insignificant next to the power of the Force. \n-Darth Vader",
      "Do. Or do not. There is no try. \n-Yoda",
      "You must unlearn what you have learned. \n-Yoda",
      "When nine hundred years old you reach, look as good you will not. \n-Yoda",
      "Truly wonderful, the mind of a child is. \n-Yoda",
      "A Jedi uses the Force for knowledge and defense, never for attack. \n-Yoda",
      "Adventure. Excitement. A Jedi craves not these things. \n-Yoda",
      "Size matters not. Judge me by my size, do you? \n-Yoda",
      "Fear is the path to the dark side…fear leads to anger…anger leads to hate…hate leads to suffering. \n-Yoda",
      "Wars not make one great. \n-Yoda",
      "Luminous beings are we…not this crude matter. \n-Yoda",
      "Difficult to see. Always in motion is the future. \n-Yoda",
      "Control, control, you must learn control! \n-Yoda",
      "I'll never turn to the Dark Side. You've failed, your highness. I am a Jedi, like my father before me. \n-Luke Skywalker",
      "If there's a bright center to the universe, you're on the planet that it's farthest from. \n-Luke Skywalker",
      "I'm Luke Skywalker. I'm here to rescue you. \n-Luke Skywalker",
      "The Force is strong in my family. My father has it. I have it. My sister has it. You have that power, too. \n-Luke Skywalker",
      "But I was going into Tosche Station to pick up some power converters! \n-Luke Skywalker",
      "Chewie...we're home. \n-Han Solo",
      "Never tell me the odds. \n-Han Solo",
      "Women always figure out the truth. Always. \n-Han Solo",
      "Fast ship? You've never heard of the Millennium Falcon? It's the ship that made the Kessel Run in less than twelve parsecs. \n-Han Solo",
      "Great shot, kid, that was one in a million! \n-Han Solo",
      "Boring conversation anyway. LUKE, WE'RE GONNA HAVE COMPANY! \n-Han Solo",
      "No reward is worth this. \n-Han Solo",
      "Wonderful girl. Either I'm going to kill her or I'm beginning to like her. \n-Han Solo",
      "Look, Your Worshipfulness, let's get one thing straight. I take orders from just one person: me. \n-Han Solo",
      "Help me, Obi-Wan Kenobi. You're my only hope. \n-Princess Leia Organa",
      "Aren't you a little short for a stormtrooper? \n-Princess Leia Organa",
      "Someone has to save our skins. Into the garbage chute, fly boy. \n-Princess Leia Organa",
      "Will someone get this big walking carpet out of my way? \n-Leia Organa",
      "You needn't worry about your reward. If money is all that you love, then that's what you'll receive. \n-Leia Organa",
      "Young fool... Only now, at the end, do you understand... \n-The Emperor",
      "Your feeble skills are no match for the power of the Dark Side. \n-The Emperor",
      "Now, you will pay the price for your lack of vision! \n-The Emperor",
      "I will make it legal. \n-Darth Sidious",
      "Many Bothans died to bring us this information. \n-Mon Mothma",
      "Charming to the last. You don't know how hard I found it, signing the order to terminate your life. \n-Governor Tarkin",
      "It's a trap! \n-Admiral Ackbar",
      "So this is how liberty dies…with thunderous applause. \n-Padmé Amidala",
      "He's no good to me dead. \n-Boba Fett",
      "I've got a bad feeling about this. \n-Various characters in Star Wars",
      "May the force be with you. \n-Various characters in Star Wars"
    ];

def telegram_bot_sendtext(msg):
    bot_token = '654480132:AAElQU1AhEz269a-dADYsBDi7fw04YnMiPg'
    bot_chatID = '-320332082'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + msg
    response = requests.get(send_text)
    return response.json()

while True:
  # site = "https://in.bookmyshow.com/buytickets/avengers-endgame-bengaluru/movie-bang-ET00100668-MT/20190426"
  # site = "https://in.bookmyshow.com/chennai/movies/star-wars-the-rise-of-skywalker-3d/ET00120440"
  site = "https://in.bookmyshow.com/mumbai/movies/star-wars-the-rise-of-skywalker/ET00115302"
  req = urllib.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
  page = urllib.urlopen(req)
  soup = BeautifulSoup(page)
  s = soup.find_all('div', {'__name'})
  # for venue in s:
  #     string_venue = str(venue.find('a').contents[1])
  #     print(string_venue)
  #     if 'PVR' in string_venue and 'Vega' in string_venue:
  #         telegram_bot_sendtext("PVR BLR VEGA IMAX DEFCON RED")
  # site = "https://in.bookmyshow.com/buytickets/avengers-endgame-kolhapur/movie-kolh-ET00100559-MT/20190426"
  # req = urllib.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
  # page = urllib.urlopen(req)
  # soup = BeautifulSoup(page)
  # s = soup.find_all('div', {'__name'})
  # for venue in s:
  #     string_venue = str(venue.find('a').contents[1])
  #     print(string_venue)
  #     if 'PVR' in string_venue:
  #         telegram_bot_sendtext("PVR KOLHAPUR AVAILABLE - GO GO GO")    
  # for city in city_arr:
  # site = "https://in.bookmyshow.com/"+city+"/movies/avengers-endgame/ET00090482"
  # req /= urllib.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
  # page = urllib.urlopen(req)
  # soup = BeautifulSoup(page)
  soup2 = soup.find_all('div', {'action-book'})
  imax_soup = soup.find_all('div' ,{'format-dimensions'})
  message = city + " - " + random.choice(STAR_WARS_DIALOGUES) + " --- No tickets yet."
  for div in soup2:
    if(div.find('a') != None):
      if 'Book' in div.find('a').contents[0]:
        message = city + " -- Tickets available! --- We're in the Endgame now!! Go Go Go!!!"
        # telegram_bot_sendtext(message)
  for div in imax_soup:
    for i in div.find_all('a'):
      if 'IMAX' in i.contents[0]:
        message = message + ' --- IMAX!!!!'
        telegram_bot_sendtext(message)
        break
      if '3D' in div.find('a').contents[0]:
        message = message + ' --- 3D'
        telegram_bot_sendtext(message)
        break
  print(message)
  telegram_bot_sendtext("testing  -- " + message)
  time.sleep(delay)
  

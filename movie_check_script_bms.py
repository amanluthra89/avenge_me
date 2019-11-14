import urllib.request as urllib
from bs4 import BeautifulSoup
import time
import requests
import random
import http.cookiejar as cookielib
import sys


city_arr = ["mumbai"]
site = "https://in.bookmyshow.com/mumbai/movies/avengers-endgame/ET00090482"

delay = 600
cutoff_val = 90000
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

def flight_results(src="BOM", dest="HKT", dept="20191110", arr=None):
	url = "http://developer.goibibo.com/api/search/?app_id=06bfd1ce&app_key=bc415f52afe2a3301cb143923d4675de&format=json&source="+src+"&destination="+dest+"&dateofdeparture="+dept+"&seatingclass=E&adults=1&children=0&infants=0&counter=0"
	r = requests.get(url)
	rj = r.json()
	for i in rj['data']['onwardflights']:
		if i['fare']['adulttotalfare'] < cutoff_val:
			msgs = create_msg(i)
			for msg in list(msgs.values()):
				if "United" in msg:
					print("here we go")
					telegram_bot_sendtext(msg)
					return

def create_msg(flight):
	h={}
	message = 'Found a Flight!\n'
	message += flight['origin']+' to '+flight['destination']+'\n'
	deptime = flight['depdate'].split('t')
	arrtime = flight['arrdate'].split('t')
	message += deptime[0]+' - '+deptime[1]+' to '+arrtime[0]+' - '+arrtime[1]+'\n'
	message += 'Flight time: '+flight['splitduration']+'\n'
	if len(flight['onwardflights']) > 0:
		for f in flight['onwardflights']:
			message += f['origin']+' to '+f['destination']+'\n'
			deptime = f['depdate'].split('t')
			arrtime = f['arrdate'].split('t')
			message += deptime[0]+' - '+deptime[1]+' to '+arrtime[0]+' - '+arrtime[1]+'\n'
			message += 'Flight time: '+f['splitduration']+'\n'
	message += 'Cost: '+str(flight['fare']['adulttotalfare'])+'\n'
	message += 'Airline: '+str(flight['airline'])
	h[flight['fare']['adulttotalfare']] = message
	print(h)
	return h

def send_sms(msg):
	url = 'http://site24.way2sms.com/Login1.action?'
	data = 'username=9769599417&password=T4292C&Submit=Sign+in'
	cj = cookielib.CookieJar()
	opener = urllib.build_opener(urllib.HTTPCookieProcessor(cj))
	opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
	opener.open(url, data)
	session_id = str(cj).split('~')[1].split(' ')[0]
	send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
	send_sms_data = 'ssaction=ss&Token='+str(session_id)+'&mobile=9769599417&message='+msg+'&msgLen=136'
	opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+session_id)]
	opener.open(send_sms_url,send_sms_data)    

while True:
	flight_results("BOM", "IXJ", "20200224", "20200228")
	time.sleep(delay)

def movie_check(site_url):
	site = "https://in.bookmyshow.com/buytickets/avengers-endgame-bengaluru/movie-bang-ET00100668-MT/20190426"
	req = urllib.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
	page = urllib.urlopen(req)
	soup = BeautifulSoup(page)
	s = soup.find_all('div', {'__name'})
	for venue in s:
		string_venue = str(venue.find('a').contents[1])
		print(string_venue)
		if 'PVR' in string_venue and 'Vega' in string_venue:
			telegram_bot_sendtext("PVR BLR VEGA IMAXDEFCON RED")
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


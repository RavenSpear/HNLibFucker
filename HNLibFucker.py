from time import sleep
import requests
import datetime
import random

# Static data
URL = "https://office.chaoxing.com/data/apps/seat/submit"
HEADERS = {
        "Host": "",
        "Connection": "",
        "Accept": "",
        "User-Agent": "",
        "X-Requested-With": "",
        "Sec-Fetch-Site": "",
        "Sec-Fetch-Mode": "",
        "Sec-Fetch-Dest": "",
        "Referer": "",
        "Accept-Encoding": "",
        "Accept-Language": "",
        "Cookie": "",
}# Fill in the blanks with information specific to your application, especially for <Cookie>.
PARAMS = {
        'roomId': '7826',
        'startTime': '08:00',
        'endTime': '17:30',
        'day': '',
        'seatNum': '',
        'captcha': '',
        'token': ''
}# Fill in <token> with information specific to your application.
START_TIME = datetime.time(18,00,00,000)
SEATS = 108
MAX_FUCK_ATTEMPTS = 20

# Required date & time info.
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days = 1)
currenttime = datetime.datetime.now().time()

# Control variables
fucked = False 
fuckattempts = 0
seatsvacant = []

# Params initialization
for num in range(0, SEATS):
        seatsvacant.append(num)
seatindex = random.randint(0, SEATS - 1)
PARAMS['day'] = tomorrow.strftime("%Y-%m-%d")
PARAMS['seatNum'] = seatsvacant[seatindex]

# Try to fuck
while(fucked == False and fuckattempts < MAX_FUCK_ATTEMPTS):
        if(currenttime >= START_TIME):
                if(fuckattempts != 0):
                        seatindex = random.randint(0, len(seatsvacant) - 1)
                        PARAMS['seatNum'] = seatsvacant[seatindex]
                response = requests.get(url=URL, headers=HEADERS, params = PARAMS)
                if(response.json()["success"] == True):
                        print("Huaining Lib is fucked! Your seat NO.: " + str(seatsvacant[seatindex]))
                        fucked = True
                else:
                        print(str(fuckattempts) + ". Fuck failed: " + str(seatsvacant[seatindex]))
                        fuckattempts += 1
                        sleep(1)
                seatsvacant.pop(seatindex)

# Best wishes.
if(fucked == False):
        print("FUCK! Good Luck Tomorrow.")

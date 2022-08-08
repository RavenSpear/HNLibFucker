from time import sleep
import requests
import datetime
import random
import re

# Static data
LIST_URL = 'https://office.chaoxing.com/front/apps/seat/list'
SELECT_URL = 'https://office.chaoxing.com/front/apps/seat/select'
SUBMIT_URL = 'https://office.chaoxing.com/data/apps/seat/submit'
HEADERS = {
        "Host": "office.chaoxing.com",
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
        "Cookie": ""
}# Fill in the blanks with information specific to your application, especially for <Cookie>.   
LIST_PARAMS = {
        'deptIdEnc': 'b143e8d5830ee353'
}
SELECT_PARAMS = {
        'id': '7826',
        'day': '',
        'backLevel': 2,
        'pageToken': ''
}
SUBMIT_PARAMS = {
        'roomId': '7826',
        'startTime': '08:00',
        'endTime': '17:30',
        'day': '',
        'seatNum': '',
        'captcha': '',
        'token': ''
}
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

# Fetch token
response = requests.get(url=LIST_URL, headers=HEADERS, params=LIST_PARAMS)
SELECT_PARAMS['pageToken'] = re.compile(r"pageToken=' \+ '(.*)'").findall(response.text)[0]
SELECT_PARAMS['day'] = today.strftime("%Y-%m-%d")
response = requests.get(url=SELECT_URL, headers=HEADERS, params=SELECT_PARAMS)
SUBMIT_PARAMS['token'] = re.compile("token: '(.*)'").findall(response.text)[0]

# Params initialization
for num in range(0, SEATS):
        seatsvacant.append(num)
seatindex = random.randint(0, SEATS - 1)
SUBMIT_PARAMS['day'] = tomorrow.strftime("%Y-%m-%d")
SUBMIT_PARAMS['seatNum'] = seatsvacant[seatindex]
print(SUBMIT_PARAMS)
# Try to fuck
while(fucked == False and fuckattempts < MAX_FUCK_ATTEMPTS):
        if(currenttime >= START_TIME):
                if(fuckattempts != 0):
                        seatindex = random.randint(0, len(seatsvacant) - 1)
                        SUBMIT_PARAMS['seatNum'] = seatsvacant[seatindex]
                response = requests.get(url=SUBMIT_URL, headers=HEADERS, params = SUBMIT_PARAMS)
                if(response.json()["success"] == True):
                        print("Huaining Lib is fucked! Your seat NO.: " + str(seatsvacant[seatindex]))
                        fucked = True
                else:
                        print(str(fuckattempts) + ". Fuck failed: " + str(seatsvacant[seatindex]))
                        print(response.text)
                        fuckattempts += 1
                        #sleep(0.3)
                seatsvacant.pop(seatindex)
        else:
                currenttime = datetime.datetime.now().time()

# Best wishes.
if(fucked == False):
        print("FUCK! Good Luck Tomorrow.")

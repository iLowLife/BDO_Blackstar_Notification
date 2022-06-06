import requests
import time
import pytz
from datetime import datetime
import json

timezone = pytz.timezone('Singapore')

discordBot = "Your Discord Webhook URL here"  # <<<<<<<<<<<<<<<<<<<<< Change this

url = 'https://trade.sea.playblackdesert.com/Trademarket/GetWorldMarketWaitList' 
headers = {
  "Content-Type": "application/json",
  "User-Agent": "BlackDesert"
}

payload = {}

BlackstarDict = {
    '715005-20' : 'Blackstar Amulet',
    '715007-20' : 'Blackstar Axe',
    '690563-20' : 'Blackstar Battle Axe',
    '715011-20' : 'Blackstar Blade',
    '715019-20' : 'Blackstar Crescent Pendulum',
    '715021-20' : 'Blackstar Crossbow',
    '718616-20' : 'Blackstar Florang',
    '715017-20' : 'Blackstar Gauntlet',
    '715016-20' : 'Blackstar Kriegsmesser',
    '732313-20' : 'Blackstar Kyve',
    '715003-20' : 'Blackstar Longbow',
    '715001-20' : 'Blackstar Longsword',
    '730564-20' : 'Blackstar Morning Star',
    '733063-20' : 'Blackstar Serenaca',
    '692045-20' : 'Blackstar Shamshir',
    '715009-20' : 'Blackstar Shortsword',
    '715013-20' : 'Blackstar Staff',
    '731111-20' : 'Blackstar Aad Sphera',
    '731105-20' : 'Blackstar Celestial Bo Staff',
    '731115-20' : 'Blackstar Cestus',
    '731107-20' : 'Blackstar Crescent Blade',
    '731117-20' : 'Blackstar Crimson Glaives',
    '731119-20' : 'Blackstar Dual Glaives',
    '731114-20' : 'Blackstar Gardbrace',
    '731112-20' : 'Blackstar Godr Sphera',
    '731116-20' : 'Blackstar Greatbow',
    '731101-20' : 'Blackstar Greatsword',
    '731103-20' : 'Blackstar Iron Buster',
    '731118-20' : 'Blackstar Jordun',
    '731104-20' : 'Blackstar Kamasylven Sword',
    '731108-20' : 'Blackstar Kerispear',
    '731121-20' : 'Blackstar Kibelius',
    '731106-20' : 'Blackstar Lancia',
    '731122-20' : 'Blackstar Patraca',
    '731110-20' : 'Blackstar Sah Chakram',
    '731102-20' : 'Blackstar Scythe',
    '731120-20' : 'Blackstar Sting',
    '731109-20' : 'Blackstar Sura Katana',
    '731113-20' : 'Blackstar Vediant',
    '735001-20' : 'Blackstar Shield',
    '735002-20' : 'Blackstar Dagger',
    '735003-20' : 'Blackstar Talisman',
    '735004-20' : 'Blackstar Ornamental Knot',
    '735005-20' : 'Blackstar Trinket',
    '735006-20' : 'Blackstar Horn Bow',
    '735007-20' : 'Blackstar Kunai',
    '735008-20' : 'Blackstar Shuriken',
    '735009-20' : 'Blackstar Vambrace',
    '735010-20' : 'Blackstar Noble Sword',
    '735011-20' : 'Blackstar Raghon',
    '735012-20' : 'Blackstar Vitclari',
    '735013-20' : 'Blackstar Haladie',
    '735014-20' : 'Blackstar Quoratum',
    '735015-20' : 'Blackstar Mareca',
    '735016-20' : 'Blackstar Shard',
    '12276-4' : 'TET Deboreka Belt',
    '12276-5' : 'PEN Deboreka Belt',
    '11653-5' : 'PEN Deboreka Necklace',
    '719897-4' : 'TET Labreska Helmet'
    }

WaitList = ['','','','','']

while(1):
    try:
        response = requests.request('POST', url, json=payload, headers=headers)
        time_now = datetime.now(timezone).strftime("%H:%M:%S")
        print(response.text," ",time_now)
        str = response.text

        for i in BlackstarDict:
            if str.find(i) != -1:
                duplicate = False
                start = str.find(i)
                end = str[start:].find("|")
                item = str[start:start+end]

                id, enhancement, price , reg = item.split("-")
                reg = datetime.fromtimestamp(int(reg),timezone).strftime("%H:%M:%S")
                print(id,enhancement,price,reg)
                print(BlackstarDict[i], " Listed at ", reg)

                for j in WaitList: #compare waitlist, to not send duplicate
                        if item == j:
                            duplicate = True

                if duplicate == False:
                    #Send Message to Discord
                    message = "< Discord User ID > " + BlackstarDict[i] + ", Price: " + price + ", Listing at: " + reg    # <<<<<<<<<<<<<<<<<<<<< Change your ID
                    payload = {"content": message}
                    r = requests.post(discordBot,data=json.dumps(payload),headers=headers)

                WaitList.append(item)
                WaitList.pop(0)

        time.sleep(60)
    except:
        print("error")
        time.sleep(60)

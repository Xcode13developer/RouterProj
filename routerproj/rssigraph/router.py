import datetime
from time import sleep
from netmiko import ConnectHandler
from background_task import background
from rssigraph.models import Point

device = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.3',
    'username': 'dev',
    'password': 'dev123',
    'secret': 'dev',
}

conn = ConnectHandler(**device)

def getData():
    output = conn.send_command("sh cell 0/1/0 ra de")
    list_of_words = output.split()
    RSSI = list_of_words[list_of_words.index("RSSI") + 2]
    RSRP = list_of_words[list_of_words.index("RSRP") + 2]
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    xPerHour = "%i.%i" % (minute, second)
    point = Point(xPerHour=xPerHour, RSSIy=RSSI, RSRPy=RSRP, date="%d / %d . %d" % (month, day, hour))
    point.save()
    print(RSSI, RSRP)

@background
def store():
    while True:
        getData()


 

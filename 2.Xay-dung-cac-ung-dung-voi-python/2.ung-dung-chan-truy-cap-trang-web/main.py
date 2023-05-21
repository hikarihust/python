import time
from datetime import datetime as dt

# hosts_file  = r"/private/etc/hosts"
hosts_file  = r"host.txt"
local       = "127.0.0.1"
website_list=[
    "www.facebook.com",
    "facebook.com",
    "www.twitter.com",
    "twitter.com"
]

timeCurrent     = dt.now()
timeWorkStart   = dt(timeCurrent.year,timeCurrent.month, timeCurrent.day, 21)
timeWorkEnd     = dt(timeCurrent.year, timeCurrent.month, timeCurrent.day, 23)

if timeWorkStart < timeCurrent < timeWorkEnd:
    with open(hosts_file,'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(local+" "+ website+"\n")
else:
    with open(hosts_file,'r+') as file:
        content = file.readlines()
        file.seek(0)
        file.truncate()
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)


# while True:
#     print("Hello")
#     time.sleep(5)

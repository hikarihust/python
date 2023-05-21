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
    print("lam viec")
else:
    print("nghi ngoi")


# while True:
#     print("Hello")
#     time.sleep(5)

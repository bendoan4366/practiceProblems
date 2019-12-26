import time
from datetime import datetime as dt
import fileinput

host_path = "C:\Windows\System32\drivers\etc\hosts"
#temp path for testing
#host_path = r"C:\Users\kndoa\OneDrive\Desktop\Data Science\PythonPractice\AddBlocker\hosts"
redirect = "127.0.0.1"

website_list = ["myspace.com", "www.myspace.com", "barstoolsports.com", "www.barstoolsports.com"]

while True:
    if dt.now().hour > 9 and dt.now().hour < 17:
        print("Inside the time window!")
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Outside the time window!")
        with open(host_path, "r+") as file:
            line_content = file.readlines()
            file.seek(0)

            for line in line_content:
                if not any(website in line for website in website_list):
                    file.write(line)
                else:
                    pass
            file.truncate()

    time.sleep(5)

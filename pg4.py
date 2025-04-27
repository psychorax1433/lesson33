import random
import time
def getRandomDate(start_date, end_date):
    print("Random date between", start_date, "and", end_date)
    date_format = "%m/%d/%Y"
    start_time = time.mktime(time.strptime(start_date, date_format))
    end_time = time.mktime(time.strptime(end_date, date_format))
    random_time = start_time + random.random() * (end_time - start_time)
    random_date = time.strftime(date_format, time.localtime(random_time))
    return random_date
print("Random Date =", getRandomDate("01/02/2024", "02/01/2025"))
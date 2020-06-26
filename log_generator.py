# item_id, timestamp, device_type, device_id, user_ip, review_title, review_text, review_stars

from datetime import date, timedelta, datetime
from random import randrange
from time import mktime, strftime, strptime

start_date = date(2020, 6, 23)
end_date = date(2020, 6, 26)

log_file = strftime("/var/log/dkulemza/capstone/%Y%m%d-%H%M%S.log")

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

while datetime.now().minute < datetime.now().minute + 5:

    random_number_of_days = randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    random_IP = "37.57.12.{0}".format(randrange(10, 200))
    random_review_stars = randrange(0, 6)
    random_id = randrange(0, 150)

    timestamp = mktime(strptime(str(random_date), '%Y-%m-%d'))

    log = 'item_id: {0}, timestamp: {1}, ' \
          'device_type: {2}, device_id: {0}, ' \
          'user_ip: {3}, review_title: {4}, ' \
          'review_text: {5}, review_stars: {6}'.format(random_id, int(timestamp), (random_id / 2) + 1, random_IP, "About this device", "Revision", random_review_stars)

    with open(log_file, "w") as f:
        f.write(log)

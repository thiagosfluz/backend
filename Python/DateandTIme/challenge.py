import datetime
import pytz


while True:

    for j in range(10):
        print(pytz.all_timezones[j])


    print("Choose up to 9 timezones: ", end='')
    timezone_chosen = input()

    if timezone_chosen in pytz.all_timezones:
        tz_to_display = pytz.timezone(timezone_chosen)
        local_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}: ".format(timezone_chosen.split("/")[0], local_time.strftime('%A %x %X %z'), local_time.tzname()))
        print("The UTC time is {}: ".format(datetime.datetime.utcnow().strftime("%A %x %X")))
        print("The local time is {}: ".format(datetime.datetime.now().strftime("%A %x %X")))
    elif timezone_chosen == '0':
        break
    else:
        print("Incorrect time zone, type again")
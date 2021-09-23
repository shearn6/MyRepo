from datetime import datetime

def time_stamp():
    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')
    return date

time = time_stamp()
print(time)
# %Y= 4 digit year
# %m= 2 digit month
# %d= 2 digit day
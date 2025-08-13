from datetime import datetime

import pytz


data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America"))

print(data)


####### Versão sem o pytz
from datetime import datetime, timezone, timedelta


data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sp = datetime.now(timezone(timedelta(hours=-3), 'BR'))

print(data_oslo)
print(data_sp)
from datetime import datetime, timedelta

# 1

currentDate = datetime.today()
dateBefore = currentDate - timedelta(days=5)

print(dateBefore)

# 2

yesterday = currentDate - timedelta(days=1)
tomorrow = currentDate + timedelta(days=1)
print(f"Yesterday: {yesterday}\nToday: {currentDate}\nTomorrow: {tomorrow}")

# 3

currentDate2 = currentDate.replace(microsecond=0)
print(currentDate2)

# 4

secDiff = (tomorrow - yesterday).total_seconds()
print(secDiff)

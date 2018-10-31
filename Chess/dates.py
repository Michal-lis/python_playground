from datetime import date, timedelta

startDate = date(2018, 4, 27)
endDate = date(2018, 5, 7)

timedelta = timedelta(days=1)
print(startDate)
current_date = startDate
while current_date < endDate:
    current_date = current_date + timedelta
    print(current_date)
print(endDate)

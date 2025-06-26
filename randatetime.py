import random
import time
def getRandomDate(startDate, endDate):
    print("printing random date between", startDate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%y'
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = startTime + (endTime - startTime) * randomGenerator
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print("randomDate", getRandomDate('01/01/20', '12/31/20'))

import sys

class Clock():
    def __init__(self):
        self.hour = 12
        self.minute = 00
    
    def incrementTime(self):
        if self.minute == 59:
            self.minute = 00
            if self.hour == 12:
                self.hour = 1
            else:
                self.hour += 1
        else:
            self.minute += 1

    def printClockTime(self):
        print("{}:{:02d}".format(self.hour, self.minute))

class Solution(object):
    def getTimeList(self, hour, minute, fourDigit):
        if fourDigit:
            return [int(hour/10), hour%10, int(minute/10), minute%10]
        else:
            return [hour, int(minute/10), minute%10]

    def calculateTimes(self):
        clock = Clock()
        clock.incrementTime()
        times = []
        while not(clock.hour == 12 and clock.minute == 00):
            if clock.hour < 10:
                clockList = self.getTimeList(clock.hour, clock.minute, False)
                if clockList[0] - clockList[1] == clockList[1] - clockList[2]:
                    times.append(clockList)
            else:
                clockList = self.getTimeList(clock.hour, clock.minute, True)
                if clockList[0] - clockList[1] == clockList[1] - clockList[2] == clockList[2] - clockList[3]:
                    times.append(clockList)
            clock.incrementTime()
        return times

    def favouriteTimes(self, timePassed):
        """
        :type timePassed: int
        :rtype: int
        """
        timeList = self.calculateTimes()
        count = 0

        count += len(timeList) * int(timePassed/(12*60))
        timeRemaining = timePassed%(12*60)

        clock = Clock()
        for i in range(timeRemaining):
            if clock.hour < 10:
                clockList = self.getTimeList(clock.hour, clock.minute, False)
                if clockList in timeList:
                    count += 1
            else:
                clockList = self.getTimeList(clock.hour, clock.minute, True)
                if clockList in timeList:
                    count += 1
            clock.incrementTime()
        
        return count

if len(sys.argv) < 2:
    print("Enter a file to test as command line argument")
else:
    filename = sys.argv[1]
    if ('/' not in filename):
        filename = 'j4/' + filename
    with open(filename) as file:
        time = file.readlines()
    time = int(time[0])
    main = Solution()
    print(main.favouriteTimes(time))

        
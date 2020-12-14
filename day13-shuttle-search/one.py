
def main():
    with open('input.txt') as file:
        time = int(file.readline())
        busses = file.readline().split(",")
    busses = filter(lambda bus: bus != "x", busses)
    busses = list(map(lambda bus: int(bus), busses))
    print(solve(time, busses))

def solve(time, busses):
    earliestTime = -1
    earliestBus = 0
    for bus in busses:
        departure = (time // bus) * bus
        if (departure < time):
            departure += bus
        waitTime = departure - time
        if (earliestTime == -1 or waitTime < earliestTime):
            earliestTime = waitTime
            earliestBus = bus
        
    return earliestBus * earliestTime   



main()
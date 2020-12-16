
def main():
    with open('input.txt') as file:
        fieldsData, yourTicketData, nearbyTicketsData = file.read().split("\n\n")
    fields = getFields(fieldsData)
    yourTicket = getYourTicket(yourTicketData)
    nearbyTickets = getNearbyTickets(nearbyTicketsData)
    
    # print(fields, yourTicket, nearbyTickets)
    print(solve(fields, nearbyTickets))

def solve(fields, nearbyTickets):
    errorRate = 0
    for nearbyTicket in nearbyTickets:
        for value in nearbyTicket:
            if (not isValid(fields, value)):
                errorRate += value
    return errorRate

def isValid(fields, value):
    isValid = False
    for fieldName in fields:
        [fieldMin1, fieldMax1, fieldMin2, fieldMax2] = fields[fieldName]
        if (fieldMin1 <= value and value <= fieldMax1 or fieldMin2 <= value and value <= fieldMax2):
            isValid = True
            break
    return isValid            

def getFields(fieldsData):
    fields = {}
    for fieldData in fieldsData.split("\n"):
        fieldName, fieldRanges = fieldData.split(": ")
        fieldRange1, fieldRange2 = fieldRanges.split(" or ")
        fieldMin1, fieldMax1 = [int(value) for value in fieldRange1.split("-")]
        fieldMin2, fieldMax2 = [int(value) for value in fieldRange2.split("-")]
        fields[fieldName] = [fieldMin1, fieldMax1, fieldMin2, fieldMax2]
    return fields

def getYourTicket(yourTicketData):
    return getTicket(yourTicketData.replace("your ticket:\n", ""))

def getNearbyTickets(nearbyTicketData):
    nearbyTicketData = nearbyTicketData.replace("nearby tickets:\n", "").split("\n")
    return [getTicket(ticketData) for ticketData in nearbyTicketData]
    
def getTicket(ticketData):
    return [int(value) for value in ticketData.split(",")]

main() 

def main():
    with open('input.txt') as file:
        fieldsData, yourTicketData, nearbyTicketsData = file.read().split("\n\n")
    fields = getFields(fieldsData)
    yourTicket = getYourTicket(yourTicketData)
    nearbyTickets = getNearbyTickets(nearbyTicketsData)    
    print(solve(fields, yourTicket, nearbyTickets))

def solve(fields, yourTicket, nearbyTickets):
    validTickets = getValidTickets(fields, nearbyTickets)
    possibleFieldsDict = getPossibleFieldsDict(fields, validTickets) 
    fieldTranslations = getFieldTranslations(possibleFieldsDict)
    
    product = 1
    for fieldTranslation, column in fieldTranslations.items():
        if (fieldTranslation.startswith("departure")):
            product *= yourTicket[column]

    return product

def getValidTickets(fields, nearbyTickets):
    validTickets = []
    for nearbyTicket in nearbyTickets:
        isValidTicket = True
        for value in nearbyTicket:
            if (not isValidValue(fields, value)):
                isValidTicket = False
                break
        if (isValidTicket):
            validTickets.append(nearbyTicket)
    return validTickets

def getPossibleFieldsDict(fields, tickets):
    possibleFieldsDict = {}
    columnsCount = len(tickets[0])
    for column in range(columnsCount):
        ticketValues = [nearbyTicket[column] for nearbyTicket in tickets]
        possibleFieldsDict[column] = getPossibleFieldsForColumn(fields, ticketValues)
    return possibleFieldsDict

def getPossibleFieldsForColumn(fields, ticketValues):
    possibleFields = [fieldName for fieldName in fields.keys()]
    for value in ticketValues:
        for fieldName in possibleFields:
            if (not isInRanges(fields[fieldName], value)):
                possibleFields.remove(fieldName)
    return possibleFields

def getFieldTranslations(possibleFieldsDict):
    fieldTranslations = {}
    
    while len(possibleFieldsDict.keys()) > 0:
        for column, possibleFields in possibleFieldsDict.items():
            if (len(possibleFields) == 1):
                foundField = possibleFields[0]
                fieldTranslations[foundField] = column
                possibleFieldsDict.pop(column)
                for c in possibleFieldsDict.keys():
                    possibleFieldsDict[c].remove(foundField)
                break

    return fieldTranslations

def isValidValue(fields, value):
    isValid = False
    for fieldName in fields:
        if (isInRanges(fields[fieldName], value)):
            isValid = True
            break
    return isValid          

def isInRanges(ranges, value):
    [fieldMin1, fieldMax1, fieldMin2, fieldMax2] = ranges
    return fieldMin1 <= value and value <= fieldMax1 or fieldMin2 <= value and value <= fieldMax2

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
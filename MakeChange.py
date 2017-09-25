
# It is assumed that the MoneyArray is ordered from highest value to the lowest value floats.

def MakeChange(DesiredChange, MoneyArray):
    if MoneyArray == None:
        raise Exception ("Money array must not be null")
    if len(MoneyArray) == 0:
        raise Exception ("Money array must be populated")

    rtnChange = []
    runningValue = int(DesiredChange * 100)

    for coin in MoneyArray:
        coinValue = int(100 *  coin[1])
        tokens = runningValue / coinValue
        rtnChange.append ( (coin[0], tokens) )
        runningValue -= tokens * coinValue
    return rtnChange

UsMoney = [ ('Dollar', 1), ('Half-Dollar', 0.5), ('Quarter', 0.25), ('Dime', 0.1), ('Nickel', 0.05), ('Penny', 0.01) ]
print "UsMoney", UsMoney

# MakeChange(7,None)
# MakeChange(7,[])
ExpectedResult = [ ('Dollar', 1), ('Half-Dollar', 0.5), ('Quarter', 0.25), ('Dime', 0.1), ('Nickel', 0.05), ('Penny', 0.01) ]
print "ExpectedResult", ExpectedResult

ActualResult = MakeChange( 3.87, UsMoney )
print "ExpectedResult for 3.87"  , ActualResult

warning = ""

def printWarningMessage(message, alert = False):
    global warning
    if alert == True:
        print(message)

def validateInputPositiveInt(*data, warn = False):
    global warning

    if data == None:
        return None
        warning = "At least one positive integer is needed."
    elif not isinstance(data, int):
        return False
        warning = "The following argument is not an integer: " + str(data) + "."
    elif data == 0:
        warning = "Only positive integers are allowed. The value is zero."
        print(warning)
    elif data < 0:
        return False
        warning = "Only positive integers are allowed. The value is negative"
        print(warning)
    else:
        return True
        warning = "The data is a positive integer higher than 0 (zero)"
        print(warning)

    if warn == True:
        printWarningMessage(message = warning, alert = True)

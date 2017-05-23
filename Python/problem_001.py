import validator as v

def SumOfMultiples(number1 = 0, number2 = 0, limit = 10):
    counter = 0
    result = 0

    if v.validateInputPositiveInt(number1 and number2) == None or v.validateInputPositiveInt(number1 and number2) == 0 or v.validateInputPositiveInt(number1, number2, limit) == False:
        v.validateInputPositiveInt(warn = True)

    else:
        pass
        # while counter <= limit:
        #     if counter % number1 == 0:
        #         result = result + counter
        # return result

SumOfMultiples(1, "ab")

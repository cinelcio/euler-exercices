from tools import validator as v

class SumOfDivisibles(object):

    def SumDivisiblesBy(number1, number2 = None, until = 10):
        counter = 0
        result = 0

        if v.Validator.validatePositiveInt(number1) == False or v.Validator.validatePositiveInt(number2) == False:
            print(v.warning)
            pass
        elif v.Validator.validateMinimalInt(number1, until) == False or v.Validator.validateMinimalInt(number2, until) == False:
            print(v.warning)
        elif v.Validator.validatePositiveInt(number1) == True and v.Validator.validatePositiveInt(number2) == None:
            for number in range(until  ):
                if counter % number1 == 0:
                    result = result + counter
                counter += 1

        else:
            for number in range(until):
                # For variable Debug
                # print("variable number: " + str(number))
                # print("variable counter: " + str(counter))
                # print("variable result: " + str(result))
                if counter % number1 == 0 or counter % number2 == 0:
                    result = result + counter
                counter += 1
        return result

    print("Solution for Euler Problem 001: " + SumDivisiblesBy(3, 5, 1000))

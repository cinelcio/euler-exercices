if __name__ == '__main__':
    import validator as v
else:
    from tools import validator as v

class FiboCounter():

    def __init__(self):
        pass

    def CountFibonacciSequence(self, highestvalue = 10, showlist = False):
        counter = 0
        result = 0
        transfer = 1
        previous = 0
        resultlist = []
        f = FiboCounter()
        validatenumber = v.Validator().validatePositiveInt(data = highestvalue)

        if validatenumber == False:
            return validatenumber

        else:
            previous = 0
            while counter < highestvalue:
                counter += 1
                previous = transfer + result
                result = transfer
                transfer = previous
                resultlist.append(result)
                # print("For position " + str(counter)+ " the result is: " + str(result))
            if showlist == True:
                return resultlist
        return result


    def GetResultByNearValue(self, proximatevalue, showlist = False):
        '''
        This method should get the argument "proximatevalue" and return the fibonacci high below the value.
        '''
        f = FiboCounter()

        # value = 0
        for value in range(proximatevalue):
            final = self.CountFibonacciSequence(highestvalue = value)
            fibonaccilist = self.CountFibonacciSequence(highestvalue = value, showlist = True)
            check = value
            if final > proximatevalue and showlist == True:
                return fibonaccilist[:value - 1]
                break
            elif final > proximatevalue and showlist == False:
                return fibonaccilist[value - 2]
                break
            else:
                continue
                

    def GetResultByPosition(self, position):
        '''
        This method should return the fibonacci number in the position given. The first result is 1, the second is 1, the third is 2, the fourth is 5 and so on.
        '''
        f = FiboCounter()
        if v.Validator.validatePositiveInt(position) == False:
            print(v.warning)
        else:
            pass

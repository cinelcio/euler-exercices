if __name__ == '__main__':
    import validator as v
else:
    from tools import validator as v

class FiboCounter():

    def CountFibonacciSequence(self, limit = 10, showresults = False):
        counter = 0
        result = 0
        transfer = 1
        previous = 0
        resultlist = []

        if v.Validator.validatePositiveInt(limit) == False:
            print(v.warning)
        else:
            previous = 0
            while counter < limit:
                counter += 1
                previous = transfer + result
                result = transfer
                transfer = previous
                resultlist.append(result)
                # print("For position " + str(counter)+ " the result is: " + str(result))
            if showresults == True:
                return resultlist
        return result


    def GetResultByProximate(self, proximate, showresults = False):
        '''
        This method should get the argument "proximate" and return the fibonacci high below the value.
        '''

        if v.Validator.validatePositiveInt(proximate) == False:
            print(v.warning)
        else:
            for value in range(proximate):
                if self.CountFibonacciSequence(limit = value) > proximate:
                    if showresults == True:
                        self.CountFibonacciSequence(limit = value, showresults = True)
                    else:
                        return self.CountFibonacciSequence(limit = value)
                else:
                    continue


    def GetResultByPosition(position):
        '''
        This method should return the fibonacci number in the position given. The first result is 1, the second is 1, the third is 2, the fourth is 5 and so on.
        '''
        if v.Validator.validatePositiveInt(position) == False:
            print(v.warning)
        else:
            pass

    GetResultByProximate(proximate = 20)

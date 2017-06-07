if __name__ == '__main__':
    import validator as v
else:
    from tools import validator as v
import csv


class PrimeVerifier():

    def __init__(self):
        pass

    def ReadSolutionsFound(self):
        p = PrimeVerifier()
        with open('primesfound.csv', newline='\n') as csvfile:
            knowprimes = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in knowprimes:
                print(', '.join(row))

    def CheckBasicRulesr(self, number):
        pass
        # validatenumber = v.Validator().validatePositiveInt(number)
        #
        # if validatenumber == False or validatenumber == None:
        #     return validatenumber


p = PrimeVerifier().ReadSolutionsFound()

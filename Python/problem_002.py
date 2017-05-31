from tools import fibonacci

class SumOfFiboEven(object):

    def __init__(self):
        pass

    def SumAllTheEvens(self, endcounter):
        f = fibonacci.FiboCounter()
        sequence = f.GetResultByNearValue(proximatevalue = endcounter, showlist = True)
        # print(sequence)
        sumEvens = 0
        for position in range(len(sequence)):
            if sequence[position] % 2 != 0:
                sumEvens = sumEvens + sequence[position]
        return sumEvens

s = SumOfFiboEven()
print("Solution for Euler Problem 002: " + str(s.SumAllTheEvens(4000000)))

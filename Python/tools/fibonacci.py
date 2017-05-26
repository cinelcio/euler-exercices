from tools import validator as v

class FiboCounter(object):
    result = 0
    counter = 0

    def SetPostion(number, limit = 10):
        global result
        if v.Validator.validatePositiveInt(number) == False or v.Validator.validateMinimalInt(number) == None:
            print(v.warning)
        else:
            continue


    def SetHighest(number, limit = 150):
        global result
        if v.Validator.validatePositiveInt(number) == False or v.Validator.validateMinimalInt(number) == None:
            print(v.warning)
        else:
            continue

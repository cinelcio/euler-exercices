class Validator():
    '''
    This validator checks the value passed. It says if it is an positive integer higher than 0 (zero) and if a value passed as the limit for any counter is indeed higher than the first multiplier of the counter.
    '''

    warning = ""


    def __init__(self): pass

    def validatePositiveInt(self, data, warn = False):
        ''' Here is checked if the value passed is an positive integer higher than 0 (zero). If warn is set to True it also returns the value in 'warning', which contains a brief explaination of why the result was given. '''

        v = Validator()

        if data == None:
            self.warning = "Argument is empty."
            if warn == True:
                print(self.warning)
            return None
        elif not isinstance(data, int):
            self.warning = "The following argument is not an integer: " + str(data) + "."
            if warn == True:
                print(self.warning)
            return False
        elif data == 0:
            self.warning = "The argument value is 0 (zero)."
            if warn == True:
                print(self.warning)
            return None
        elif data < 0:
            self.warning = "Only positive integers are allowed. " + str(data) + " is negative."
            if warn == True:
                print(self.warning)
            return False
        else:
            self.warning = "The data is a positive integer higher than 0 (zero)."
            return True

        # if warn == True:
        #     print(self.warning)


    def validateMinimalInt(self, value, minimal, warn = False):
        '''
        Here is checked if the value passed is higher thant the minimal, also passed. as an argument. If warn is set to True it also returns the value in 'warning', which contains a brief explaination of why the result was given.
        '''
        v = Validator()
        if self.validatePositiveInt(value) == False or self.validatePositiveInt(minimal) == False:
            return warning
        elif value > minimal:
            self.warning = "Arguments must be below the limit. Put them below " + str(minimal) + " or increase limit."
            if warn == True:
                print(self.warning)
            return False
        elif value == minimal:
            self.warning = "The first value should not be equal to the minimal choosen."
            if warn == True:
                print(self.warning)
            return False
        else:
            return True

        # if warn == True:
        #     return self.warning

if __name__ == '__main__':
    v = Validator()

    print("Module Health Check:")
    v.validatePositiveInt(data = -1, warn = True)
    v.validatePositiveInt("ab", warn = True)
    v.validatePositiveInt(0, warn = True)
    print(v.validatePositiveInt(3, warn = True))
    v.validateMinimalInt(15, 10, warn = True)
    v.validateMinimalInt(10, 10, warn = True)
    print(v.validateMinimalInt(5, 10, warn = True))

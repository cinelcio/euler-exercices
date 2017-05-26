class Validator():
    '''
    This validator checks the value passed. It says if it is an positive integer higher than 0 (zero) and if a value passed as the limit for any counter is indeed higher than the first multiplier of the counter.
    '''

    warning = ""

    def validatePositiveInt(data, warn = False):
        '''
        Here is checked if the value passed is an positive integer higher than 0 (zero).
        If warn is set to True it also returns the value in 'warning', which contains a brief explaination of why the result was given.
        '''

        global warning
        warning = ""

        if data == None:
            warning = "Argument is empty."
            return None
        elif not isinstance(data, int):
            warning = "The following argument is not an integer: " + str(data) + "."
            return False
        elif data == 0:
            warning = "The argument value is 0 (zero)."
            return False
        elif data < 0:
            warning = "Only positive integers are allowed. " + str(data) + " is negative."
            return False
        else:
            warning = "The data is a positive integer higher than 0 (zero)."
            return True

        if warn == True:
            return warning


    def validateMinimalInt(value, minimal, warn = False):
        '''
        Here is checked if the value passed is higher thant the minimal, also passed. as an argument. If warn is set to True it also returns the value in 'warning', which contains a brief explaination of why the result was given.
        '''

        global warning

        if Validator.validatePositiveInt(value) == False or Validator.validatePositiveInt(minimal) == False:
            pass
        elif value > minimal:
            warning = "Arguments must be below the limit. Put them below " + str(minimal) + " or increase limit."
            return False
        elif value == minimal:
            warning = "The first value should not be equal to the minimal choosen."
            return False
        else:
            return True

        if warn == True:
            return warning

if __name__ == '__main__':
    print("Module Health Check:")
    print(Validator.validatePositiveInt(-1, warn = True))
    print(Validator.validatePositiveInt("ab", warn = True))
    print(Validator.validatePositiveInt(3, warn = True))
    print(Validator.validatePositiveInt(0, warn = True))

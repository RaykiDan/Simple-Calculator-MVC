class ModelCalculator:

    @classmethod
    def plus(cls, var1, var2):
        return var1 + var2

    @classmethod
    def minus(cls, var1, var2):
        return var1 - var2

    @classmethod
    def multiply(cls, var1, var2):
        return var1 * var2

    @classmethod
    def divide(cls, var1, var2):
        return round(var1 / var2, 2)

    @classmethod
    def larger(cls, var1, var2):
        if var1 > var2:
            return var1
        elif var2 > var1:
            return var2
        else:
            return 'Equal'

    @classmethod
    def smaller(cls, var1, var2):
        if var1 < var2:
            return var1
        elif var2 < var1:
            return var2
        else:
            return 'Equal'

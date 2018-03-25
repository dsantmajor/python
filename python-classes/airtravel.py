"""Model for aircraft flights """

class Flight:
    # def number(self):
    #     return "S40315"
    # Below is the initializer method
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("No airline code in {}".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid Airline code {}".format(number))
        self._number = number
        if not number[2:].isdigit():
            raise ValueError("Invalid route number {}".format(number))
    def number(self):
        return self._number
    def airlinecode(self):
        return self._number[:2]
    def routenumber(self):
        return self._number[2:]
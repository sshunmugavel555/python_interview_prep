""" Module that has all the employee specific classes """

class Employee:
    """ Class that models an employee class """

    def __init__(self,fn,ln,sal) -> None:
        """ Initialize instance vars """
        self.fn=fn
        self.ln=ln
        self.sal=sal

    def give_raise(self,delta=5_000):
        """ Method to give raise to salary """
        if delta>=0:
            self.sal += delta
        else:
            print(f"Raise in sal cannot be negative ")
    
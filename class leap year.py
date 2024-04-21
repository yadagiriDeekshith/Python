class LeapYearCheck:
    def __init__(self,year):
        self.year=year
    def is_leap(self):
        if (self.year % 4==0 and self.year % 100 != 0)or(self.year % 400==0):
            return True
        else:
            return False
year=int(input("Enter a year"))
leap_check=LeapYearCheck(year)
if leap_check.is_leap():
    print("True")
else:
    print("False")

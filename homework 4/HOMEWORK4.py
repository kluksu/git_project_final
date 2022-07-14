import inspect
from typing import Type

def is_Meuberet(year:int) -> bool:
    """
    recieves an int that describe a year, if devided by 4 then retrun true, else return false
    :param year:
    :return:
    """
    return True if (year % 4 == 0  and year % 100!=0) or year%400==0 else False


class Date:
    def __init__(self,day:int,month:int,year:int):
        """

        :param day:
        :param month:
        :param year:
        """
        if day<1 or day>31:
            raise ValueError ("value of day must be int in range 1-31")
        elif month<1 or month>12:
            raise ValueError("value of month must be int in  range of 1-12")
        elif year<1000 or year>9999:
            raise ValueError("value of year must be an int in range of 1000-9999")
        self._day=day
        self._month=month
        self._year=year
        self.months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    def __str__(self)->str:
        """
        retruns a string representation of class instance
        :return:
        """
        return f"{self._day,self._month,self._year}"
    def isValid(self, current_day:int=0, current_month:int=0, current_year:int=0 ) -> bool:
        """
        can be used for checking if a date is valid on this instance by default or on
        a selected date in format of dd,mm,yyyy
        :param current_day:
        :param current_month:
        :param current_year:
        :return:
        """
        current_day=current_day if current_day!=0 else self._day
        current_month=current_month if current_month!=0 else self._month
        current_year= current_year if current_year!=0 else self._year
        isMeuberet= is_Meuberet(current_year)
        meuberet_lastDay= isMeuberet==True and current_month==2 and current_day<=29
        for value in current_day, current_month, current_year:
            if not isinstance(value,int):
                return False
        if (current_day>=1 and current_month<=12 and current_day<=self.months[current_month] ) \
                or ( meuberet_lastDay ):
            return (True)
        else:
            return (False)
    def get_next_day(self)->"Date":
        """
        retruns the next day
        :return:
        """
        current_day, current_month, current_year,months = vars(self).values()
        if(self.isValid(current_day, current_month, current_year)):
             if(self.isValid(current_day+1,current_month,current_year)==True):
                 return Date(current_day+1, current_month, current_year)
             elif (self.isValid(1,current_month+1,current_year)==True):
                 return Date(1,current_month+1,current_year)
             else:
                 return Date(1, 1, current_year+1)
        else:
            raise ValueError("date that was given is not valid")
    def dateToDays(self)->int:
        """
        returns an int that represent days to count from beggining of time (used latter in other functions)
        :return:
        """
        years_total = 0
        months=self.months
        months[2]=28 if is_Meuberet(self._year)!=True else 29
        months_total=0
        days_total=0
        for year in range(0,self._year,1):
            days_in_year = 365 if is_Meuberet(year)!=True else 366
            years_total=years_total+days_in_year
        for month in range(1,self._month):
            days_in_month = months[month]
            months_total=months_total+days_in_month

        for day in range(1,self._day):
            days_total=days_total+1
        total=months_total+years_total+days_total
        return total
    def get_next_days(self,days_to_add:int)->"Date":
        """
        take an int as number of days and returns a date in number of days from current date instance
        :param days_to_add:
        :return:
        """
        total_days=days_to_add
        months = self.months
        current_year=self._year
        months[2] = 28 if is_Meuberet(current_year) != True else 29
        current_year=self._year
        while total_days>366:
                days_in_year = 365 if is_Meuberet(current_year) != True else 366
                total_days=total_days-days_in_year
                current_year=current_year+1
        day,month,year=self._day,self._month,current_year
        months[2] = 28 if is_Meuberet(year) != True else 29
        if months[month]<day:
            day=day-months[month]
            month=month+1
            if month == 13:
                year=year+1
                month=1
        new_day = Date(day,month,year)
        while total_days>0:
                new_day= (new_day.get_next_day())
                total_days=total_days-1
        return (new_day)
    def __gt__(self,other:Type["Date"])->bool:
     """
     recives another date, returns true if current date is grater, retruns false if current date is smaller
     :param other:
     :return:
     """
     if(self._year>other._year):
         return True
     elif self._year==other._year and self._month>other._month:
         return True
     elif self._year==other._year and self._month==other._month and self._day>other._day:
         return True
     else:
         return False
    def __eq__(self, other:Type["Date"])-> bool:
        """
        recives another date and retruns true of both dates are the same, returns false if they are not
        :param other:
        :return:
        """
        if self.__gt__(other)==False and self._day==other._day and\
                self._month==other._month and self._year==other._year:
            return True
        else:
            return False
    def __ge__(self,other:Type["Date"])->bool:
       """

       :param other:
       :return:
       """
       if self.__gt__(other) or self.__eq__(other):
           return True
       else:
           return False
    def __lt__(self, other:Type["Date"])->bool:
        """
        recieves another date and retrun true if current date is less then other date
        :param other:
        :return:
        """
        if self.__gt__(other)==False and self.__eq__(other)==False:
            return True
        else:
            return False
    def __le__(self, other:Type["Date"])->bool:
        if self.__lt__(other) or self.__eq__(other):
            return True
        else:
            return False
    def __sub__(self, other: Type["Date"]) -> int:
        """
        recieves another date and retruns the number of days between the two dates
        :param other:
        :return:
        """
        sub=self.dateToDays()-other.dateToDays()
        return sub if sub>=0 else -sub







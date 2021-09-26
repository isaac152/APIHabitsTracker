from datetime import date,timedelta
from datetime import datetime
from collections import OrderedDict

class DateList:
    def __init__(self):
        self.dates = OrderedDict()
        
    def str_to_date(self,date_string:str):
        return datetime.strptime(date_string,'%Y-%m-%d').date()
    def mark_today(self):
        self.dates.update({f"{date.today()}":True})

    def unmark_today(self):
        try:
            self.dates.pop(f"{date.today()}")
        except KeyError:
            print('Not found today date')

    def edit_dates(self,dates):
        self.dates.update(dates)
        self.remove_undone()
        self.dates=OrderedDict(sorted(self.dates.items()))

    def remove_undone(self):
        new_order_dict=self.dates.copy()
        for k,v in new_order_dict.items():
            if(v==False):
                try:
                    self.dates.pop(k)
                except:
                    print('error')

    def get_all_week(self,date:str):
        dates = self.str_to_date(date)
        day = dates.isocalendar()[2]
        cont=0
        week = [str(dates+timedelta(days=i)) for i in range(0-day,7-day)]
        for k in self.dates:
            if(k in week):
                cont+=1
        return cont
    
    def get_all_month(self,date:str):
        dates = self.str_to_date(date)
        cont=0
        month = str(dates.month)
        for k in self.dates:
            if(k[5:7]==month):
                cont+=1
        return cont

    def get_all_year(self,date:str):
        dates=self.str_to_date(date)
        cont=0
        year = str(dates.year)
        for k in self.dates:
            if(k[:4]==year):
                cont+=1
        return cont

    def update_dates(self,list_dates):
        for i in list_dates:
            date={i:True}
            self.dates.update(date)

class Score:
    
    def __init__(self,days=7):
        self.days=days

    def max_score(self,result):
        if(result>1):
            return 1
        return result

    def weekly_score(self,date:str):
        result= self.listDates.get_all_week(date)/self.days
        return self.max_score(result)

    def monthly_score(self,date:str):
        result= self.listDates.get_all_month(date)/(self.days*4.4)
        return self.max_score(result)

    def year_score(self,date:str):
        result=self.listDates.get_all_year(date)/(self.days*52)
        return self.max_score(result)        


class Habit:
    name:str
    description:str
    #repetition by week
    days:int

    def __init__(self,**kwargs):
        self.name=kwargs.get('name')
        self.description=kwargs.get('description')
        self.days=kwargs.get('days')
        self._id=kwargs.get('_id')
        if(not self.days):
            self.days=7
        self.date=DateList()
        dates=kwargs.get('Marks')
        if(dates):
            self.date.update_dates(dates)
    def __str__(self):
        return  f'{self.name} recurrencia: {self.days}'

    def changes(self,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
        

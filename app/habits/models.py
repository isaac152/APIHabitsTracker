from datetime import date,timedelta
from datetime import datetime
from collections import OrderedDict


class DateList:
    def __init__(self):
        self.dates = OrderedDict()
        
    def str_to_date(self,date:str):
        return datetime.strptime(date,'%Y-%m-%d').date()
    def mark_today(self):
        self.dates.update({f"{date.today()}":1})

    def unmark_today(self):
        self.dates.pop(f"{date.today()}")
    
    def edit_dates(self,dates):
        format_dates=self.format_dates(dates)
        self.dates.update(format_dates)
        self.remove_undone()
        self.dates=OrderedDict(sorted(self.dates.items()))
    
    def format_dates(self,dates):
        new_dic=dates.copy()
        list_dates=[i for i in dates]
        for i in list_dates:
            datetime_aux=datetime.strptime(i,"%Y-%m-%d")
            new_dic[i]=new_dic[datetime_aux.strftime("%Y-%m-%d")]
            del new_dic[i]
        return new_dic

    def remove_undone(self):
        new_order_dict=self.dates.copy()
        for k,v in new_order_dict.items():
            if(v==0):
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
    
class Score:
    
    def __init__(self,listDates,days=7):
        self.days=days
        self.listDates:DateList=listDates        

    def max_score(self,result):
        if(result>1):
            return 1
        return result

    def weekly_score(self,date:str):
        result= self.listDates.get_all_week(date)/self.days
        return self.max_score(result)

    def monthly_score(self,date:str):
        result= self.listDates.get_all_month(date)/(self.days*4)
        return self.max_score(result)

    def year_score(self,date:str):
        result=self.listDates.get_all_year(date)/(self.days*52)
        return self.max_score(result)
    

class ScoreList:
    def __init__(self):
        self.score=OrderedDict()

    def update_actual_score(self,score:Score):
        today=date.today()
        today_str=str(today)
        year=str(today.year)
        week = today.isocalendar()[1]
        week_score=score.weekly_score(today)
        self.score[year].update({week:week_score})

    def update_scores(self,score:Score,dates):
        list_dates=[i for i in dates]
        for date in list_dates:
            week = score.listDates.str_to_date(date).isocalendar()[1]
            self.score[date[:4]].update({week:score.weekly_score(date)})
        

class HabitData:
    def __init__(self,days=7):
        self.datelist:DateList=DateList()
        self.days=days
        self.scoreList:ScoreList=ScoreList()
    
    def update_today(self,option):
        if(option==1):
            self.datelist.mark_today()
        else:
            self.datelist.unmark_today()
        new_score=Score(self.datelist,self.days)
        self.scoreList.update_actual_score(new_score)
    
    def update_date(self,dates):
        self.datelist.edit_dates(dates)
        new_score=Score(self.datelist,self.days)
        self.scoreList.update_score(new_score,dates)


class Habit:
    id_h:int
    name:str
    description:str
    #repetition by week
    days:int
    data:HabitData()

    def __init__(self,**kwargs):
        self.id_h=kwargs.get('id')
        self.name=kwargs.get('name')
        self.description=kwargs.get('description')
        self.days=kwargs.get('days')
        self.data=HabitData(self.days)
    
    def __str__(self):
        return  f'{self.id_h} : {self.name}'

    def changes(self,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
        

habits_list = []
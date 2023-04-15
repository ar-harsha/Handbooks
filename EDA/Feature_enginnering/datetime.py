# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:36:43 2023

@author: harsh
"""

import datetime as dt

d = dt.date(1999,4,22)
#time delta
dt_delta = dt.timedelta(100)#almost 3 months
print(d+dt_delta)

print(d.strftime("%A,%B,%d,%Y"))

date = dt.date(2023,2,26)
time = dt.time(22,27,8) #hrs : min : sec
date_time = dt.datetime(2023,2,26,22,27,8)

#get current date time
present = dt.datetime.today()
print(present)

#str to datetime
random_date = "22/04/1999"
to_dt = dt.datetime.strptime(random_date,"%d/%m/%Y")
print(to_dt)
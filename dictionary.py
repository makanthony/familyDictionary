# -*- coding: utf-8 -*-
"""
Dec 1 2022

Anthony Mak
"""

Dad = {
       'Name':'Hank',
        'Birthday':'06/26/1974',
        'Favorite artist':'Black Flag',
        'Favorite Color':'Red'
       }
Mom = {
       'Name':'Madison',
        'Birthday':'09/15/1976',
        'Favorite artist':'Gorillaz',
        'Favorite Color':'Orange'
       }
Brother = {
    'Name':'Jacob',
     'Birthday':'05/27/2003',
     'Favorite artist':'Megadeth',
     'Favorite Color':'Blue'
    }
Sister = {
    'Name':'Isabella',
     'Birthday':'03/22/2000',
     'Favorite artist':'Rise Against',
     'Favorite Color':'Purple'
     }
Cousin = {
    'Name':'Tito',
     'Birthday':'08/06/1997',
     'Favorite artist':'Kendrick Lamar',
     'Favorite Color':'Green'
    }

print(Dad, Mom, Brother, Sister, Cousin)

Uncle = {
    'Name':'Peter',
     'Birthday':'11/27/1980',
     'Favorite Color':'Pink'
    }

name1 = Dad['Name']
if(Dad['Name'] > Mom['Name']):
    name2 = name1
    name1 = Mom['Name']
else:
    name2 = Mom['Name']

if(Brother['Name'] > Dad['Name']):
    if(Brother['Name'] > Mom['Name']):
        name3 = Brother['Name']
    else:
        name3 = name2
        name2 = Brother['Name']
else:
    name3 = name2
    name2 = name1
    name1 = Brother['Name']

if(Sister['Name'] > Dad['Name']):
    if(Sister['Name'] > Mom['Name']):
        if(Sister['Name'] > Brother['Name']):
            name4 = Sister['Name']
        else:
            name4 = name3
            name3 = Sister['Name']
    else:
        name4 = name3
        name3 = name2
        name2 = Sister['Name']
else:
    name4 = name3
    name3 = name2
    name2 = name1
    name1 = Sister['Name']
    
if(Cousin['Name'] > Dad['Name']):
    if(Cousin['Name'] > Mom['Name']):
        if(Cousin['Name'] > Brother['Name']):
            if(Cousin['Name'] > Sister['Name']):
                name5 = Cousin['Name']
            else:
                name5 = name4
                name4 = Cousin['Name']
        else:
            name5 = name4
            name4 = name3
            name3 = Cousin['Name']
    else:
        name5 = name4
        name4 = name3
        name3 = name2
        name2 = Cousin['Name']
else:
    name5 = name4
    name4 = name3
    name3 = name2
    name2 = name1
    name1 = Cousin['Name']
    
if(Cousin['Name'] > Dad['Name']):
    if(Cousin['Name'] > Mom['Name']):
        if(Cousin['Name'] > Brother['Name']):
            if(Cousin['Name'] > Sister['Name']):
                if(Uncle['Name'] > Cousin['Name']):
                    name6 = Uncle['Name']
                else:
                    name6 = name5
                    name5 = Uncle['Name']
            else:
                name6 = name5
                name5 = name4
                name4 = Uncle['Name']
        else:
            name6 = name5
            name5 = name4
            name4 = name3
            name3 = Uncle['Name']
    else:
        name6 = name5
        name5 = name4
        name4 = name3
        name3 = name2
        name2 = Uncle['Name']
else:
    name6 = name5
    name5 = name4
    name4 = name3
    name3 = name2
    name2 = name1
    name1 = Uncle['Name']
    
print("{}, {}, {}, {}, {}, {}".format(name1, name2, name3, name4, name5, name6))
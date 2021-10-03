dta = {     'CS101': {'Room Number': '3004', 'Instructor': 'Haynes', 'Meeting Time': '8:00 a.m.'},
                 'CS102': {'Room Number': '4501', 'Instructor': 'Alvarado', 'Meeting Time': '9:00 a.m.'},   
                   'CS103': {'Room number': '6755', 'Instructor': 'Rich', 'Meeting Time':'10:00 a.m.'},
                  'NT110': {'Room Number': '1244', 'Instructor': 'Burke', 'Meeting Time': '11:00 a.m.'},   
                   'CM241': {'Room Number': '1411', 'Instructor': 'Lee', 'Meeting Time':'1:00 a.m.'}} 
clss_choice = input("what class would you like to see?: ")



print('Room number:', dta[clss_choice]['Room Number'], 'Instructor:', dta[clss_choice]['Instructor'], 'Meeting time:', dta[clss_choice]['Meeting Time'] )
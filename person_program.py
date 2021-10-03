import Person_class as PR
name = 'Ryan'
adress = '1511 meadow glade ct'
telephone = '8329333904'
customer_num = '69420'
mailing_pref = True
mailing_pref1 = False
ryan1 = PR.person(name,adress,telephone)
ryan2 = PR.customer(name,adress,telephone,customer_num,mailing_pref1)
ryan3 = PR.customer(name,adress,telephone,customer_num,mailing_pref)
ryan1.print_person()
ryan2.print_person()
ryan3.print_person()

import mysql.connector

# timelist= []
# for i in range(3):
#     randh = random.randint(1, 23)
#     randm = random.randint(0, 59)
#     ti0 = datetime.time(randh, randm, 0)
#
#     timelist.append(str(ti0))
#
# times = {}
# k = 0
# for i in timelist:
#     k = k+1
#     times[k] = i
#
#
#
#
# print(timelist)
# print(times)
#
# import mysql.connector as con
#
# c = con.connect(host = 'localhost', user = 'root', passwd = 'mySQL1234$s-10763', database = 'tickets')
# if c.is_connected():
#     print('Connected')
#
#
# timeValidator = datetime.date.today()
# #strp
# DOB = (input("Enter your Date of Birth in yyyy-mm-dd format: "))
# validDOB = datetime.datetime.strptime(DOB, "%Y-%m-%d").date()
# if validDOB >= timeValidator.today():
#     print("\nCannot choose a date in the future, ", DOB, "Please try again..\n")
# #
# cur = c.cursor()
# cur.execute('insert into date1 values("{date}")'.format(date = DOB))
# c.commit()

passenger1 = "sai"
DOB = "2005-08-11"
boardGen = "AXJS2348"
passportNumber = "S28393"
airline = "Emirates"
fltime = "01:34:00"
fldate = "2023-03-01"
flnum = "AXE3402"
con = mysql.connector.connect(user='root', host='localhost', password='mySQL1234$s-10763', database='tickets')
cur = con.cursor()
cur.execute('insert into journeydetails values ("{p1}","{dob}","{bpass}","{passport}","{airline}","{fltime}",'
            '"{fldate}","{flnum}"').format(
    p1= passenger1, dob=DOB, bpass=boardGen, passport=passportNumber, airline=airline,
    fltime=fltime, fldate=fldate, flnum=flnum)
con.commit()


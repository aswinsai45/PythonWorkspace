import mysql.connector as connector

con = connector.connect(user='root', host='localhost', password='mySQL1234$s-10763')
cur = con.cursor(buffered=True)


def createdatabase():
    try:
        cur.execute('CREATE DATABASE STUDENT;')
        cur.execute('USE STUDENT;')
        con.commit()
        print('Database created successfully')

    except connector.errors.DatabaseError:
        print('Database Already Exists!')


def createtable():
    try:
        cur.execute('use student;')
        cur.execute(
            'CREATE TABLE STUDENTDETAILS(ID INT, NAME VARCHAR(50), AGE BIGINT, CLASS VARCHAR(5), SECTION VARCHAR(5));')
        con.commit()
        cur.execute(
            'CREATE TABLE MARKSDETAILS(ID INT, EXAMNAME VARCHAR(30), SUB1 float, SUB2 float, SUB3 float, SUB4 float, SUB5 float, TOTAL float, AVERAGE FLOAT, GRADE VARCHAR(3));')
        con.commit()

        print('Tables created successfully')

    except connector.errors.ProgrammingError:
        print('Tables already exist!')


def insertStudentDetails():
    print()
    ID = int(input('Enter Student ID: '))
    name = input('Enter Name: ')
    age = int(input('Enter Age: '))
    class1 = input('Enter Class: ')
    sec = input('Enter Section: ')

    cur.execute('use student;')
    cur.execute('insert into studentdetails values({},"{}",{},"{}","{}")'.format(ID, name, age, class1, sec))
    con.commit()


def insertMarksDetails():
    ID = int(input('Enter ID: '))
    exam = input('Enter Exam Name: ')
    sub1 = float(input('Sub1 marks: '))
    sub2 = float(input('Sub2 marks: '))
    sub3 = float(input('Sub3 marks: '))
    sub4 = float(input('Sub4 marks: '))
    sub5 = float(input('Sub5 marks: '))
    total = sub1 + sub2 + sub3 + sub4 + sub5
    average = total / 5
    grade = input('Enter Grade: ')

    cur.execute('use student;')
    cur.execute(
        'insert into marksdetails values({},"{}",{},{},{},{},{},{},{},"{}")'.format(ID, exam, sub1, sub2, sub3, sub4,
                                                                                    sub5, total, average, grade))
    con.commit()


def updateMarksDetails():
    id = int(input('Enter ID to change marks: '))
    subn = input('Enter SubjectNum to change mark: ')
    newmark = float(input('Enter New Mark: '))

    sub = 'sub'+subn
    cur.execute('use student;')
    cur.execute(
        'update marksdetails set {} = {} where ID = {}'.format(sub, newmark, id))
    con.commit()


    cur.execute('update marksdetails set average = (sub1+sub2+sub3+sub4+sub5/5)')
    cur.execute('update marksdetails set total = sub1+sub2+sub3+sub4+sub5 where ID = {}'.format(id))
    con.commit()

def displaystudent():
    cur.execute('SELECT * FROM STUDENTDETAILS;')
    v = cur.fetchall()
    if v:
        for i in v:
            print(i)
    else:
        print('Table Empty')

def displaymark():
    cur.execute('SELECT * FROM MARKSDETAILS;')
    v = cur.fetchall()
    if v:
        for i in v:
            print(i)
    else:
        print('Table empty')


print('1. Create Database\n2. Create Tables\n3. Insert Student Details\n4. Inser Mark Details\n5. Update Marks\n6. Display Student Table\n7. Display Mark Table\n8. Exit')

while True:
    ch = int(input('Enter choice: '))
    if ch == 1:
        createdatabase()
    elif ch == 2:
        createtable()
    elif ch == 3:
        print('Have to enter atleast 5 datas\n')
        for i in range(5):
            insertStudentDetails()
    elif ch == 4:
        print('Have to enter atleast 5 datas\n')
        for i in range(5):
            insertMarksDetails()
    elif ch == 5:
        updateMarksDetails()
    elif ch == 6:
        displaystudent()
    elif ch == 7:
        displaymark()
    elif ch == 8:
        print('Thank you')
        break
    else:
        print('PLease enter a valid choice')


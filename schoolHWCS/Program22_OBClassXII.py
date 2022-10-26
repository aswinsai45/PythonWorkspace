import mysql.connector as connector

con = connector.connect(user='root', host='localhost', password='mySQL1234$s-10763')
cur = con.cursor()


def createdatabase():
    try:
        cur.execute('CREATE DATABASE STUDENT;')
        cur.execute('USE STUDENT;')
        con.commit()

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

    except connector.errors.ProgrammingError:
        print('Tables already exist!')


def insertStudentDetails():
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
    sub = input('Enter SubjectNum to change mark: ')
    newmark = float(input('Enter New Mark: '))

    cur.execute('use student;')
    cur.execute(
        'update marksdetails set "{}" = {} where ID = {} and "{}" in (sub1, sub2, sub3, sub4, sub5);)'.format(sub, newmark, id, sub))
    con.commit()

    cur.execute('update marksdetails set average = (sub1+sub2+sub3+sub4+sub5/5) and total = sub1+sub2+sub3+sub4+sub5 where ID = {}'.format(id))

updateMarksDetails()

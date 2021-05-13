import datetime
import pymysql
myDB = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project_db")
myCursor = myDB.cursor()


un = input("Enter UserName: ")
pd = input("Enter Password: ")

myCursor.execute("select * from user_profile where uname='{}' and pwd='{}'".format(un,pd))
uData = myCursor.fetchone()

def work_faculty():
    while True:
        print("1. Add Student")
        print("2. Add Technology")
        print("3. Add Questions")
        print("4. Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            s_un = input("Enter Student UserName: ")
            pwd = input("Enter Password: ")
            mob = input("Enter Mobile: ")

            myCursor.execute("insert into user_profile(uname,PWD,MOBILE,USETYPE) values('{}','{}','{}','student')".format(s_un, pwd, mob))
            myDB.commit()
            print("Student added!")
            
        elif ch == 2:
            try:
                tn = input("Enter Technology Name: ")
                myCursor.execute("insert into technology(tname) values ('{}')".format(tn))
                myDB.commit()
                print("Technology Added!")
            except:
                print("Technology already exist!")
        elif ch == 3:
            myCursor.execute("select * from technology")
            all_tech = myCursor.fetchall()

            for i in all_tech:
                print(i[0], i[1])

            tid = int(input("Select Tech ID:"))         
            
            q = input("Enter Question: ")
            a = input("Enter Option A: ")
            b = input("Enter Option B: ")
            c = input("Enter Option C: ")
            d = input("Enter Option D: ")
            correct = input("Enter Correct (A/B/C/D) : ")
            correct_2 = input("Enter Correct (A/B/C/D) : ")

            myCursor.execute("insert into questions(question,opta,optb,optc,optd,correct,correct2nd,techid)values('{}','{}','{}','{}','{}','{}','{}',{})".format(q,a,b,c,d,correct,correct_2,tid))
            myDB.commit()
            print("Question Added!")
            
            
        elif ch == 4:
            break

def work_student(userid):
    while True:
        print("1. Start test")
        print("2. Results")
        print("3. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            myCursor.execute("select * from technology")
            all_tech = myCursor.fetchall()

            for i in all_tech:
                print(i[0], i[1])

            tid = int(input("Select Tech ID:"))

            myCursor.execute("select * from questions where techid={}".format(tid))
            ques = myCursor.fetchall()
            j = 1
            count = 0
            
            for i in ques:
                print(j, i[1])
                print("A.",i[2])
                print("B.",i[3])
                print("C.",i[4])
                print("D.",i[5])

                ans = input("Enter ans: ")
                ans2 = input("Enter 2nd ans: ")


                if ans == i[6] or ans2 == i[7]:
                    count = count + 1
                    

                j += 1

            rslt = print("Result: ", (count/len(ques))*100)
               
     
        elif ch == 2:


            def marks():
                total==count

            def status():

                if rslt >= 40:
                      print("Pass")
                elif rslt <= 40:
                      print("Fail")          

            myCursor.execute("select * from technology")
            select_tech = myCursor.fetchall()

            for t in select_tech:
                print(t[0], t[1])

            
            sid = int(input("Select Tech ID:"))

            myCursor.execute("select * from questions where techid={}".format(sid))
            c = myCursor.fetchall()

            x = datetime.datetime.now()
            #y = x.strftime("%x")
             

            myCursor.execute("insert into result (userid,techid,resdate,marks,status)values('{}','{}','{}','{}','{}' )".format(userid,sid,x,marks,status))    
            myDB.commit()
            print("Hello! Your no.is:",marks, "And status is : ",status)            

            
        elif ch == 3:
            break




if uData:
    print("=======WELCOME {}==========".format(uData[1].upper()))
    if uData[4] == 'faculty':
        work_faculty()
    elif uData[4] == 'student':
        work_student(uData[0])
else:
    print("Wrong Credentials...")

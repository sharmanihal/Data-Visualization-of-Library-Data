import sys

from PyQt5.QtWidgets import *
from PyQt5.uic import *
import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cx_Oracle


file1 = open("username.txt","r")
file2 = open("password.txt","r")
user = file1.read()
passw = file2.read()
user = user[:-1]
passw = passw[:-1]


conn = cx_Oracle.connect(user+'/'+passw)
cur = conn.cursor()

'''
Main Starting Window Class
'''

class Main(QDialog):
    def __init__(self):
        super(Main,self).__init__()
        loadUi('MainWindow.ui',self)
        self.setWindowTitle("Main Window")
        self.button1.clicked.connect(self.mathematical)
        self.button2.clicked.connect(self.visualization)
    def mathematical(self):
        self.obj1=analysisq()
        self.obj1.show()
    def visualization(self):
        self.obj2=visualizationClass()
        self.obj2.show()



'''
MathsAnalysis class

'''
class analysisq(QDialog):


    def __init__(self):
        super(analysisq,self).__init__()
        loadUi('analysis.ui',self)
        self.setWindowTitle("Analysis")

        self.btn1.clicked.connect(self.allBooks)
        self.btn2.clicked.connect(self.famousAuthor)
        self.btn3.clicked.connect(self.famousBook)
        self.btn4.clicked.connect(self.currentlyIssued)
        self.btn5.clicked.connect(self.totalBorrowers)
        self.btn6.clicked.connect(self.totalLost)
        self.btn7.clicked.connect(self.availableBooks)
        self.btn8.clicked.connect(self.booksPerMonth)


    def booksPerMonth(self):
        self.a=borrowers()
        self.a.show()

    def allBooks(self):
        query = "select * from books"
        list1 = []
        cur.execute(query)
        for row in cur:
            list1.append(row[0])
        a = str(len(list1))
        self.lab1.setText(a)
    def famousAuthor(self):
        query = "select * from books"
        list1 = []
        cur.execute(query)
        for row in cur:
            list1.append(row[2])
         # this is imported to find the most occuring author name
        from collections import Counter
        # It will return the most common author name.
        def Most_Common_Author(lst):
           data = Counter(lst)
           return data.most_common(1)[0][0]

        self.lab2.setText(Most_Common_Author(list1))
    def famousBook(self):
        query = "select * from books"
        list1 = []
        cur.execute(query)
        for row in cur:
            list1.append(row[1])
        #this is imported to find the most occuring book name
        from collections import Counter
        #It will return the most common book name.
        def Most_Common(lst):
            data = Counter(lst)
            return data.most_common(1)[0][0]

        self.lab3.setText(Most_Common(list1))


    def currentlyIssued(self):
        query ="select * from borrowers"
        list2=[]
        cur.execute(query)
        for row in cur:
            list2.append(row[0])
        a=str(len(list2))
        self.lab4.setText(a)

    def totalBorrowers(self):
        query="select * from return "
        list3 = []
        cur.execute(query)
        for row in cur:
            list3.append(row[0])
        a = str(len(list3))
        self.lab5.setText(a)

    def availableBooks(self):
        query="select * from books where availability='y'or availability='Y'"
        list4 = []
        cur.execute(query)
        for row in cur:
            list4.append(row[0])
        a = str(len(list4))
        self.lab7.setText(a)

    def totalLost(self):
        query="select * from lost"
        list5 = []
        cur.execute(query)
        for row in cur:
            list5.append(row[0])
        a = str(len(list5))
        self.lab6.setText(a)


'''
Visualization Class
'''
class visualizationClass(QDialog):
    def __init__(self):
        super(visualizationClass, self).__init__()
        loadUi('visualizationMainWindow.ui', self)
        self.btn1.clicked.connect(self.borrowersIncreasingWithTime)
        self.btn2.clicked.connect(self.booksClassifiedInDifferentCategories)
        self.btn4.clicked.connect(self.availableIssuedLostBooks)
        self.btn5.clicked.connect(self.bookIssuedPerMonth)


    def bookIssuedPerMonth(self):

        qjan = "select * from borrowers where extract(month from doi)=1 and extract(year from doi)=2018"
        qfeb = "select * from borrowers where extract(month from doi)=2 and extract(year from doi)=2018"
        qmarch = "select * from borrowers where extract(month from doi)=3 and extract(year from doi)=2018"
        qapril = "select * from borrowers where extract(month from doi)=4 and extract(year from doi)=2018"
        qmay = "select * from borrowers where extract(month from doi)=5 and extract(year from doi)=2018"
        qjune = "select * from borrowers where extract(month from doi)=6 and extract(year from doi)=2018"
        qjuly = "select * from borrowers where extract(month from doi)=7 and extract(year from doi)=2018"
        qaug = "select * from borrowers where extract(month from doi)= 8 and extract(year from doi)=2018"
        qsep = "select * from borrowers where extract(month from doi)=9 and extract(year from doi)=2018"
        qoct = "select * from borrowers where extract(month from doi)=10 and extract(year from doi)=2018"
        qnov = "select * from borrowers where extract(month from doi)=11 and extract(year from doi)=2018"
        qdec = "select * from borrowers where extract(month from doi)=12 and extract(year from doi)=2018"
        # jan
        totalCount = []
        count = 0
        cur.execute(qjan)
        for row in cur:
            count += 1
        totalCount.append(count)

        # feb
        count = 0
        cur.execute(qfeb)
        for row in cur:
            count += 1
        totalCount.append(count)

        # march
        count = 0
        cur.execute(qmarch)
        for row in cur:
            count += 1
        totalCount.append(count)

        # april
        count = 0
        cur.execute(qapril)
        for row in cur:
            count += 1
        totalCount.append(count)

        # may
        count = 0
        cur.execute(qmay)
        for row in cur:
            count += 1
        totalCount.append(count)

        # june
        count = 0
        cur.execute(qjune)
        for row in cur:
            count += 1
        totalCount.append(count)

        # july
        count = 0
        cur.execute(qjuly)
        for row in cur:
            count += 1
        totalCount.append(count)

        # aug
        count = 0
        cur.execute(qaug)
        for row in cur:
            count += 1
        totalCount.append(count)

        # sep
        count = 0
        cur.execute(qsep)
        for row in cur:
            count += 1
        totalCount.append(count)

        # oct
        count = 0
        cur.execute(qoct)
        for row in cur:
            count += 1
        totalCount.append(count)

        # nov
        count = 0
        cur.execute(qnov)
        for row in cur:
            count += 1
        totalCount.append(count)

        # dec
        count = 0
        cur.execute(qdec)
        for row in cur:
            count += 1
        totalCount.append(count)

        Month = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        colors = ['yellowgreen', 'lightskyblue', 'lightcoral', 'red', 'Green', 'DarkGreen', 'Grey', 'orange', 'brown',
                  'silver', 'pink', 'darkblue']

        plt.pie(totalCount, colors=colors, startangle=90, shadow=True, autopct='%1.1f%%')
        plt.legend(Month, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    def booksClassifiedInDifferentCategories(self):
        sql = 'select * from books'
        cur.execute(sql)
        programming = 0
        nonProgramming = 0

        total = []

        # ^((?!java|cplusplus).)*$
        for row in cur:
            if re.search(
                    "JAVA|C+\+|PYTHON|HTML|CSS|JAVASCRIPT|PROGRAMMING|DATA|ALGORITHM|ANGULAR|\.NET|VB|VISUAL BASIC|JQUERY|CODING",
                    row[1]):
                programming += 1
            else:
                nonProgramming += 1
        total.append(programming)
        total.append(nonProgramming)

        # books = ['Programming Books', "Non Programming Books"]
        colors = ['green', 'orange']

        green_patch = mpatches.Patch(color='green', label='Progrramming Books')

        orange_patch = mpatches.Patch(color='orange', label='Non Progrramming Books')
        plt.legend(handles=[green_patch, orange_patch])
        plt.pie(total, colors=colors, shadow=True, startangle=90, autopct='%1.1f%%')
        plt.show()

    def booksIssuedPerSemester(self):
        pass

    def availableIssuedLostBooks(self):
        sql1 = 'select * from books where availability=\'Y\''
        sql2 = 'select * from books where availability=\'N\''
        sql3 = 'select * from books where availability=\'L\''

        cur.execute(sql1)
        count = 0
        totalCount = []
        for i in cur:
            count += 1
        totalCount.append(count)
        count = 0

        cur.execute(sql2)
        for j in cur:
            count += 1
        totalCount.append(count)
        count = 0

        cur.execute(sql3)
        for k in cur:
            count += 1
        totalCount.append(count)

        books = ['Available Books', 'Issued Books', 'Lost Books']
        colors = ['yellowgreen', 'lightskyblue', 'lightcoral']

        plt.pie(totalCount, colors=colors, startangle=90, shadow=True, autopct='%1.1f%%')

        plt.legend(books, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    def borrowersIncreasingWithTime(self):
        qjan = "select * from borrowers where extract(month from doi)=1 and extract(year from doi)=2018"
        qfeb = "select * from borrowers where extract(month from doi)=2 and extract(year from doi)=2018"
        qmarch = "select * from borrowers where extract(month from doi)=3 and extract(year from doi)=2018"
        qapril = "select * from borrowers where extract(month from doi)=4 and extract(year from doi)=2018"
        qmay = "select * from borrowers where extract(month from doi)=5 and extract(year from doi)=2018"
        qjune = "select * from borrowers where extract(month from doi)=6 and extract(year from doi)=2018"
        qjuly = "select * from borrowers where extract(month from doi)=7 and extract(year from doi)=2018"
        qaug = "select * from borrowers where extract(month from doi)=8 and extract(year from doi)=2018"
        qsep = "select * from borrowers where extract(month from doi)=9 and extract(year from doi)=2018"
        qoct = "select * from borrowers where extract(month from doi)=10 and extract(year from doi)=2018"
        qnov = "select * from borrowers where extract(month from doi)=11 and extract(year from doi)=2018"
        qdec = "select * from borrowers where extract(month from doi)=12 and extract(year from doi)=2018"
        a = []
        # jan
        cur.execute(qjan)
        totalCount1 = set()
        for row in cur:
            totalCount1.add(row[0])
        totalCount1 = len(totalCount1)
        a.append(totalCount1)

        # feb
        cur.execute(qfeb)
        totalCount2 = set()
        for row in cur:
            totalCount2.add(row[0])
        totalCount2 = len(totalCount2)
        a.append(totalCount2)

        # march
        cur.execute(qmarch)
        totalCount3 = set()
        for row in cur:
            totalCount3.add(row[0])
        totalCount3 = len(totalCount3)
        a.append(totalCount3)

        # april
        cur.execute(qapril)
        totalCount4 = set()
        for row in cur:
            totalCount4.add(row[0])
        totalCount4 = len(totalCount4)
        a.append(totalCount4)

        # may
        cur.execute(qmay)
        totalCount5 = set()
        for row in cur:
            totalCount5.add(row[0])
        totalCount5 = len(totalCount5)
        a.append(totalCount5)

        # june
        cur.execute(qjune)
        totalCount6 = set()
        for row in cur:
            totalCount6.add(row[0])
        totalCount6 = len(totalCount6)
        a.append(totalCount6)

        # july
        cur.execute(qjuly)
        totalCount7 = set()
        for row in cur:
            totalCount7.add(row[0])
        totalCount7 = len(totalCount7)
        a.append(totalCount7)

        # aug
        cur.execute(qaug)
        totalCount8 = set()
        for row in cur:
            totalCount8.add(row[0])
        totalCount8 = len(totalCount8)
        a.append(totalCount8)

        # sep
        cur.execute(qsep)
        totalCount9 = set()
        for row in cur:
            totalCount9.add(row[0])
        totalCount9 = len(totalCount9)
        a.append(totalCount9)

        # oct
        cur.execute(qoct)
        totalCount10 = set()
        for row in cur:
            totalCount10.add(row[0])
        totalCount10 = len(totalCount10)
        a.append(totalCount10)

        # nov
        cur.execute(qnov)
        totalCount11 = set()
        for row in cur:
            totalCount11.add(row[0])
        totalCount11 = len(totalCount11)
        a.append(totalCount11)

        # dec
        cur.execute(qdec)
        totalCount12 = set()
        for row in cur:
            totalCount12.add(row[0])
        totalCount12 = len(totalCount12)
        a.append(totalCount12)
        Month = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        plt.plot(Month,a)
        plt.title("Borrowers per month")
        plt.xlabel("Months")
        plt.ylabel("Borrowers")
        plt.show()

class borrowers(QDialog):
    a = []


    def __init__(self):
        super(borrowers,self).__init__()
        loadUi('noOfBorrowers.ui',self)
        self.setWindowTitle("Borrowers")

        self.jan.clicked.connect(self.janfun)
        self.feb.clicked.connect(self.febfun)
        self.march.clicked.connect(self.marchfun)
        self.april.clicked.connect(self.aprilfun)
        self.may.clicked.connect(self.mayfun)
        self.june.clicked.connect(self.junefun)
        self.july.clicked.connect(self.julyfun)
        self.aug.clicked.connect(self.augfun)
        self.sep.clicked.connect(self.sepfun)
        self.oct.clicked.connect(self.octfun)
        self.nov.clicked.connect(self.novfun)
        self.dec.clicked.connect(self.decfun)

    qjan = "select * from borrowers where extract(month from doi)=1 and extract(year from doi)=2018"
    qfeb = "select * from borrowers where extract(month from doi)=2 and extract(year from doi)=2018"
    qmarch = "select * from borrowers where extract(month from doi)=3 and extract(year from doi)=2018"
    qapril = "select * from borrowers where extract(month from doi)=4 and extract(year from doi)=2018"
    qmay = "select * from borrowers where extract(month from doi)=5 and extract(year from doi)=2018"
    qjune = "select * from borrowers where extract(month from doi)=6 and extract(year from doi)=2018"
    qjuly = "select * from borrowers where extract(month from doi)=7 and extract(year from doi)=2018"
    qaug = "select * from borrowers where extract(month from doi)=8 and extract(year from doi)=2018"
    qsep = "select * from borrowers where extract(month from doi)=9 and extract(year from doi)=2018"
    qoct = "select * from borrowers where extract(month from doi)=10 and extract(year from doi)=2018"
    qnov = "select * from borrowers where extract(month from doi)=11 and extract(year from doi)=2018"
    qdec = "select * from borrowers where extract(month from doi)=12 and extract(year from doi)=2018"

    # jan
    cur.execute(qjan)
    totalCount1 = set()
    for row in cur:
        totalCount1.add(row[0])
    totalCount1 = len(totalCount1)
    a.append(totalCount1)

    # feb
    cur.execute(qfeb)
    totalCount2 = set()
    for row in cur:
        totalCount2.add(row[0])
    totalCount2 = len(totalCount2)
    a.append(totalCount2)

    # march
    cur.execute(qmarch)
    totalCount3 = set()
    for row in cur:
        totalCount3.add(row[0])
    totalCount3 = len(totalCount3)
    a.append(totalCount3)

    # april
    cur.execute(qapril)
    totalCount4 = set()
    for row in cur:
        totalCount4.add(row[0])
    totalCount4 = len(totalCount4)
    a.append(totalCount4)

    # may
    cur.execute(qmay)
    totalCount5 = set()
    for row in cur:
        totalCount5.add(row[0])
    totalCount5 = len(totalCount5)
    a.append(totalCount5)

    # june
    cur.execute(qjune)
    totalCount6 = set()
    for row in cur:
        totalCount6.add(row[0])
    totalCount6 = len(totalCount6)
    a.append(totalCount6)

    # july
    cur.execute(qjuly)
    totalCount7 = set()
    for row in cur:
        totalCount7.add(row[0])
    totalCount7 = len(totalCount7)
    a.append(totalCount7)

    # aug
    cur.execute(qaug)
    totalCount8 = set()
    for row in cur:
        totalCount8.add(row[0])
    totalCount8 = len(totalCount8)
    a.append(totalCount8)

    # sep
    cur.execute(qsep)
    totalCount9 = set()
    for row in cur:
        totalCount9.add(row[0])
    totalCount9 = len(totalCount9)
    a.append(totalCount9)

    # oct
    cur.execute(qoct)
    totalCount10 = set()
    for row in cur:
        totalCount10.add(row[0])
    totalCount10 = len(totalCount10)
    a.append(totalCount10)

    # nov
    cur.execute(qnov)
    totalCount11 = set()
    for row in cur:
        totalCount11.add(row[0])
    totalCount11 = len(totalCount11)
    a.append(totalCount11)

    # dec
    cur.execute(qdec)
    totalCount12 = set()
    for row in cur:
        totalCount12.add(row[0])
    totalCount12 = len(totalCount12)
    a.append(totalCount12)

    def janfun(self):
        self.lab1.setText(str(self.a[0]))

    def febfun(self):
        self.lab2.setText(str(self.a[1]))

    def marchfun(self):
        self.lab3.setText(str(self.a[2]))

    def aprilfun(self):
        self.lab4.setText(str(self.a[3]))

    def mayfun(self):
        self.lab5.setText(str(self.a[4]))

    def junefun(self):
        self.lab6.setText(str(self.a[5]))

    def julyfun(self):
        self.lab7.setText(str(self.a[6]))

    def augfun(self):
        self.lab8.setText(str(self.a[7]))

    def sepfun(self):
        self.lab9.setText(str(self.a[8]))

    def octfun(self):
        self.lab10.setText(str(self.a[9]))

    def novfun(self):
        self.lab11.setText(str(self.a[10]))

    def decfun(self):
        self.lab12.setText(str(self.a[11]))



app=QApplication(sys.argv)
q=Main()
q.show()
sys.exit(app.exec_())





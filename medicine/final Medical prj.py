import sqlite3 as sql
import datetime
con=sql.connect('medplus')
cur=con.cursor()
print('1.Search\t\t\t2.Billing\n3.Display\t\t\t4.Order\n5.Order Place\t\t6.Check Profit')
c=int(input('enter your Choice:  '))
if c==1:
    s = 'select MedicineID,Availability,Medicine Name from Medicine '
    cur.execute(s)
    data = cur.fetchall()
    print('mid\t avbty\t M name')
    for i in data:
        for j in i:
            print(j, end='\t')
        print()
elif c==2:
    totalbill = 0
    c2 = 'y'
    while c2 == 'y':
        qry = 'select * from Transactions'
        cur.execute(qry)
        data1 = cur.fetchall()
        for i in data1:
            pass
        a11= i[0]
        a12=a11[0]
        a13=int(a11[1:])
        a13+=1
        tid=a12+str(a13)
        a = 'select * from medicine where MedicineID=?'
        mid = int(input('enter the medicine id:   '))
        t = (mid,)
        cur.execute(a, t)
        p = cur.fetchone()
        print(p)
        if p != None:
            q = 'insert into Transactions values(?,?,?,?,?,?)'
            b = 'update Medicine set Availability=Availability-? where MedicineID=?'
            q1 = 'insert into Orders values(?,?,?,?,?)'
            pr = 'insert into Profit values(?,?,?,?,?,?)'
            date = datetime.date.today()
            odate = date.isoformat()
            mname = p[1]
            print(p[4], 'sheets available')
            qq = int(input('enter the quantity :  '))
            cp = p[2]
            t = (tid, mid, odate, mname, qq, cp)
            a1 = (q1, mid)
            sp=p[3]
            p1 = (mid, mname,odate, cp, sp, qq)
            cur.execute(pr, p1)
            cur.execute(q, t)
            cur.execute(b, a1)
            print(mname, 'billing is entered')
            tb = (p[3] * qq)
            totalbill += tb
        else:
            print('Medicine is Jot Available')
        c2 = input('do u want to add another Medicine(y/n):  ')
        print('Final Bill is', totalbill)
elif c==3:
    import sqlite3 as sql
    con = sql.connect('medplus')
    cur = con.cursor()
    date = input('enter the date')
    s = 'select * from Transactions where Date=?'
    t = (date,)
    cur.execute(s, t)
    data = cur.fetchall()
    if data!=None:
        for i in data:
            for j in i:
                print(j, end='\t')
            print()
    else:
        print(s,'-this Date history is not available')
elif c==4:
    mid = int(input('enter the medicine Id:  '))
    s = 'select * from Medicine where MedicineID=?'
    s1 = (mid,)
    cur.execute(s, s1)
    d = cur.fetchone()
    if d != None:
        o = int(input('enter the Medicine Quantity'))
        qu = f'update Medicine set Availability=Availability+{o} where MedicineID={mid}'
        cur.execute(qu)
        q = 'insert into orders values(?,?,?,?,?,?,?)'
        oid = int(input('enter the order id in integer:  '))
        date = datetime.date.today()
        odate = date.isoformat()
        mname = d[1]
        cost = d[2]
        bill = (cost * o)
        t = (oid, mid, odate, mname, cost, o, bill)
        cur.execute(q, t)
    else:
        q = 'insert into orders values(?,?,?,?,?,?,?)'
        a = 'insert into Medicine values(?,?,?,?,?)'
        orid = int(input('enter the order id in integer:  '))
        date = datetime.date.today()
        odate = date.isoformat()
        mname = input('enter mname:  ')
        oq = int(input('enter the order quantity:  '))
        cprice = float(input('enter the cost price:  '))
        sprice = float(input('enter the sell price:   '))
        bill = cprice * oq
        t = (orid, mid, odate, mname, cprice, oq, bill)
        a1 = (mid, mname, cprice, sprice, oq)
        cur.execute(q, t)
        cur.execute(a, a1)
        print(mname, 'ordered successful')
elif c==5:
    q = 'select   * from Medicine where Availability<=30'
    cur.execute(q)
    data = cur.fetchall()
    qry='select * from orders'
    cur.execute(qry)
    data1=cur.fetchall()
    for i in data1:
        pass
    oid=i[0]
    oid+=1
    print('mid\t\tmname\t\tavailability')
    for i in data:
        print(f'{i[0]}\t{i[1]}\t\t{i[4]}')
    c = 'select * from Medicine where MedicineID=?'
    a = 'insert into Orders values(?,?,?,?,?,?,?)'
    b = 'update Medicine set Availability=Availability+? where MedicineID=?'
    mid = int(input('enter the medicine id:  '))
    c1 = (mid,)
    cur.execute(c, c1)
    d = cur.fetchone()
    o = int(input('enter the order Quantity:  '))
    bill = d[2] * o
    date = datetime.date.today()
    odate = date.isoformat()
    mname = d[1]
    cost = d[2]
    b1 = (o, mid)
    cur.execute(b, b1)
    a1 = (oid, mid, odate, mname, cost, o, bill)
    cur.execute(a, a1)
elif c==6:
    margin=0
    s = f'select * from Profit where Date=?'
    date=input('enter the date')
    t=(date,)
    cur.execute(s,t)
    data = cur.fetchall()
    print('MID\t\t MNAME\t\t PROFIT\n---      -----       ------')
    for i in data:
        profit = (i[4] - i[3]) * i[5]
        print(i[0] ,i[1],'\t\t',profit)
        margin+=profit
    print('------------------------------------------------------\ntotal profit is : ---',margin,'\n------------------------------------------------------')
else:
    print('enter your correct option')
con.commit()
con.close()
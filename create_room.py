from database import *

def create_room(capa):
    if capa!='1' and capa!='2':
        print('Level is wrong')
        return
    db=databaselink()
    cur=db.cursor()
    cur.execute('select id from waiter')
    t=cur.fetchall()
    if len(t)==0:
        print('No waiter')
        cur.close()
        db.close()
        return
    else:
        cur.execute('select num from room')
        n=cur.fetchall()
        nn=list()
        for i in n:
            nn.append(i[0])
        for i in range(1,20000):
            if i not in nn:
                cur.execute('insert into room values(%s,%s,%s)'%(str(i),capa,str(t[0][0])))
                db.commit()
                re_room()
                cur.close()
                db.close()
                return
        print('Fail to create a room')
        return

#for i in range(3):
#    create_room('1')
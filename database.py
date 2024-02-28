import hashlib
import os
import pymysql
import time

def databaselink():
    db=pymysql.connect(host='localhost',user='root',password='zqy7036651',db='test_by_zqy')
    return db
################################
#辅助函数
def add_for(data):
    if data < 10:
        return '0' + str(data)
    return str(data)

def get_time():
    # 获取当前时间
    def add_for(data):
        if data < 10:
            return '0' + str(data)
        return str(data)

    t = time.localtime()
    t_y = str(t.tm_year)

    return t_y + '-' + add_for(t.tm_mon) + '-' + add_for(t.tm_mday) + ' ' + add_for(t.tm_hour) + ':' + add_for(t.tm_min) + ':' + add_for(t.tm_sec)

def shift(dt):
    return add_for(dt.year)+'-'+add_for(dt.month)+'-'+add_for(dt.day)+' '+add_for(dt.hour)+':'+add_for(dt.minute)+':'+add_for(dt.second)
#判断真确格式日期是否合法
def isvalid(year,month,day):
    y=int(year)
    m=int(month)
    d=int(day)
    if y<=0 or m<=0 or d<=0:
        return False
    if m==4 or m==6 or m==9 or m==11:
        if d==31:
            return False
    elif m==2:
        if y%4 or y%400==0:
            if d>=29:
                return False
        else:
            if d>=30:
                return False
    return True

def out_order_food():
    db=databaselink()
    cur=db.cursor()
    cur.execute('select food_id from order_food where food_id<0')
    l=list()
    for tt in cur.fetchall():
        l.append(tt[0])
    for i in range(-1000000000,0):
        if i not in l:
            cur.close()
            db.close()
            return i

def out_tec():
    db=databaselink()
    cur=db.cursor()
    cur.execute('select tec_id from order_service where tec_id<0')
    l=list()
    for tt in cur.fetchall():
        l.append(tt[0])
    for i in range(-1000000000, 0):
        if i not in l:
            cur.close()
            db.close()
            return i

#重新分配房间给服务员
def re_room():
    db=databaselink()
    cur=db.cursor()
    cur.execute('select id from waiter')
    #获得所有服务员的id
    waiter_all=list()
    for i in cur.fetchall():
        waiter_all.append(str(i[0]))
    #获取所有房间id
    room_all=list()
    cur.execute('select num from room')
    for i in cur.fetchall():
        room_all.append(str(i[0]))
    i=0
    j=0
    while j!=len(room_all):
        cur.execute('update room set waiter_id=%s where num=%s'%(waiter_all[i],room_all[j]))
        i=i+1
        if i==len(waiter_all):
            i=0
        j=j+1
    db.commit()
    cur.close()
    db.close()
###################################################
###内部按钮
#查询顾客库中是否有这个电话，电话是否合法，能否成功注册等等，返回true or false
def sec(phone,pa,pa_a):

    db=databaselink()
    cur=db.cursor()
    cur.execute('select* from login where phonenum="%s"'%phone)
    #此时库中有该号码
    if(len(cur.fetchall())):
        cur.close()
        db.close()
        return [False,'该号码已存在']
    #电话位数
    if phone.isdigit()==False or len(phone)!=11:
        cur.close()
        db.close()
        return [False,'电话有错误']
    #密码问题
    if pa!=pa_a:
        cur.close()
        db.close()
        return [False,'两次密码不一致']
    if len(pa)==0:
        cur.close()
        db.close()
        return [False,'密码长度不足']
    salt_bytes: bytes = os.urandom(64)
    password_bytes=pa.encode('utf-8')
    # set corresponding parameters
    n: int = 4
    r: int = 8
    p: int = 16
    # Hash encryption
    password_hash: bytes = hashlib.scrypt(password_bytes, salt=salt_bytes, n=n, r=r, p=p)
    cur.execute('select id from login')
    id_all_tuple=cur.fetchall()
    id_all_list=list()
    for id_t in id_all_tuple:
        id_all_list.append(str(id_t[0]))
    for id in range(100000000):
        if str(id) not in id_all_list :
            cur.execute('insert into login values(%s,"%s","%s",%s,"%s")'%(id,phone,bytes.hex(password_hash),'3',bytes.hex(salt_bytes)))
            db.commit()
            cur.close()
            db.close()
            return [True,'注册成功']
    cur.close()
    db.close()
    return [False,'请联系管理员']


def alter_pas_guanli(phone,old,neww,neww_a):
    if neww!=neww_a:
        return [False,'两次密码不一致']
    if phone.isdigit()==False or len(phone)!=11:
        return [False,'电话号码不对']
    if old==neww:
        return[False,'新旧密码一致']
    if len(neww)==0 or len(old)==0:
        return[False,'未输入旧密码或新密码']
    db=databaselink()
    cur=db.cursor()
    cur.execute('select pwd,salt from login where phonenum=%s'%phone)
    t=cur.fetchall()
    if len(t)!=1:
        cur.close()
        db.close()
        return [False,'无该手机号']
    a,b,c=f1(phone,old)
    if a=='false':
        cur.close()
        db.close()
        return [False,'手机号或密码有误']
    elif a=='true':
        salt_bytes: bytes = bytes.fromhex(t[0][1])
        password_bytes = neww.encode('utf-8')
        # set corresponding parameters
        n: int = 4
        r: int = 8
        p: int = 16
        # Hash encryption
        password_hash: bytes = hashlib.scrypt(password_bytes, salt=salt_bytes, n=n, r=r, p=p)
        ppp=bytes.hex(password_hash)
        cur.execute('update login set pwd="%s" where phonenum=%s'%(ppp,phone))
        db.commit()
        cur.close()
        db.close()
        return [True,'修改成功']

    def d1(id):
        db = databaselink()
        cur = db.cursor()
        time_now = get_time()
        # 有没有正在进行的订单
        cur.execute(
            'select id from order_ where cus_id=%s and start_time<"%s" and end_time>"%s"' % (id, time_now, time_now))
        if len(cur.fetchall()) != 0:
            return False
        # 此时开始删除
        cur.execute('select id from order_ where cus_id=%s and start_time>"%s"' % (id, time_now))
        l = list()
        for i in cur.fetchall():
            l.append(str(i[0]))
        # 删除预约订单
        del_ord(l)
        # 获得不需要删除的订单，需要修改cus_id为-1
        cur.execute('select id from order_ where cus_id=%s' % id)
        for i in cur.fetchall():
            cur.execute('update order_ set cus_id=-1 where id=%s ' % str(i[0]))
        # 删除顾客本身
        cur.execute('delete from customer where id=%s' % id)
        cur.execute('delete from login where id=%s' % id)
        db.commit()
        cur.close()
        db.close()
        return True

##删除管理
def de_g(phonenum):
    if phonenum.isdigit()==False or len(phonenum)!=11:
        return [False,'电话号码不对']
    db=databaselink()
    cur=db.cursor()
    #此时开始查找该手机号
    cur.execute('select identity from login where phonenum=%s'%phonenum)
    t=cur.fetchall()
    if len(t)==0 or t[0][0]!=3:
        cur.close()
        db.close()
        return [False,'无该手机号或该手机号不是管理员']
    cur.execute('delete from login where phonenum=%s'%phonenum)
    db.commit()
    cur.close()
    db.close()
    return [True,'删除成功']
########################################################33
#登录注册
#查询电话和号码，返回list[true/false(是否可以登录)，type(1,2,3,4分别代表顾客，技师，领导，服务员)，id(该账号id)]
def f1(phone,password):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select pwd,salt,identity,id from login where phonenum=%s'%phone)
    t=cur.fetchall()
    l=list()
    if(len(t)==0):
        l.append('false')
        l.append(' ')
        l.append(' ')
    else:
        salt_bytes=bytes.fromhex(t[0][1])
        password_bytes=password.encode('utf-8')
        n: int = 4
        r: int = 8
        p: int = 16
        # Hash encryption
        password_hash_hex= bytes.hex(hashlib.scrypt(password_bytes, salt=salt_bytes, n=n, r=r, p=p))
        if password_hash_hex==t[0][0]:
            l.append('true')
        else:
            l.append('false')
        l.append(str(t[0][2]))
        l.append(str(t[0][3]))
    return l

#查询顾客库中是否有这个电话，电话是否合法，能否成功注册等等，返回true or false
def f2(name,phone,sex,birth,pa,pa_a):

    db=databaselink()
    cur=db.cursor()
    cur.execute('select* from login where phonenum="%s"'%phone)
    #此时库中有该号码
    if(len(cur.fetchall())):
        return False
    #电话位数
    if phone.isdigit()==False or len(phone)!=11:
        return False
    #name数量多了
    if len(name)>20:
        return False
    #gender
    if(sex!='男' and sex!='女'):
        print(4)
        return False
    salt_bytes: bytes = os.urandom(64)
    password_bytes=pa.encode('utf-8')
    # set corresponding parameters
    n: int = 4
    r: int = 8
    p: int = 16
    # Hash encryption
    password_hash: bytes = hashlib.scrypt(password_bytes, salt=salt_bytes, n=n, r=r, p=p)
    cur.execute('select id from login')
    id_all_tuple=cur.fetchall()
    id_all_list=list()
    for id_t in id_all_tuple:
        id_all_list.append(str(id_t[0]))
    for id in range(100000000):
        if str(id) not in id_all_list :
            cur.execute('insert into login values(%s,"%s","%s",%s,"%s")'%(id,phone,bytes.hex(password_hash),'1',bytes.hex(salt_bytes)))
            cur.execute('insert into customer values(%s,"%s","%s",STR_TO_DATE("%s","%%Y-%%m-%%d"),0,NULL)'%(id,name,sex,birth+'-'+'01'))
            db.commit()
            cur.close()
            db.close()
            return True
    cur.close()
    db.close()
    return False

def alter_pas(phone,old,neww):
    if phone.isdigit()==False or len(phone)!=11:
        return False
    db=databaselink()
    cur=db.cursor()
    cur.execute('select pwd,salt from login where phonenum=%s'%phone)
    t=cur.fetchall()
    if len(t)!=1:
        return False
    a,b,c=f1(phone,old)
    if a=='false':
        cur.close()
        db.close()
        return False
    elif a=='true':
        salt_bytes: bytes = bytes.fromhex(t[0][1])
        password_bytes = neww.encode('utf-8')
        # set corresponding parameters
        n: int = 4
        r: int = 8
        p: int = 16
        # Hash encryption
        password_hash: bytes = hashlib.scrypt(password_bytes, salt=salt_bytes, n=n, r=r, p=p)
        ppp=bytes.hex(password_hash)
        cur.execute('update login set pwd="%s" where phonenum=%s'%(ppp,phone))
        db.commit()
        cur.close()
        db.close()
        return True

#############################################################
###顾客端


##############
# book room
###查询该  #顾客#   id的信息
# 返回list[id,姓名，电话，性别，生日，余额，备注]
def fun_2(id):
    db = databaselink()
    cur = db.cursor()
    cur.execute("select *from customer where id=%s"%id)
    t=cur.fetchall()
    cur.execute('select phonenum from login where id=%s'%id)
    tt=cur.fetchall()
    l=list()
    l.append(str(t[0][0]))
    l.append(t[0][1])
    #电话
    l.append(tt[0][0])

    l.append(t[0][2])
    l.append(str(t[0][3])[0:7])
    l.append(str(t[0][4]))
    l.append(str(t[0][5]))
    db.close()
    return l

#输入顾客id返回顾客的房间预约情况
#这里是已经登录成功的id，肯定合法且存在
#序号为1，2，3，4，5
#[[订单id,房号，日期，开始时间，结束时间]，。。。]
def f5 (id):
    # 获取当前时间
    def add_for(data):
        if data < 10:
            return '0' + str(data)
        return str(data)

    t = time.localtime()
    t_y = str(t.tm_year)

    time_now = t_y + '-' + add_for(t.tm_mon) + '-' + add_for(t.tm_mday) + ' ' + add_for(t.tm_hour) + ':' + add_for(
        t.tm_min) + ':' + add_for(t.tm_sec)
    # 连接数据库
    db=databaselink()
    cur=db.cursor()
    cur.execute('select room_num,start_time,end_time,id from order_ where cus_id=%s and end_time>"%s"'%(id,time_now))
    t=cur.fetchall()
    l=list()
    for i in range(len(t)):
        ll=list()
        ll.append(str(t[i][3]))
        ll.append(str(t[i][0]))
        ll.append(str(t[i][1].year)+'-'+add_for(t[i][1].month)+'-'+add_for(t[i][1].day))
        ll.append(add_for(t[i][1].hour)+':'+add_for(t[i][1].minute))
        ll.append(add_for(t[i][2].hour)+':'+add_for(t[i][2].minute))
        l.append(ll)
    return l

#f5的变种，用于返回当前时间在起始时间之前的所有预约订单信息
def f5_p (id):
    # 获取当前时间
    def add_for(data):
        if data < 10:
            return '0' + str(data)
        return str(data)

    t = time.localtime()
    t_y = str(t.tm_year)

    time_now = t_y + '-' + add_for(t.tm_mon) + '-' + add_for(t.tm_mday) + ' ' + add_for(t.tm_hour) + ':' + add_for(
        t.tm_min) + ':' + add_for(t.tm_sec)
    # 连接数据库
    db=databaselink()
    cur=db.cursor()
    cur.execute('select room_num,start_time,end_time,id from order_ where cus_id=%s and start_time>"%s"'%(id,time_now))
    t=cur.fetchall()
    l=list()
    for i in range(len(t)):
        ll=list()
        ll.append(str(t[i][3]))
        ll.append(str(t[i][0]))
        ll.append(str(t[i][1].year)+'-'+add_for(t[i][1].month)+'-'+add_for(t[i][1].day))
        ll.append(add_for(t[i][1].hour)+':'+add_for(t[i][1].minute))
        ll.append(add_for(t[i][2].hour)+':'+add_for(t[i][2].minute))
        l.append(ll)
    return l
#输入（明天/后天）,开始时间，结束时间，实际人数<=
#如果没有空闲时间返回‘ffffff’，否则返回房号
def f3(date,st,et,type):
    #date=2明天/3后台
    db=databaselink()
    cur=db.cursor()
    alter=int(date)-1
    def add_for(data):
        if data < 10:
            return '0' + str(data)
        return str(data)

    t = time.localtime()
    t_y = str(t.tm_year)

    time_st = t_y + '-' + add_for(t.tm_mon) + '-' + add_for(t.tm_mday) + ' ' + st + ':' + '00'
    time_et=t_y + '-' + add_for(t.tm_mon) + '-' + add_for(t.tm_mday) + ' ' + et + ':' + '00'
    db=databaselink()
    cur=db.cursor()
    print('select num from room where level>=%s and num not in (select room_num from order_ where "%s" between date_add(start_time,interval -%s day) and date_add(end_time,interval -%s day) or "%s" between date_add(start_time,interval -%s day) and date_add(end_time,interval -%s day) ) '%(type,time_st,alter,alter,time_et,alter,alter))
    cur.execute('select num,level from room where level>=%s and num not in (select room_num from order_ where "%s" between date_add(start_time,interval -%s day) and date_add(end_time,interval -%s day) or "%s" between date_add(start_time,interval -%s day) and date_add(end_time,interval -%s day) ) order by level '%(type,time_st,alter,alter,time_et,alter,alter))
    ttt=cur.fetchall()
    if len(ttt)==0:
        return ['ffffff','0']
    cur
    return [str(ttt[0][0]),str(ttt[0][1])]

#返回所有套餐信息
#mes_list=[
#    ['id','按摩套餐',[['产品A','功效'],['产品B','功效'],['产品C','功效']]],
#    ['id','推拿套餐',[['产品A','功效'],['产品B','功效'],['产品C','功效']]],
#         ]
#新的
#mes_list=[
#    ['id','按摩套餐',功效,套餐价格，[['产品A','功效'，产品价格，产品id],['产品B','功效'，产品价格，产品id],['产品C','功效'，产品价格，产品id]]],
#    ['id','推拿套餐',[['产品A','功效'],['产品B','功效'],['产品C','功效']]],
#         ]
def f6():
    db=databaselink()
    cur=db.cursor()
    cur.execute('select id,name,eff,price from package')
    t=cur.fetchall()
    l=list()
    for tt in t:
        ll=list()
        lll=list()
        ll.append(str(tt[0]))
        ll.append(tt[1])
        ll.append(tt[2])
        ll.append(str(tt[3]))
        cur.execute('select name,eff,price,id from product,package_product where quan>0 and pro_id=id and pac_id=%s order by price'%(str(tt[0])))
        ttt=cur.fetchall()
        for tttt in ttt:
            lll.append([tttt[0],tttt[1],str(tttt[2]),str(tttt[3])])
        ll.append(lll)
        l.append(ll)
    return l

#为该合法顾客id增加一个订单
#成功返回True，因为房间不空闲等问题失败返回False
#库存不足问题
#date=1今天/=2明天/=3后天
#type=1/2为房间容纳人数
#list=[[套餐id,产品id,套餐数量]...]
def f7(id,listt,num,st,et,datee):
    print(listt)
    dateee=get_time()[0:10]
    date_st=dateee+' '+st+':00'
    date_et=dateee+' '+et+':00'
    tttt=str(int(datee)-1)
    db=databaselink()
    cur=db.cursor()
    #检测当前房间是否还有效
    print('select * from order_ where room_num=%s and "%s" not between date_add(start_time,interval -%s day) and date_add(end_time,interval -%s day) and "%s" not between date_add(start_time,interval -%s day) and date_add(end_time,interval -%s day)'%(num,date_st,tttt,tttt,date_et,tttt,tttt))
    cur.execute('select * from order_ where room_num=%s and ("%s" between date_add(start_time,interval -%s day) and date_add(end_time,interval -%s day)  or "%s" between date_add(start_time,interval -%s day) and date_add(end_time,interval -%s day))'%(num,date_st,tttt,tttt,date_et,tttt,tttt))
    pp=cur.fetchall()
    if len(pp)!=0:
        print(pp)
        cur.close()
        db.close()
        return [False,'当前房间已被占用']
    #检查库存
    cur.execute('select id,quan,price,name from product')
    all_pro=cur.fetchall()
    money=0
    money_ser=0
    money_pro=0
    #选中套餐总数
    people_should=0
    ms=list()
    for eve in listt:
        print(eve)
        people_should=people_should+int(eve[2])
        #加套餐价格
        cur.execute('select price from package where id=%s'%eve[0])
        ser_money_now=cur.fetchall()[0][0]*int(eve[2])
        ms.append(ser_money_now)
        money_ser=money_ser+ser_money_now
        #加商品价格
        for i in all_pro:
            if i[0]==int(eve[1]):
                money_pro=money_pro+i[2]*int(eve[2])
                ms.append(i[2]*int(eve[2]))
                if i[1]<int(eve[2]):
                    return [False,'%s 库存不足'%i[3]]
                break
    money=money_pro+money_ser
    #检查余额
    cur.execute('select boa from customer where id=%s'%id)
    boa=cur.fetchall()[0][0]
    if boa<money:
        return [False,'余额不足，请充值']
    #检查技师时间
    cur.execute('select technician.id from technician where technician.id not in(select distinct tec_id from order_service,order_ where order_.id=order_Service.order_id and ("%s" between date_add(start_time,interval -%s day) and date_add(end_time,interval -%s day) or "%s" between date_add(start_time,interval -%s day) and date_add(end_time,interval -%s day)))'%(date_st,tttt,tttt,date_et,tttt,tttt))
    tec_now=cur.fetchall()
    if len(tec_now)<people_should:
        return [False,'当前时间段技师不足，请调整套餐数量或者调整时间']
#此时说明订单可下
    #更新money
    cur.execute('update customer set boa=boa-%s where id=%s'%(str(money),id))
    #更新产品的库存
    for eve in listt:
        cur.execute('update product set quan=quan-%s where id=%s'%(eve[2],eve[1]))
    #技师工作时间
    h1=int(et[0:2])-int(st[0:2])
    h2=(int(et[3:5])-int(st[3:5]))/60
    hh=h1+h2
    #创建订单
    cur.execute('select id from order_')
    ord_id_all=cur.fetchall()
    l_all=list()
    for oo in ord_id_all:
        l_all.append(oo[0])
    order_id=0
    for i in range(500000000,1000000000):
        if i not in l_all:
            order_id=i
            break
    if order_id==0:
        return [False,'订单已满，请联系管理员']
    #订单创建好了
    print('insert into order_ values(%s,%s,%s,date_add("%s",interval %s day),date_add("%s",interval %s day))'%(str(order_id),id,num,date_st,tttt,date_et,tttt))
    cur.execute('insert into order_ values(%s,%s,%s,date_add("%s",interval %s day),date_add("%s",interval %s day))'%(str(order_id),id,num,date_st,tttt,date_et,tttt))

    #创建订单服务产品明细
    tec_index=0
    print(listt)
    cnt=0
    for l_now in listt:
        print(l_now)
        while l_now[2]!='0':
            print(1)
            cur.execute('insert into order_service values(%s,%s,%s,%s,%s,%s)'%(str(order_id),l_now[0],str(tec_now[tec_index][0]),l_now[1],str(ms[2*cnt]),str(ms[2*cnt+1])))
            #增加技师工作时间
            cur.execute('update technician set work_hour=work_hour+%s where id=%s'%(str(hh),str(tec_now[tec_index][0])))
            tec_index=tec_index+1
            l_now[2]=str(int(l_now[2])-1)
        cnt=cnt+1
    db.commit()
    cur.close()
    db.close()
    return True
############################
###个人信息修改
#将该id顾客的信息更改为new_list
#new_list=[name,phone,sex,birth,note]
#要检查phone的合法性
#birth格式为2022-12
#生日只考虑到月份
#修改失败返回[False,失败原因字符串]
#理论上失败原因应该只有名字过长或电话不行
def f10(id,name,phone,sex,birth,note):
    if len(name)>20:
        return [False,'名字过长']
    if len(name)==0:
        return [False,'名字没有正确填写']
    if len(phone)!=11:
        return [False,'电话号码长度不正确']
    if len(note)>50:
        return [False,'note过长']
    db=databaselink()
    cur=db.cursor()
    cur.execute('select * from login where phonenum=%s'%phone)
    now=cur.fetchall()
    #原来的手机号
    cur.execute('select phonenum from login where id=%s'%id)
    alter=cur.fetchall()
    if len(now)!=0 and phone!=alter[0][0]:
        return [False,'已存在该手机号']
    cur.execute('update login set phonenum="%s" where id =%s'%(phone,id))
    cur.execute('update customer set name="%s",gender="%s",birthday=STR_TO_DATE("%s","%%Y-%%m"),note="%s" where id=%s'%(name,sex,birth,note,id))
    db.commit()
    return [True]

############################
###选购商品

#返回所有库存不为0商品信息
#list=[名字，单价，id]
def f8():
    db=databaselink()
    cur=db.cursor()
    cur.execute('select name,price,id from food where quan!=0')
    t=cur.fetchall()
    l=list()
    for tt in t:
        l.append([tt[0],str(tt[1]),str(tt[2])])
    return l

#增加一个商品订单
#llist为商品信息=[[商品id,数量]，。。。]
#返回list
#添加成功list0=True,否则为False
#list是订单号

def f9(cus_id,llist,listt):
    if len(llist)==0:
        return [False,'还没有添加商品，请添加商品']
    db=databaselink()
    cur=db.cursor()
    l=list()
    money=0
    for ll in llist:
        cur.execute('select quan,name,price from food where id=%s'%ll[0])
        num=cur.fetchall()
        money=money+num[0][2]*int(ll[1])
        if int(num[0][0])<int(ll[1]):
            return [False,'%s的库存不足'%(num[0][1])]
    cur.execute('select boa from customer where id=%s'%cus_id)
    boa=cur.fetchall()[0][0]
    if boa<money:
        return [False,'余额不足，请充值']
#可以下单了
    #扣款
    cur.execute('update customer set boa=boa-%s where id=%s'%(str(money),cus_id))
    # 获取当前时间
    def add_for(data):
        if data < 10:
            return '0' + str(data)
        return str(data)

    t = time.localtime()
    t_y = str(t.tm_year)

    time_now = t_y + '-' + add_for(t.tm_mon) + '-' + add_for(t.tm_mday) + ' ' + add_for(t.tm_hour) + ':' + add_for(t.tm_min) + ':' + add_for(t.tm_sec)
    print(time_now)
    for ll in llist:
        cur.execute('select price,quan from food where id=%s'%ll[0])

        num,res=cur.fetchall()[0]
        #插入商品订单
        cur.execute('insert into order_food values(%s,%s,"%s",%s,%s,0)'%(listt,ll[0],time_now,str(num),ll[1]))
        #减少商品库存
        cur.execute('update food set quan=%s where id=%s'%(str(res-int(ll[1])),ll[0]))
        db.commit()
    cur.close()
    db.close()
    return [True]

#退订
def del_ord(order_list):
    #获取当前时间
    time_now=get_time()
    db=databaselink()
    cur=db.cursor()
    customer_id=0
    #先检查订单的日期是否还有效退订
    for order_id in order_list:
        cur.execute('select * from order_ where id=%s and start_time>"%s"'%(order_id,time_now))
        if len(cur.fetchall())==0:
            cur.close()
            db.close()
            return [False,'有订单已不可退订']
    #全部检查完毕，开始退订
    for order_id in order_list:
        cur.execute('select cus_id,end_time-start_time,tec_id,pro_id,ser_price+pro_price from order_,order_service,product where order_.id=%s and order_.id=order_service.order_id and pro_id=product.id'%order_id)
        info=cur.fetchall()
        for eve in info:
            customer_id=str(eve[0])
            #余额
            cur.execute('update customer set boa=boa+%s where id=%s'%(str(eve[4]),str(eve[0])))
            #产品库存
            cur.execute('update product set quan=quan+1 where id=%s'%(str(eve[3])))
            #技师工作时间
            print('eee')
            print(eve[1])
            h_h=eve[1]//10000+(eve[1]%10000)/6000
            print(h_h)
            cur.execute('update technician set work_hour=work_hour-%s where id=%s'%(str(h_h),str(eve[2])))
        cur.execute('select food_id,price_byone*num,num from order_food where ord_id=%s'%order_id)
        info=cur.fetchall()
        print(info)
        for eve in info:
            #余额
            cur.execute('update customer set boa=boa+%s where id=%s'%(str(eve[1]),customer_id))
            #库存
            cur.execute('update food set quan=quan+%s where id=%s'%(str(eve[2]),str(eve[0])))
        # 删除产品订单
        cur.execute('delete from order_service where order_id=%s' % order_id)
        cur.execute('delete from order_ where id=%s' % order_id)
        cur.execute('delete from order_food where ord_id=%s'%order_id)
    db.commit()
    cur.close()
    db.close()
    return [True]

###################################
###管理端
#以下均为模糊搜索，输入一个字符串
#搜索顾客返回list=[[id,name,sex,phone]...]
def a2(st):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select id,name,gender,phonenum from login natural join customer where name like "%s%%" or name like "%%%s" or name like "%%%s%%" order by id '%(st,st,st))
    t=cur.fetchall()
    l=list()
    for tt in t:
        l.append([str(tt[0]),tt[1],tt[2],tt[3]])
    cur.close()
    db.close()
    return l
#print(a2('y'))

#输入电话密码判断能否登录
#能登录返回[True,id]
def f11(phone,password):
    print(phone)
    print(password)
    db = databaselink()
    cur = db.cursor()
    cur.execute('select pwd,salt,identity,id from login where phonenum="%s"' % phone)
    t = cur.fetchall()
    l = list()
    if (len(t) == 0):
        l.append(False)
        l.append('无此账号')
    else:
        salt_bytes = bytes.fromhex(t[0][1])
        password_bytes = password.encode('utf-8')
        n: int = 4
        r: int = 8
        p: int = 16
        # Hash encryption
        password_hash_hex = bytes.hex(hashlib.scrypt(password_bytes, salt=salt_bytes, n=n, r=r, p=p))
        if password_hash_hex == t[0][0]:
            l.append(True)
            l.append(str(t[0][3]))
        else:
            l.append(False)
            l.append('密码错误')
    cur.close()
    db.close()
    return l

####改变该顾客的####余额
###无返回
####成功返回True否则False
def fun_3(id, new_money):
    if new_money.isdigit()==False:
        return False
    if int(new_money)<0:
        return False
    db = databaselink()
    cur = db.cursor()
    cur.execute('update customer set boa=%s where id=%s'%(new_money,id))
    db.commit()
    db.close()
    return True

def d1(id):
    db=databaselink()
    cur=db.cursor()
    time_now=get_time()
    #有没有正在进行的订单
    cur.execute('select id from order_ where cus_id=%s and start_time<"%s" and end_time>"%s"'%(id,time_now,time_now))
    if len(cur.fetchall())!=0:
        return False
    #此时开始删除
    cur.execute('select id from order_ where cus_id=%s and start_time>"%s"'%(id,time_now))
    l=list()
    for i in cur.fetchall():
        l.append(str(i[0]))
    #删除预约订单
    del_ord(l)
    #获得不需要删除的订单，需要修改cus_id为-1
    cur.execute('select id from order_ where cus_id=%s'%id)
    for i in cur.fetchall():
        cur.execute('update order_ set cus_id=-1 where id=%s '%str(i[0]))
    #删除顾客本身
    cur.execute('delete from customer where id=%s'%id)
    cur.execute('delete from login where id=%s'%id)
    db.commit()
    cur.close()
    db.close()
    return True

#搜索员工，list=[[id,name,sex,phone,工种，工时]]
#服务员没有工时，直接空值
def a3(st):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select id,name,gender,phonenum,"技师",work_hour from login natural join technician where name like "%s%%" or name like "%%%s" or name like "%%%s%%" order by id'%(st,st,st))
    t_1=cur.fetchall()
    l=list()
    for tt in t_1:
        l.append([str(tt[0]),tt[1],tt[2],tt[3],tt[4],str(tt[5])])

    cur.execute(
        'select id,name,gender,phonenum,"服务员" from login natural join waiter where name like "%s%%" or name like "%%%s" or name like "%%%s%%" order by id' % (
        st, st, st))
    t_1 = cur.fetchall()
    for tt in t_1:
        l.append([str(tt[0]), tt[1], tt[2], tt[3], tt[4], 'None'])

    cur.close()
    db.close()
    return l

#增加员工
#l为 [name0, sex1, phone2, type3, salary4, note5]
def b9(l):
    if len(l[0])>20:
        return [False,'名字过长']
    if l[1]!='男' and l[1]!='女':
        return [False,'性别非法输入']
    if l[2].isdigit()==False or len(l[2])!=11 or int(l[2])<0:
        return [False,'手机号码非法输入']
    if l[4].isdigit()==False or len(l[4])>8 or int(l[4])<=0 :
        return [False,'工资非法输入']
    if len(l[5])>50:
        return [False,'note过长']
    if len(l[5])==0:
        l[5]='NULL'
    #检查手机号是否已存在
    db=databaselink()
    cur=db.cursor()
    cur.execute('select * from login where phonenum="%s"'%l[2])
    if len(cur.fetchall())!=0:
        cur.close()
        db.close()
        return [False,'已存在该手机号']
    #获得密码
    salt_bytes: bytes = os.urandom(64)
    password_bytes = l[2].encode('utf-8')
    # set corresponding parameters
    n: int = 4
    r: int = 8
    p: int = 16
    # Hash encryption
    password_hash: bytes = hashlib.scrypt(password_bytes, salt=salt_bytes, n=n, r=r, p=p)
    #获得职称
    if l[3]=='技师':
        ttt='2'
    else:
        ttt='4'
    print(l[3])
    print(ttt)
    #获得可用id
    cur.execute('select id from login')
    id_all_tuple = cur.fetchall()
    id_all_list = list()
    for id_t in id_all_tuple:
        id_all_list.append(str(id_t[0]))
    for id in range(100000000):
        if str(id) not in id_all_list:
            cur.execute('insert into login values(%s,"%s","%s",%s,"%s")' % (
            id, l[2], bytes.hex(password_hash), ttt, bytes.hex(salt_bytes)))
            if ttt=='2':
                cur.execute('insert into technician values(%s,"%s","%s",0,%s,"%s")' % (id, l[0], l[1],l[4],l[5] ))
            else:
                cur.execute('insert into waiter values(%s,"%s","%s",%s,%s)' % (id, l[0], l[1],l[4],l[5]))
            db.commit()
            re_room()
            cur.close()
            db.close()
            return [True]





#删除员工
def dd1(id):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select identity from login where id=%s'%(id))
    identity=cur.fetchall()[0][0]
    if identity==4:
        cur.execute('select *from login where identity=4')
        if(len(cur.fetchall())==1):
            cur.close()
            db.close()
            return [False,'当前员工为最后一名服务员，不可删除']
        cur.execute('delete from login where id=%s'%id)
        cur.execute('delete from waiter where id=%s'%id)
        re_room()
    elif identity==2:
        time_now=get_time()
        cur.execute('select * from order_,order_service where id=order_id and tec_id=%s and start_time<"%s" and end_time>"%s" '%(id,time_now,time_now))
        if len(cur.fetchall())!=0:
            return [False,'当前技师正在工作，无法删除']
        #获得所有未执行的订单及套餐
        cur.execute('select order_id,pack_id,start_time,end_time from order_,order_service where tec_id=%s and id=order_id and start_time<"%s"'%(id,time_now))
        t=cur.fetchall()
        for i in t :
            st=shift(i[2])
            et=shift(i[3])
            #print('select id from technician where id not in(select distinct tec_id from order_,order_service where order_.id=order_service.order_id and ((start_time>="%s" and start_time<="%s") or (end_time>="%s" and end_time<="%s"))'%(st,et,st,et))
            cur.execute('select id from technician where id not in(select distinct tec_id from order_,order_service where order_.id=order_service.order_id and ((start_time>="%s" and start_time<="%s") or (end_time>="%s" and end_time<="%s")))'%(st,et,st,et))
            alt=cur.fetchall()
            if len(alt)==0:
                #退单
                cur.execute('select cus_id,pro_id,ser_price+pro_price from order_,order_service where order_id=id and order_id=%s and pack_id=%s and tec_id=%s'%(str(i[0]),str(i[1]),id))
                pro_and_price=cur.fetchall()[0]
                #更新顾客余额
                cur.execute('update customer set boa=boa+%s where id=%s'%(str(pro_and_price[2]),str(pro_and_price[0])))
                #更新产品库存
                cur.execute('update product set quan=quan+1 where id=%s'%str(pro_and_price[1]))
                #删除当前订单套餐详细
                cur.execute('delete from order_service where order_id=%s and pack_id=%s and tec_id=%s'%(str(i[0]),str(i[1]),id))
            else:#2022-12-11 14:30:00
                h=str(int(et[11:13])-int(st[11:13])+(int(et[14:16])-int(st[14:16]))/60)
                #转换技师
                t_id=str(alt[0][0])
                    #切换订单技师
                cur.execute('update order_service set tec_id=%s where order_id=%s and pack_id=%s and tec_id=%s'%(t_id,str(i[0]),str(i[1]),id))
                    #更新技师时间
                cur.execute('update technician set work_hour=work_hour+%s where id=%s'%(h,t_id))
        #把以前的订单的技师id改成-1
        cur.execute('select order_id,pack_id from order_service where tec_id=%s'%id)
        for bv in cur.fetchall():
            cur.execute('update order_service set tec_id=%s where order_id=%s and pack_id=%s and tec_id=%s'%(str(out_tec()),str(bv[0]),str(bv[1]),id))
        cur.execute('delete from technician where id=%s'%id)
        cur.execute('delete from login where id=%s'%id)
    db.commit()
    cur.close()
    db.close()
    return [True]

##这个函数改一下，不要工时
#改成list=[id，姓名，性别，电话，工种，底薪，备注]
#id已保证合法
##查询该员工id的信息，
# 返回list[id,姓名，电话，性别，工时，底薪，备注]
def fun_4(id):
    db = databaselink()
    cur = db.cursor()
    cur.execute('select identity,phonenum from login where id=%s' % id)
    i ,phone= cur.fetchall()[0]
    if i==2:
        cur.execute('select id,name,gender,bas_sal,note from technician where id=%s' % id)
    elif i==4:
        cur.execute('select id,name,gender,bas_sal,note from waiter where id=%s' % id)
    t=cur.fetchall()
    l=list()
    print(t)
    l.append(str(t[0][0]))
    l.append(t[0][1])
    l.append(t[0][2])
    l.append(phone)
    if i==2:
        l.append('技师')
    else:
        l.append('服务员')
    l.append(str(t[0][3]))
    l.append(t[0][4])
    cur.close()
    db.close()
    return l

#将该id的员工的信息修改为list
#list=[name0,sex1,phone2,typ3,salary4,note5]
#身份不可改变
#id已确认合法
#修改成功返回id否则[False,]
def bb2(id,listt):
    if len(listt[0])>20 or len(listt[0])==0:
        return [False,'姓名输入过长或未输入']
    if listt[2].isdigit()==False or len(listt[2])!=11:
        return [False,'手机号输入非法']
    if listt[4].isdigit()==False or int(listt[4])<0 or len(listt[4])>8:
        return [False,'工资输入非法']
    if len(listt[5])>50:
        return [False,'note过长']
    if listt[1]!='男' and listt[1]!='女':
        return [False,'性别输入有误']
    db=databaselink()
    cur=db.cursor()
    cur.execute('select phonenum from login where id=%s'%id)
    old=cur.fetchall()[0][0]
    #检查手机号是否存在
    if listt[2]!=old:
        cur.execute('select *from login where phonenum ="%s"'%listt[2])
        if len(cur.fetchall())!=0:
            cur.close()
            db.close()
            return [False,'已存在改手机号']
        #直接去修改手机号
        else:
            cur.execute('update login set phonenum="%s" where id=%s'%(listt[2],id))
    #修改其他信息
    if listt[3]=='技师':
        cur.execute('update technician set name="%s",gender="%s",bas_sal=%s,note="%s" where id=%s'%(listt[0],listt[1],listt[4],listt[5],id))
    elif listt[3]=='服务员':
        cur.execute('update waiter set name="%s",gender="%s",bas_sal=%s,note="%s" where id=%s'%(listt[0],listt[1],listt[4],listt[5],id))
    db.commit()
    cur.close()
    db.close()
    return [True]

#查询该 员工 id是否存在
def b1(id):
    if id.isdigit()==False:
        return False
    if len(id)>11 or len(id)==0:
        return False
    db=databaselink()
    cur=db.cursor()
    cur.execute('select *from login where id=%s and(identity=4 or identity=2)'%id)
    if len(cur.fetchall())==0:
        return False
    return True

#搜索套餐list=[[id,套餐名]]
#前面fun_6是获取所有套餐的信息，可参考
def a4(st):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select id,name,price,eff from package where name like "%s%%" or name like "%%%s" or name like "%%%s%%" '%(st,st,st))
    t=cur.fetchall()
    l=list()
    for tt in t:
        l.append([str(tt[0]),tt[1],str(tt[2]),tt[3]])
    cur.close()
    db.close()
    return l

#返回所有可用产品的id
def b5():
    db=databaselink()
    cur=db.cursor()
    cur.execute('select id,name,price,eff from product order by id')
    l=list()
    for tt in cur.fetchall():
        l.append([str(tt[0]),tt[1],str(tt[2]),tt[3]])
    cur.close()
    db.close()
    return l

#增加套餐
#listt = [name0, price1, pro1 2, pro2 3, pro3 4, eff 5]
def b10(listt):
    if len(listt[0])>20:
        return [False,'name输入过长']
    if listt[1].isdigit()==False or int(listt[1])<=0:
        return [False,'price输入非法']
    if len(listt[5])>50:
        return [False,'功效文字过长']
    if len(listt[2])==0 and len(listt[3])==0 and len(listt[4])==0:
        return [False,'产品选择有问题']
    if listt[2]==listt[3] or listt[2]==listt[4] or listt[3]==listt[4]:
        return [False,'重复选择产品']
    db=databaselink()
    cur=db.cursor()
    #获取合法id
    cur.execute('select id from package')
    id_now_on=list()
    for t in cur.fetchall():
        id_now_on.append(t[0])
    for i in range(400000000,500000000):
        if i not in id_now_on:
            #插入套餐信息
            cur.execute('insert into package values(%s,"%s",%s,"%s")'%(str(i),listt[0],str(listt[1]),listt[5]))
            pro=list()
            #获得将绑定的产品
            if len(listt[2])!=0:
                pro.append(listt[2])
            if len(listt[3])!=0:
                pro.append(listt[3])
            if len(listt[4]) != 0:
                pro.append(listt[4])
            for p in pro:
                cur.execute('insert into package_product values(%s,%s)'%(str(i),p))
            break
    db.commit()
    cur.close()
    db.close()
    return [True]

#搜产品list=[[id,产品名,单价,库存]]
def a5(st):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select id,name,price,quan from product where name like "%s%%" or name like "%%%s" or name like "%%%s%%" order by id '%(st,st,st))
    t=cur.fetchall()
    l=list()
    for tt in t:
        l.append([str(tt[0]),tt[1],str(tt[2]),str(tt[3])])
    cur.close()
    db.close()
    return l

#搜商品list=[[id,商品名,单价,库存]]
#type==1返回食物==2返回酒水
def a6(st,type):
    db = databaselink()
    cur = db.cursor()
    ss=100000000*int(type)
    ee=ss+99999999
    cur.execute(
        'select id,name,price,quan from food where id>=%s and id<=%s and( name like "%s%%" or name like "%%%s" or name like "%%%s%%") order by id' % (
        str(ss),str(ee),st, st, st))
    t = cur.fetchall()
    l = list()
    for tt in t:
        l.append([str(tt[0]), tt[1], str(tt[2]), str(tt[3])])
    cur.close()
    db.close()
    return l
#        list = [name, count, price, eff]
#加产品
def fun_11(listt):
    if len(listt[0])>20 or len(listt[0])==0:
        return [False,'name过长']
    if listt[1].isdigit()==False or int(listt[1])<0:
        return [False,'数量不合法']
    if listt[2].isdigit()==False or int(listt[2])<0 or len(listt[2])>8:
        return [False,'价格不合法']
    if len(listt[3])>50:
        return [False,'功效长度过长']
    db=databaselink()
    cur=db.cursor()
    cur.execute('select id from product')
    pro_all=list()
    for tt in cur.fetchall():
        pro_all.append(tt[0])
    for i in range(300000000,400000000):
        if i not in pro_all:
            cur.execute('insert into product values(%s,"%s",%s,%s,"%s")'%(str(i),listt[0],listt[2],listt[1],listt[3]))
            break
    db.commit()
    cur.close()
    db.close()
    return [True]

#        listt = [type, name, price, count]
#添加商品
def fun_12(listt):
    if len(listt[1])>20 or len(listt[1])==0:
        return [False,'name过长']
    if listt[3].isdigit()==False or int(listt[3])<0:
        return [False,'数量不合法']
    if listt[2].isdigit()==False or int(listt[2])<0 or len(listt[2])>8:
        return [False,'价格不合法']
    db=databaselink()
    cur=db.cursor()
    tn=0
    cur.execute('select id from food')
    food_all=list()
    for tt in cur.fetchall():
        food_all.append(tt[0])
    if listt[0]=='食物':
        tn=0
    else:
        tn=100000000
    for i in range(100000000+tn,200000000+tn):
        if i not in food_all:
            cur.execute('insert into food values(%s,"%s",%s,%s)'%(str(i),listt[1],listt[2],listt[3]))
            break
    db.commit()
    cur.close()
    db.close()
    return [True]

#查询该套餐id是否存在，返回True or False
def b3(id):
    if id.isdigit()==False:
        return False
    db=databaselink()
    cur=db.cursor()
    cur.execute('select * from package where id=%s'%id)
    if len(cur.fetchall())==0:
        return False
    return True

#查询该合法套餐id的信息
#返回list=[id,名字,产品Aid,Bid,Cid,价格，功效]
#产品可为空值
def bb4(id):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select id,name,price,eff from package where id=%s'%id)
    pa=cur.fetchall()[0]
    cur.execute('select pro_id from package_product where pac_id=%s'%id)
    ttt=list()
    for tt in cur.fetchall():
       ttt.append(str(tt[0]))
    while len(ttt)!=3:
        ttt.append('')
    return [id,pa[1]]+ttt+[str(pa[2]),pa[3]]

#list = [name, price, pro1, pro2, pro3, eff]
#修改套餐信息
def b6(id,listt):
    if len(listt[0])>20 or len(listt[0])==0:
        return [False,'name过长']
    if listt[1].isdigit()==False or int(listt[1])<0 or len(listt[1])>8:
        return [False,'价格不合法']
    if len(listt[5])>50:
        return [False,'功效字数过长']
    db=databaselink()
    cur=db.cursor()
    cur.execute('update package set name="%s",price=%s,eff="%s" where id=%s'%(listt[0],str(listt[1]),listt[5],id))
    db.commit()
    cur.close()
    db.close()
    return [True]

#删除package,product,food
def d2(id):
    db=databaselink()
    cur=db.cursor()
    #查询当前是否有人使用
    time_now=get_time()
    #对套餐进行识别
    cur.execute('select* from order_,order_service where pack_id=%s and id=order_id and "%s">=start_time and "%s"<=end_time'%(id,time_now,time_now))
    if len(cur.fetchall())!=0:
        cur.close()
        db.close()
        return [False,'删除失败，套餐正在使用']
    #对product进行识别
    cur.execute(
        'select* from order_,order_service where pro_id=%s and id=order_id and "%s">=start_time and "%s"<=end_time' % (
        id, time_now, time_now))
    if len(cur.fetchall()) != 0:
        cur.close()
        db.close()
        return [False, '删除失败，产品正在使用']
    #对food进行识别
    cur.execute(
        'select* from order_,order_food where food_id=%s and id=ord_id and "%s">=start_time and "%s"<=end_time' % (
        id, time_now, time_now))
    if len(cur.fetchall()) != 0:
        cur.close()
        db.close()
        return [False, '删除失败，套餐正在使用']

    #当前可删除
    if int(id)>=400000000:
        #对以前的套餐操作
        cur.execute('update order_service set pack_id=-1 where pack_id=%s and order_id in(select a.u from((select order_.id u from order_,order_Service where order_.id=order_service.order_id and end_time<"%s")) a)'%(id,time_now))
          #对将来的套餐进行操作
              #获取顾客id0,订单号1,技师号2,产品号3，总价格4,时间5
        cur.execute('select cus_id,id,tec_id,pro_id,ser_price+pro_price,end_time-start_time from order_,order_service where id=order_id and pack_id=%s and start_time>"%s"'%(id,time_now))
        for tt in cur.fetchall():
                    #返还顾客余额
            cur.execute('update customer set boa=boa+%s where id=%s'%(str(tt[4]),str(tt[0])))
                    #返还技师time
            h=str(int(tt[5])/6000)
            cur.execute('update technician set work_hour=work_hour-%s where id=%s'%(h,str(tt[0])))
                    #返还pro的quan
            cur.execute('update product set quan=quan+1 where id=%s'%str(tt[3]))
                    #删除订单套餐
                        #如果该订单没有套餐了，那么同样不可删除
            cur.execute('select *from order_service where order_id=%s'%str(tt[1]))
            if(len(cur.fetchall())==1):
                cur.close()
                db.close()
                return [False,'删除失败,当前套餐被唯一拥有']
            cur.execute('delete from order_service where order_id=%s and pack_id=%s and tec_id=%s'%(tt[1],id,tt[2]))
            #删除套餐本身以及套餐绑定的pro
        cur.execute('delete from package_product where pac_id=%s'%(id))
        cur.execute('delete from package where id=%s'%id)
    #产品
    elif int(id)>=300000000:
        #判定当前产品是否被某个套餐唯一绑定
        cur.execute('select pac_id,count(pro_id) from package_product where pac_id in (select pac_id  from package_product where pro_id=%s) order by pac_id'%id)
        for lk in cur.fetchall():
            if lk[1]==1:
                cur.close()
                db.close()
                return[False,'当前产品被某个套餐唯一绑定，不可删除该产品']
        # 对以前的产品操作
        cur.execute(
            'update order_service set pro_id=-1 where pro_id=%s and order_id in(select a.u from((select order_.id u from order_,order_Service where order_.id=order_service.order_id and end_time<"%s")) a)' % (
            id, time_now))
        # 对将来的套餐进行操作
        # 获取顾客id0,订单号1,技师号2,产品号3，总价格4,时间5,套餐号6
        cur.execute(
            'select cus_id,id,tec_id,pro_id,ser_price+pro_price,end_time-start_time,pack_id from order_,order_service where id=order_id and pro_id=%s and start_time>"%s"' % (
            id, time_now))
        for tt in cur.fetchall():
            # 返还顾客余额
            cur.execute('update customer set boa=boa+%s where id=%s' % (str(tt[4]), str(tt[0])))
            # 返还技师time
            h = str(int(tt[5]) / 6000)
            cur.execute('update technician set work_hour=work_hour-%s where id=%s' % (h, str(tt[0])))
            # 返还pro的quan
            cur.execute('update product set quan=quan+1 where id=%s' % str(tt[3]))
            # 删除订单套餐
            # 如果该订单没有套餐了，那么同样不可删除
            cur.execute('select *from order_service where order_id=%s' % str(tt[1]))
            if (len(cur.fetchall()) == 1):
                cur.close()
                db.close()
                return [False, '删除失败,当前产品被唯一拥有']
            cur.execute('delete from order_service where order_id=%s and pack_id=%s and tec_id=%s' % (str(tt[1]), str(tt[6]), str(tt[2])))
            # 删除套餐本身以及套餐绑定的pro
        cur.execute('delete from package_product where pro_id=%s' % (id))
        cur.execute('delete from product where id=%s' % id)
    #商品
    elif int(id)>=100000000:
        # 对以前的商品操作
        cur.execute(
            'update order_food set food_id=%s where food_id=%s and ord_id in(select a.u from((select order_.id u from order_ where end_time<"%s")) a)' % (
            str(out_order_food()),id, time_now))
        # 对将来的商品进行操作
        # 获取顾客id0,订单号1,总价格2
        cur.execute(
            'select cus_id,order_.id,num*price_byone from order_,order_food where order_.id=ord_id and food_id=%s and start_time>"%s"' % (
            id, time_now))
        for tt in cur.fetchall():
            # 返还顾客余额
            cur.execute('update customer set boa=boa+%s where id=%s' % (str(tt[2]), str(tt[0])))
            #删除order_food订单
            cur.execute('delete from order_food where ord_id=%s and food_id=%s' % (str(tt[1]),id))
            # 删除food本身
        cur.execute('delete from food where id=%s' % id)
    #全部处理完了才commit
    db.commit()
    cur.close()
    db.close()
    return [True]

#查询该产品id是否存在
def b7(id):
    if id.isdigit()==False:
        return False
    db=databaselink()
    cur=db.cursor()

    cur.execute('select *from product where id=%s'%id)
    if len(cur.fetchall())==0:
        return False
    return True


#产品最后还要多加一个功效
# 查询产品or商品ID
# 返回list=[id,name,price,库存]
def fun_9(id):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select id,name,price,quan from food where id=%s'%id)
    t=cur.fetchall()
    l=list()
    if(len(t)==1):
        for tt in t[0]:
            l.append(str(tt))
    else:
        cur.execute('select id,name,price,quan,eff from product where id=%s' % id)
        t = cur.fetchall()
        if (len(t) == 1):
            for tt in t[0]:
                l.append(str(tt))
    cur.close()
    db.close()
    return l

#修改成功返回id否则'-1'
# 将对应id的产品or商品信息修改为
# new_list[id,名字,价格,库存]
#产品的new_list最后还有个功效
#id合法
def fun_10(new_list):
    # new_list[0]为id,不会改变
    #判断数据是否合法
    if len(new_list[1])>20 or len(new_list[1])==0:
        return [False,'名字不合法']
    elif new_list[2].isdigit()==False or int(new_list[2])<0:
        return [False,'价格不合法']
    elif new_list[3].isdigit()==False or int(new_list[3])<0:
        return [False,'库存不合法']
    else:
        db = databaselink()
        cur = db.cursor()
        #确定商品，产品并修改
        if int(new_list[0])<300000000:
            cur.execute('update food set name="%s",price=%s,quan=%s where id=%s'%(new_list[1],new_list[2],new_list[3],new_list[0]))
        else:
            if len(new_list[4])>50:
                cur.close()
                db.close()
                return[False,'功效过长']
            cur.execute('update product set name="%s",price=%s,quan=%s,eff="%s" where id=%s'%(new_list[1],new_list[2],new_list[3],new_list[4],new_list[0]))
    db.commit()
    cur.close()
    db.close()
    return [True]

#查询该商品id是否存在
def b8(id):
    if id.isdigit()==False:
        return False
    db=databaselink()
    cur=db.cursor()
    cur.execute('select *from food where id=%s '%id)
    if len(cur.fetchall())==0:
        return False
    cur.close()
    db.close()
    return True

#查询商品
def fun_99(id):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select id,name,price,quan from food where id=%s'%(id))
    l=list()
    for tt in cur.fetchall()[0]:
        l.append(str(tt))
    if int(id)<200000000:
        l.append('食物')
    else:
        l.append('酒水')
    return l

#查看所有房间
def room_all():
    db=databaselink()
    cur=db.cursor()
    cur.execute('select num,level,waiter_id,name from room,waiter where room.waiter_id=waiter.id')
    l=list()
    for i in cur.fetchall():
        l.append([str(i[0]),str(i[1]),str(i[2]),i[3]])
    cur.close()
    db.close()
    return l

#2022-01-01
def a1(datee):
    print(datee)
    if len(datee)!=10:
        print(1)
        return [False,'请输入完整日期']
    if datee[0:4].isdigit()==False or datee[5:7].isdigit()==False or datee[8:10].isdigit()==False:
        print(2)
        return [False,'请输入正确的日期']
    if isvalid(datee[0:4],datee[5:7],datee[8:10])==False:
        print(3)
        return [False, '日期不合法']
    db=databaselink()
    cur=db.cursor()
    cur.execute('select room_num,level,start_time,end_time from order_,room where room.num=order_.room_num and start_time>="%s" and end_time<date_add("%s",interval 1 day) order by level,room_num'%(datee,datee))
    l=list()
    for i in cur.fetchall():
        l.append([str(i[0]),str(i[1]),add_for(i[2].hour)+':'+add_for(i[2].minute)+'-'+add_for(i[3].hour)+':'+add_for(i[3].minute)])
    return l

#年营业额
def year_money(year):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select sum(ser_price),sum(pro_price) from order_,order_service where order_.id=order_Service.order_id and start_time>="%s" and end_time<date_add("%s",interval 1 year)'%(year+'-01-01',year+'-01-01'))
    ser_p,pro_p=cur.fetchall()[0]
    cur.execute('select sum(price_byone*num) from order_,order_food where order_.id=order_food.ord_id and start_time>="%s" and end_time<date_add("%s",interval 1 year)'%(year+'-01-01',year+'-01-01'))
    good_p=cur.fetchall()[0][0]
    cur.close()
    db.close()
    if ser_p is None:
        ser_p=0
    if pro_p is None:
        pro_p=0
    if good_p is None:
        good_p=0
    return [str(ser_p),str(pro_p),str(good_p)]

#月营业额
def month_money(year,month):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select sum(ser_price),sum(pro_price) from order_,order_service where order_.id=order_Service.order_id and start_time>="%s" and end_time<date_add("%s",interval 1 month)'%(year+'-'+month+'-01',year+'-'+month+'-01'))
    ser_p,pro_p=cur.fetchall()[0]
    cur.execute('select sum(price_byone*num) from order_,order_food where order_.id=order_food.ord_id and start_time>="%s" and end_time<date_add("%s",interval 1 month)'%(year+'-'+month+'-01',year+'-'+month+'-01'))
    good_p=cur.fetchall()[0][0]
    cur.close()
    db.close()
    if ser_p is None:
        ser_p=0
    if pro_p is None:
        pro_p=0
    if good_p is None:
        good_p=0
    return [str(ser_p),str(pro_p),str(good_p)]


#################################################################3
###员工端

# 检测该员工id返回工种
# id合法
def c1(id):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select identity from login where id=%s'%id)
    t=cur.fetchall()
    if t[0][0]==2:
        return '技师'
    elif t[0][0]==4:
        return '服务员'


# 查询该技师id，返回list
# list=[[房号，开始时间，结束时间，套餐集合]]
# 套餐集合为[[套餐id,产品id]...]
# list=[
# ['123','14:30','15:30',[['147','001'],['258','002']]],
# ['125','15:30','16:30',[['147','001'],['258','003']],]
##预约或正在进行中
#list=[
# ['123','14:30','15:30',['147','001']],
# ['125','15:30','16:30',['147','001'],]
def c2(id):
    def add_for(data):
        if data < 10:
            return '0' + str(data)
        return str(data)
    def shift(dt):
        return add_for(dt.year)+'-'+add_for(dt.month)+'-'+add_for(dt.day)+' '+add_for(dt.hour)+':'+add_for(dt.minute)+':'+add_for(dt.second)
    db=databaselink()
    cur=db.cursor()

    time_now=get_time()
    cur.execute('select room_num,start_time,end_time,package.name,product.name from order_,order_service,package,product where order_.id=order_id and tec_id=%s and end_time>"%s" and package.id=order_service.pack_id and order_service.pro_id=product.id '%(id,time_now))
    t=cur.fetchall()
    l=list()
    for tt in t:
        l.append([str(tt[0]),shift(tt[1]),shift(tt[2]),[str(tt[3]),str(tt[4])]])
    cur.close()
    db.close()
    return l

# 根据该技师合法id返回list
# list=[id,name,sex,phone,工种,note,work_time,salary]
def c4(id):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select id,name,gender,phonenum,"技师",note,work_hour,bas_sal from technician natural left outer join login where id=%s'%id)
    l=list()
    for i in cur.fetchall()[0]:
        l.append(str(i))
    print(l)
    return l


# 根据该服务员合法id返回list
# list=[id,name,sex,phone,工种,note,salary]
def c5(id):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select waiter.id,waiter.name,gender,phonenum,"服务员",note,bas_sal from waiter natural left outer join login where id=%s'%id)
    l=list()
    for i in cur.fetchall()[0]:
        l.append(str(i))
    return l

# 查询该服务员id，返回list
# 商品集合包括[[商品名,数量，商品id]......]
# 数量也是字符串
# work_list=[房号,订单号
#      ['2022-12-28 20:11',[商品集合]],
#       ['2022-12-28 20:20',[商品集合]],
# ]
# 没有工作安排直接返回False
def c3(id):
    def add_for(data):
        if data < 10:
            return '0' + str(data)
        return str(data)
    def shift(dt):
        return add_for(dt.year)+'-'+add_for(dt.month)+'-'+add_for(dt.day)+' '+add_for(dt.hour)+':'+add_for(dt.minute)+':'+add_for(dt.second)

    db=databaselink()
    cur=db.cursor()
    time_now=get_time()
    cur.execute('select room.num,order_.id from waiter,room,order_,order_food where waiter.id=%s and waiter.id=room.waiter_id and order_.room_num=room.num and order_.id=order_food.ord_id and order_.start_time<="%s" and order_.end_time>="%s" and order_food.state=0'%(id,time_now,time_now))
    t=cur.fetchall()
    if len(t)==0:
        cur.close()
        db.close()
        return False
    ans=list()
    room_num=t[0][0]
    ans.append(str(room_num))
    ans.append(str(t[0][1]))
    cur.execute('select order_food.time,food.name,order_food.num,food.id from order_food,food where order_food.ord_id=%s and order_food.food_id=food.id and state=0 order by time'%(str(t[0][1])))
    tt=cur.fetchall()
    ll=list()
    food=list()
    datee=' '
    for eve in tt:
        d=shift(eve[0])
        #当前日期不是之前的日期
        if datee!=d:
            if datee!=' ':
                ll.append(food)
                ans.append(ll)
                ll=list()
                food=list()
            datee = d
            ll.append(datee)
        food.append([eve[1],str(eve[2]),str(eve[3])])
    ll.append(food)
    ans.append(ll)
    print(ans)
    return ans
#未调试


# 将已完成work_list传入，传出新work_list
# 格式同上
# id是服务员id
# 商品集合包括[[商品名,数量，商品id]......]
# 数量也是字符串
# work_list=[房号,订单号
#      ['2022-12-28 20:11',[商品集合]],
#       ['2022-12-28 20:20',[商品集合]],
# ]
def c33(id, work_list):
    print(work_list)
    if work_list==False:
        return c3(id)
    db=databaselink()
    cur=db.cursor()
    order_id=work_list[1]
    for tt in work_list[2:]:
        time_=tt[0]
        for ttt in tt[1]:
            idn=ttt[2]
            cur.execute('update order_food set state=1 where ord_id=%s and food_id=%s and time="%s"'%(order_id,idn,time_))

    db.commit()
    cur.close()
    db.close()
    return c3(id)

def remind():
    db=databaselink()
    cur=db.cursor()
    l=list()
    cur.execute('select id,name from product where quan=0')
    for tt in cur.fetchall():
        l.append([str(tt[0]),tt[1],'产品'])
    cur.execute('select id,name from food where quan=0')
    for tt in cur.fetchall():
        l.append([str(tt[0]),tt[1],'商品'])
    return l

#def del_food(id):
def seek_order_all(id):
    # 输入顾客id返回顾客的房间预约情况
    # 这里是已经登录成功的id，肯定合法且存在
    # 序号为1，2，3，4，5
    # [[订单id,房号，日期，开始时间，结束时间]，。。。]
    db=databaselink()
    cur=db.cursor()
    l=f5(id)
    for i in range(len(l)):
        cur.execute('select sum(price_byone*num) from order_food where ord_id=%s'%l[i][0])
        m1=cur.fetchall()[0][0]
        if m1 is None:
            m1=0
        cur.execute('select sum(ser_price+pro_price) from order_service where order_id=%s'%l[i][0])
        m2=cur.fetchall()[0][0]
        print(m2)
        l[i].append('%s'%str(m1+m2))
    cur.close()
    db.close()
    print(l)
    return l

#根据订单id返回套餐
def pac_by_id(id):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select package.name,product.name,ser_price,pro_price,technician.name from order_service,technician,package,product where pack_id=package.id and tec_id=technician.id and pro_id=product.id and order_id=%s'%id)
    l=list()
    ttt=cur.fetchall()
    print(ttt)
    for i in ttt:
        l.append([i[0],i[1],str(i[2]),str(i[3]),i[4]])
    cur.close()
    db.close()
    print(l)
    return l


# 商品名，下单时间，单价，数量，食物id，状态
def seek_order_food(id):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select name,time,price_byone,num,food_id,state from order_food,food where food_id=id and ord_id=%s'%id)
    l=list()
    for i in cur.fetchall():
        ty=''
        if i[5]==0:
            ty='未完成'
        else:
            ty='已完成'
        l.append([i[0],shift(i[1]),str(i[2]),str(i[3]),str(i[4]),ty])
    cur.close()
    db.close()
    return l

def delete_good(order_id,food_id,t,cus_id):
    db=databaselink()
    cur=db.cursor()
    cur.execute('select price_byone,num,state from order_food where ord_id=%s and food_id=%s and time="%s"'%(order_id,food_id,t))
    i=cur.fetchall()[0]
    #此时商品已送达
    if i[2]==1:
        cur.close()
        db.close()
        return [False,'当前商品已送达，不可退单']
    #该商品未送达
        #更新顾客余额
    cur.execute('update customer set boa=boa+%s where id=%s'%(str(i[0]*i[1]),cus_id))
        #更新商品库存
    cur.execute('update food set quan=quan+%s where id=%s'%(str(i[1]),food_id))
        #删除该单
    cur.execute('delete from order_food where ord_id=%s and food_id=%s and time="%s"'%(order_id,food_id,t))
    db.commit()
    cur.close()
    db.close()
    return [True]





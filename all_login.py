from database import *


# 登录界面
class login:
    def __init__(self):
        self.frame_new = tk.Frame(root, bg='white')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/else/登录页面.png")
        ttk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=0 * 40, y=0 * 40, width=864, height=576)
        phone = tk.StringVar()
        password = tk.StringVar()
        # 电话，密码的输入框
        self.en1 = ttk.Entry(self.frame_new, textvariable=phone)
        self.en1.place(x=14 * 40, y=6.2 * 40, width=3.8 * 40, height=0.5 * 40)
        self.en2 = ttk.Entry(self.frame_new, textvariable=password, show='*')
        self.en2.place(x=14 * 40, y=8 * 40, width=3.8 * 40, height=0.5 * 40)
        # 登录，注册按钮
        self.yes = ttk.Button(self.frame_new, text='登录', command=lambda: self.yess(phone.get(), password.get()))
        self.yes.place(x=17 * 40, y=9.5 * 40, width=1 * 40, height=0.75 * 40)
        self.no = ttk.Button(self.frame_new, text='注册', command=self.reg)
        self.no.place(x=11.5 * 40, y=9.5 * 40, width=1 * 40, height=0.75 * 40)
        self.forget = ttk.Button(self.frame_new, text='忘记密码', command=self.forget_pa)
        self.forget.place(x=11.5 * 40 + 40, y=9.5 * 40, width=1.5 * 40, height=0.75 * 40)
        self.change = ttk.Button(self.frame_new, text='修改密码', command=self.change_pa)
        self.change.place(x=11.5 * 40 + 40 + 1.5 * 40, y=9.5 * 40, width=1.5 * 40, height=0.75 * 40)

    def yess(self, phone, password):

        # 查询电话和号码，返回list[true/false(是否可以登录)，type(1,2,3分别代表顾客员工领导)，id(该账号id)]
        this_list = f1(phone, password)
        # this_list = ['true', '1', '123']
        if (this_list[0] == 'true'):
            if this_list[1] == '1':
                # 顾客端
                customer_1(this_list[2])
            elif this_list[1] == '2':
                # 员工端
                yuangong(this_list[2])
            elif this_list[1] == '3':
                # 管理端
                guanli()
            elif this_list[1] == '4':
                # 员工端
                yuangong(this_list[2])
        else:
            login_false()

    def reg(self):
        register()

    def forget_pa(self):
        ttk.Label(self.frame_new, text='请前往前台修改密码', background='#FEFCE0').place(x=11.5 * 40 + 40, y=5 * 40,
                                                                                width=5 * 40, height=0.75 * 40)

    def change_pa(self):
        change_pa()


# 修改密码界面
class change_pa:
    def __init__(self):
        self.frame_new = tk.Frame(root, bg='white')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/else/修改密码.png")
        tk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=0 * 40, y=0 * 40, width=864, height=576)
        # 电话，密码的输入框
        self.phone = tk.StringVar()
        self.password = tk.StringVar()
        self.new_password = tk.StringVar()
        self.en1 = ttk.Entry(self.frame_new, textvariable=self.phone)
        self.en1.place(x=12 * 40, y=5.8 * 40, width=5.9 * 40, height=0.5 * 40)
        self.en2 = ttk.Entry(self.frame_new, textvariable=self.password, show='*')
        self.en2.place(x=12 * 40, y=7.1 * 40, width=5.9 * 40, height=0.5 * 40)
        self.en3 = ttk.Entry(self.frame_new, textvariable=self.new_password, show='*')
        self.en3.place(x=12 * 40, y=8.3 * 40, width=5.9 * 40, height=0.5 * 40)
        self.change = ttk.Button(self.frame_new, text='修改', command=self.change)
        self.change.place(x=11.5 * 40 + 40 + 1.5 * 40, y=9.5 * 40, width=1.5 * 40, height=0.75 * 40)
        self.ret = ttk.Button(self.frame_new, text='返回', command=self.ret)
        self.ret.place(x=11.5 * 40 + 40 + 1.5 * 80, y=9.5 * 40, width=1.5 * 40, height=0.75 * 40)

    def change(self):
        phone = self.phone.get()
        pa = self.password.get()
        new_pa = self.new_password.get()
        # 传入返回能否被修改
        #
        k = alter_pas(phone, pa, new_pa)
        if k == True:
            ttk.Label(self.frame_new, text='修改成功', background='#FEFCE0').place(x=11.5 * 40 + 40, y=4.5 * 40,
                                                                               width=5 * 40, height=0.75 * 40)
        else:
            ttk.Label(self.frame_new, text='修改失败，电话或密码填写错误', background='#FEFCE0').place(x=11.5 * 40 + 40, y=4.5 * 40,
                                                                                         width=5 * 40, height=0.75 * 40)

    def ret(self):
        login()


# 登录失败界面
class login_false:
    def __init__(self):
        self.frame_new = tk.Frame(root, bg='white')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/else/登录失败.png")
        tk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.phone = tk.StringVar()
        self.password = tk.StringVar()
        # 电话，密码的输入框
        self.en1 = ttk.Entry(self.frame_new, textvariable=self.phone)
        self.en1.place(x=14 * 40, y=6.2 * 40, width=3.8 * 40, height=0.5 * 40)
        self.en2 = ttk.Entry(self.frame_new, textvariable=self.password, show='*')
        self.en2.place(x=14 * 40, y=8 * 40, width=3.8 * 40, height=0.5 * 40)
        # 登录，注册按钮
        self.yes = ttk.Button(self.frame_new, text='登录',
                              command=lambda: self.yess(self.phone.get(), self.password.get()))
        self.yes.place(x=17 * 40, y=9.5 * 40, width=1.5 * 40, height=0.75 * 40)
        self.no = ttk.Button(self.frame_new, text='注册', command=self.reg)
        self.no.place(x=11.5 * 40, y=9.5 * 40, width=1.5 * 40, height=0.75 * 40)

    def yess(self, phone, password):

        # 查询电话和号码，返回list[true/false(是否可以登录)，type(1,2,3分别代表顾客员工领导)，id(该账号id)]
        this_list = f1(phone, password)
        # this_list=search(phone,password)
        # this_list = ['true', '1', '123']
        if (this_list[0] == 'true'):
            if this_list[1] == '1':
                # 顾客端
                customer_1(this_list[2])
            elif this_list[1] == '2':
                # 员工端
                yuangong(this_list[2])
            elif this_list[1] == '3':
                # 管理端
                guanli()
            elif this_list[1] == '4':
                # 员工端
                yuangong(this_list[2])
        else:
            return

    def reg(self):
        register()


# 注册界面，这里只能为顾客注册，员工和管理需要管理端注册
class register:
    def __init__(self):
        self.frame_new = tk.Frame(root, bg='white')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/else/注册.png")
        tk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.name = tk.StringVar()
        self.phone = tk.StringVar()
        self.sex = tk.StringVar()
        self.sex.set('男')
        self.birth1 = tk.StringVar()
        self.birth2 = tk.StringVar()
        self.password = tk.StringVar()
        self.password_again = tk.StringVar()
        # 名字，电话，性别，生日，密码，确认密码的输入框
        self.en1 = ttk.Entry(self.frame_new, textvariable=self.name)
        self.en1.place(x=14 * 40, y=2.6 * 40, width=3.8 * 40, height=0.5 * 40)
        self.en2 = ttk.Combobox(self.frame_new, textvariable=self.sex, values=['男', '女'])
        self.en2.place(x=14 * 40, y=3.75 * 40, width=3.8 * 40, height=0.5 * 40)
        self.en3 = ttk.Entry(self.frame_new, textvariable=self.phone)
        self.en3.place(x=14 * 40, y=5 * 40, width=3.8 * 40, height=0.5 * 40)
        self.en4 = ttk.Combobox(self.frame_new, state='readonly', textvariable=self.birth1, values=[
            '1930', '1931', '1932', '1933', '1934', '1935', '1936',
            '1937', '1938', '1939', '1940', '1941', '1942', '1943',
            '1944', '1945', '1946', '1947', '1948', '1949', '1950',
            '1951', '1952', '1953', '1954', '1955', '1956', '1957',
            '1958', '1959', '1960', '1961', '1962', '1963', '1964',
            '1965', '1966', '1967', '1968', '1969', '1970', '1971',
            '1972', '1973', '1974', '1975', '1976', '1977', '1978',
            '1979', '1980', '1981', '1982', '1983', '1984', '1985',
            '1986', '1987', '1988', '1989', '1990', '1991', '1992',
            '1993', '1994', '1995', '1996', '1997', '1998', '1999',
            '2000', '2001', '2002', '2003', '2004', '2005', '2006',
            '2007', '2008', '2009', '2010', '2011', '2012', '2013',
            '2014', '2015', '2016', '2017', '2018', '2019', '2020',
            '2021', '2022', '2023'])
        self.en4.place(x=14 * 40, y=6.2 * 40, width=3.8 * 20, height=0.5 * 40)
        self.en44 = ttk.Combobox(self.frame_new, state='readonly', textvariable=self.birth2, values=[
            '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
        self.en44.place(x=14 * 40 + 3.8 * 20, y=6.2 * 40, width=3.8 * 20, height=0.5 * 40)
        self.en5 = ttk.Entry(self.frame_new, textvariable=self.password, show='*')
        self.en5.place(x=14 * 40, y=7.85 * 40, width=3.8 * 40, height=0.5 * 40)
        self.en6 = ttk.Entry(self.frame_new, textvariable=self.password_again, show='*')
        self.en6.place(x=14 * 40, y=9.46 * 40, width=3.8 * 40, height=0.5 * 40)
        # 确认注册和返回按钮，确认注册后要核查数据合法性返回界面
        self.yes = ttk.Button(self.frame_new, text='注册', command=self.re)
        self.yes.place(x=17 * 40, y=10.5 * 40, width=1.5 * 40, height=0.75 * 40)
        self.no = ttk.Button(self.frame_new, text='返回', command=self.turn)
        self.no.place(x=11.5 * 40, y=10.5 * 40, width=1.5 * 40, height=0.75 * 40)

    def turn(self):
        login()

    def re(self):
        name = self.name.get()
        phone = self.phone.get()
        sex = self.sex.get()
        birth = self.birth1.get() + '-' + self.birth2.get()
        pa = self.password.get()
        pa_a = self.password_again.get()
        # 首先判断两次密码输入是否相等
        if pa == pa_a:
            check = f2(name, phone, sex, birth, pa, pa_a)
            # check=True
            if check == False:
                register_again(name, phone, sex, birth, pa, pa_a, 2)
            else:
                register_success()
        else:
            register_again(name, phone, sex, birth, pa, pa_a, 1)


# 注册界面again，上一次输入有误检测后出这个界面
class register_again:
    def __init__(self, name, phone, sex, birth, pa, pa_a, type):
        print('this')
        self.frame_new = tk.Frame(root, bg='white')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/else/注册.png")
        tk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        if type == 1:
            ttk.Label(self.frame_new, text='两次密码不一致').place(x=600, y=405, width=90, height=17)
        else:
            ttk.Label(self.frame_new, text='其他信息有误').place(x=600, y=405, width=90, height=17)
        self.frame_new.place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.name = tk.StringVar()
        self.phone = tk.StringVar()
        self.sex = tk.StringVar()
        self.birth1 = tk.StringVar()
        self.birth2 = tk.StringVar()
        self.password = tk.StringVar()
        self.password_again = tk.StringVar()

        self.name.set(name)
        self.phone.set(phone)
        self.sex.set(sex)
        self.birth1.set(birth[0:4])
        self.birth2.set(birth[5:7])
        self.password.set(pa)
        self.password_again.set(pa_a)
        # 名字，电话，性别，生日，密码，确认密码的输入框
        self.en1 = ttk.Entry(self.frame_new, textvariable=self.name)
        self.en1.place(x=14 * 40, y=2.6 * 40, width=3.8 * 40, height=0.5 * 40)
        self.en2 = ttk.Combobox(self.frame_new, textvariable=self.sex, values=['男', '女'])
        self.en2.place(x=14 * 40, y=3.75 * 40, width=3.8 * 40, height=0.5 * 40)
        self.en3 = ttk.Entry(self.frame_new, textvariable=self.phone)
        self.en3.place(x=14 * 40, y=5 * 40, width=3.8 * 40, height=0.5 * 40)
        self.en4 = ttk.Combobox(self.frame_new, state='readonly', textvariable=self.birth1, values=[
            '1930', '1931', '1932', '1933', '1934', '1935', '1936',
            '1937', '1938', '1939', '1940', '1941', '1942', '1943',
            '1944', '1945', '1946', '1947', '1948', '1949', '1950',
            '1951', '1952', '1953', '1954', '1955', '1956', '1957',
            '1958', '1959', '1960', '1961', '1962', '1963', '1964',
            '1965', '1966', '1967', '1968', '1969', '1970', '1971',
            '1972', '1973', '1974', '1975', '1976', '1977', '1978',
            '1979', '1980', '1981', '1982', '1983', '1984', '1985',
            '1986', '1987', '1988', '1989', '1990', '1991', '1992',
            '1993', '1994', '1995', '1996', '1997', '1998', '1999',
            '2000', '2001', '2002', '2003', '2004', '2005', '2006',
            '2007', '2008', '2009', '2010', '2011', '2012', '2013',
            '2014', '2015', '2016', '2017', '2018', '2019', '2020',
            '2021', '2022', '2023'])
        self.en4.place(x=14 * 40, y=6.2 * 40, width=3.8 * 20, height=0.5 * 40)
        self.en44 = ttk.Combobox(self.frame_new, state='readonly', textvariable=self.birth2, values=[
            '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
        self.en44.place(x=14 * 40 + 3.8 * 20, y=6.2 * 40, width=3.8 * 20, height=0.5 * 40)
        self.en5 = ttk.Entry(self.frame_new, textvariable=self.password, show='*')
        self.en5.place(x=14 * 40, y=7.85 * 40, width=3.8 * 40, height=0.5 * 40)
        self.en6 = ttk.Entry(self.frame_new, textvariable=self.password_again, show='*')
        self.en6.place(x=14 * 40, y=9.46 * 40, width=3.8 * 40, height=0.5 * 40)
        # 确认注册和返回按钮，确认注册后要核查数据合法性返回界面
        self.yes = ttk.Button(self.frame_new, text='注册', command=self.re)
        self.yes.place(x=17 * 40, y=10.5 * 40, width=1.5 * 40, height=0.75 * 40)
        self.no = ttk.Button(self.frame_new, text='返回', command=self.turn)
        self.no.place(x=11.5 * 40, y=10.5 * 40, width=1.5 * 40, height=0.75 * 40)

    def turn(self):
        login()

    def re(self):
        name = self.name.get()
        phone = self.phone.get()
        sex = self.sex.get()
        birth = self.birth1.get() + '-' + self.birth2.get()
        pa = self.password.get()
        pa_a = self.password_again.get()
        # 首先判断两次密码输入是否相等
        if pa == pa_a:
            check = f2(name, phone, sex, birth, pa, pa_a)
            # check=1
            if check == False:
                register_again(name, phone, sex, birth, pa, pa_a, 2)
            else:
                register_success()
        else:
            register_again(name, phone, sex, birth, pa, pa_a, 1)


# 成功注册界面
class register_success:
    def __init__(self):
        self.frame_new = tk.Frame(root, bg='white')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/else/注册成功.png")
        tk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=0 * 40, y=0 * 40, width=864, height=576)
        # 前往登录界面
        self.yes = ttk.Button(self.frame_new, text='登录', command=self.re)
        self.yes.place(x=17 * 40, y=9.5 * 40, width=1.5 * 40, height=0.75 * 40)

    def re(self):
        login()


######顾客端#######
# 顾客初始界面
class customer_1:
    def __init__(self, id):
        self.frame_new = tk.Frame(root, bg='#84877E')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/customer/background/顾客界面.png")
        ttk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=-2, y=0, width=864, height=576)
        # 导入按钮背景
        self.room_bt_bk = tk.PhotoImage(file="image/customer/button/ROOM.png")
        self.order_bt_bk = tk.PhotoImage(file="image/customer/button/ORDER.png")
        self.more_bt_bk = tk.PhotoImage(file="image/customer/button/MORE.png")
        self.mes_change = tk.PhotoImage(file="image/customer/button/头像.png")
        ###########新增查看订单详细信息功能
        look_more = ttk.Button(self.frame_new, text='查看更多订单信息', command=lambda: more_order_message(id))
        look_more.place(x=612, y=444, width=219, height=25)

        ####################333
        # 按钮放置
        self.b1 = tk.Button(self.frame_new, image=self.room_bt_bk, bg="white", border="0",
                            command=lambda: self.book_room(id))
        self.b1.place(x=0, y=194, width=69, height=21)
        self.b2 = tk.Button(self.frame_new, image=self.order_bt_bk, bg="white", border="0",
                            command=lambda: self.order(id))
        self.b2.place(x=0, y=222, width=69, height=21)
        self.b3 = tk.Button(self.frame_new, image=self.more_bt_bk, bg="white", border="0",
                            command=lambda: del_package(id))
        self.b3.place(x=0, y=255, width=69, height=21)
        self.b4 = tk.Button(self.frame_new, image=self.mes_change, bg="white", border="0",
                            command=lambda: self.customer_change(id))
        self.b4.place(x=738, y=24, width=30, height=30)
        list = fun_2(id)  # 返回list[id,姓名，电话，性别，生日，余额，备注]
        # list = ['111', 'xss', '19999999999', '女', '2004-01-18', '200', None]
        # 个人信息框
        ttk.Label(self.frame_new, text=id).place(x=694, y=101, width=124, height=15)
        ttk.Label(self.frame_new, text=list[2]).place(x=694, y=124, width=124, height=15)
        ttk.Label(self.frame_new, text=list[4]).place(x=694, y=147, width=124, height=15)
        ttk.Label(self.frame_new, text=list[5]).place(x=694, y=211, width=124, height=15)
        ttk.Label(self.frame_new, text=list[6]).place(x=633, y=295, width=185, height=74)
        self.my_list = f5(id)
        # self.my_list = [
        #    ['1', '123', '2022-12-23', '14:00', '15:00'],
        #    ['2', '122', '2022-12-24', '14:00', '15:00'],
        #    ['3', '113', '2022-12-27', '14:00', '15:00']
        # ]
        show_list = []
        for i in range(len(self.my_list)):
            show_list.append([self.my_list[i][1], self.my_list[i][2], self.my_list[i][3], self.my_list[i][4]])
        columns = ['房号', '日期', '开始时间', '结束时间']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(show_list),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列

        )
        table.place(x=172, y=212, width=350, height=151)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.heading(columns[2], text=columns[2])
        table.heading(columns[3], text=columns[3])
        table.column(columns[0], width=50, minwidth=50)
        table.column(columns[1], width=100, minwidth=100)
        table.column(columns[2], width=100, minwidth=100)
        table.column(columns[3], width=100, minwidth=100)
        for i in range(len(show_list)):
            table.insert('', 'end', values=show_list[i])

    def book_room(self, id):
        book_room(id)

    def order(self, id):
        order(id)

    def customer_change(self, id):
        customer_change(id)


class more_order_message:
    def __init__(self, id):
        self.frame_new = tk.Frame(root, bg='#84877E')
        # 背景图导入
        global land1
        land1 = tk.PhotoImage(file="image/customer/background/查看更多订单信息.png")
        ttk.Label(self.frame_new, image=land1).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=-2, y=0, width=864, height=576)

        # 放置订单框
        self.mes_list = seek_order_all(id)
        #self.mes_list = [
        #    ['1', '123', '2022-12-23', '14:00', '15:00', '99'],
        #    ['2', '122', '2022-12-24', '14:00', '15:00', '88'],
        #    ['3', '113', '2022-12-27', '14:00', '15:00', '77']
        #]

        show_list = []
        for i in range(len(self.mes_list)):
            show_list.append(
                [self.mes_list[i][1], self.mes_list[i][2] + ' ' + self.mes_list[i][3] + '-' + self.mes_list[i][4],self.mes_list[i][5]])

        columns = ['房号', '时间', '总费用']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(show_list),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列

        )
        table.place(x=151 + 40, y=147, width=300, height=250)
        self.itm = 0

        def onSelect(e):
            self.itm = table.set(table.focus())
            pass

        table.bind("<<TreeviewSelect>>", onSelect)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.heading(columns[2], text=columns[2])
        table.column(columns[0], width=50, minwidth=50)
        table.column(columns[1], width=200, minwidth=200)
        table.column(columns[2], width=50, minwidth=50)
        for i in range(len(show_list)):
            table.insert('', 'end', values=show_list[i])

        # 返回按钮
        t = ttk.Button(self.frame_new, text='返回', command=lambda: customer_1(id))
        t.place(x=75, y=100, width=50, height=25)
        # 确认按钮
        y = ttk.Button(self.frame_new, text='看套餐', command=lambda: self.show_order_message(id, 1))
        y.place(x=125, y=100, width=50, height=25)
        yy = ttk.Button(self.frame_new, text='看商品', command=lambda: self.show_order_message(id, 2))
        yy.place(x=175, y=100, width=50, height=25)

    def show_order_message(self, id, type):
        order_id = 0
        for i in range(len(self.mes_list)):
            if self.itm['房号'] == self.mes_list[i][1] and self.itm['时间'] == self.mes_list[i][2] + ' ' + self.mes_list[i][
                3] + '-' + self.mes_list[i][4]:
                order_id = self.mes_list[i][0]
                break
        if type == 1:
            show_order_package(id, order_id)
        else:
            show_order_good(id, order_id)



class show_order_package:
    def __init__(self, id, order_id):
        print(order_id)
        # 根据订单id返回订单的套餐信息和商品信息
        # 商品名，下单时间，单价，数量
        #package_list = [
        #    ['薯片套餐', '产品', '77', '20', '张庆宇'],
        #]
        package_list=pac_by_id(order_id)
        self.frame_new = tk.Frame(root, bg='#84877E')
        # 背景图导入
        global land2
        land2 = tk.PhotoImage(file="image/customer/background/查看更多订单信息.png")
        ttk.Label(self.frame_new, image=land2).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=-2, y=0, width=864, height=576)

        show_list = []
        for i in range(len(package_list)):
            show_list.append(package_list[i])

        columns = ['套餐名', '产品名', '套餐价格', '产品价格', '技师']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(show_list),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列

        )
        table.place(x=151 + 40, y=147, width=500, height=250)
        self.itm = 0

        def onSelect(e):
            self.itm = table.set(table.focus())
            pass

        table.bind("<<TreeviewSelect>>", onSelect)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.heading(columns[2], text=columns[2])
        table.heading(columns[3], text=columns[3])
        table.heading(columns[4], text=columns[4])
        table.column(columns[0], width=100, minwidth=100)
        table.column(columns[1], width=100, minwidth=100)
        table.column(columns[2], width=100, minwidth=100)
        table.column(columns[3], width=100, minwidth=100)
        table.column(columns[4], width=100, minwidth=100)
        for i in range(len(show_list)):
            table.insert('', 'end', values=show_list[i])

        # 返回按钮
        t = ttk.Button(self.frame_new, text='返回', command=lambda: more_order_message(id))
        t.place(x=75, y=150, width=50, height=25)


class show_order_good:
    def __init__(self, id, order_id):
        print(order_id)
        # 根据订单id返回订单的套餐信息和商品信息
        # 商品名，下单时间，单价，数量，食物id
        self.good_list =seek_order_food(order_id)
        #self.good_list = [
        #    ['薯片', '2022-12-12 14:00', '7', '2', '1234'],
        #    ['可乐', '2022-13-13 15:09', '3', '2', '2345']
        #]
        self.frame_new = tk.Frame(root, bg='#84877E')
        # 背景图导入
        global land2
        land2 = tk.PhotoImage(file="image/customer/background/查看更多订单信息.png")
        ttk.Label(self.frame_new, image=land2).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=-2, y=0, width=864, height=576)

        show_list = []
        for i in range(len(self.good_list)):
            show_list.append([self.good_list[i][0], self.good_list[i][1], self.good_list[i][2], self.good_list[i][3],self.good_list[i][5]])

        columns = ['商品名', '下单时间', '单价', '数量','状态']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(show_list),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列

        )
        table.place(x=151 + 40, y=147, width=600, height=250)
        self.itm = 0

        def onSelect(e):
            self.itm = table.set(table.focus())
            pass

        table.bind("<<TreeviewSelect>>", onSelect)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.heading(columns[2], text=columns[2])
        table.heading(columns[3], text=columns[3])
        table.heading(columns[4], text=columns[4])
        table.column(columns[0], width=100, minwidth=100)
        table.column(columns[1], width=200, minwidth=200)
        table.column(columns[2], width=100, minwidth=100)
        table.column(columns[3], width=100, minwidth=100)
        table.column(columns[4], width=100, minwidth=100)
        for i in range(len(show_list)):
            table.insert('', 'end', values=show_list[i])

        # 返回按钮
        t = ttk.Button(self.frame_new, text='返回', command=lambda: more_order_message(id))
        t.place(x=75, y=150, width=50, height=25)
        # 确认按钮
        y = ttk.Button(self.frame_new, text='删除', command=lambda: self.dele(id, order_id))
        y.place(x=125, y=150, width=50, height=25)

    def dele(self, id, order_id):
        # 删除self.itm
        print(self.itm)
        good_id = 0
        time=0
        for i in range(len(self.good_list)):
            if self.itm['商品名'] == self.good_list[i][0] and self.itm['下单时间'] == self.good_list[i][1] and self.itm[
                '单价'] == self.good_list[i][2] and self.itm['数量'] == self.good_list[i][3]:
                good_id = self.good_list[i][4]
                time=self.good_list[i][1]
                break
        ########函数
        k=delete_good(order_id,good_id,time,id)
        #k=[False,'原因']
        if k[0]==False:
            ttk.Label(self.frame_new,text=k[1]).place(x=139,y=461,width=200,height=25)
            return
        show_order_good(id, order_id)


# 退钱
class del_package:
    def __init__(self, id):
        self.frame_new = tk.Frame(root, bg='#84877E')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/customer/background/退款.png")
        ttk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=-2, y=0, width=864, height=576)
        # 按钮背景图导入
        self.i1 = tk.PhotoImage(file='image/customer/button/确认.png')
        self.i2 = tk.PhotoImage(file='image/customer/button/退订.png')
        self.i3 = tk.PhotoImage(file='image/customer/button/删除.png')
        # 按钮放置
        self.yes = tk.Button(self.frame_new, image=self.i1, bg='#677D71', border='0', command=self.show_plist)
        self.yes.place(x=415, y=421, width=87, height=27)
        self.real_yes = tk.Button(self.frame_new, image=self.i2, bg='#5A776A', border='0',
                                  command=lambda: self.finish(id))
        self.real_yes.place(x=658, y=421, width=87, height=27)
        self.dele = tk.Button(self.frame_new, image=self.i3, bg='#677D71', border='0', command=self.dele_package)
        self.dele.place(x=325, y=421, width=87, height=27)

        # 订单展示框
        # 要改
        # [订单号，房号，日期（包括开始时间结束时间）]
        n = f5_p(id)
        self.mes_list = list()
        for i in n:
            self.mes_list.append([i[0], i[1], i[2] + ' ' + i[3] + '-' + i[4]])
        # self.mes_list = [
        #    ['123', '001', '2022-12-22 14:00-14:30'],
        #    ['123', '021', '2022-12-22 14:00-14:30'],
        #    ['123', '011', '2022-12-22 14:00-14:30'],
        #   ['123', '031', '2022-12-22 14:00-14:30'],
        # ]

        show_list = []
        for i in range(len(self.mes_list)):
            show_list.append([self.mes_list[i][1], self.mes_list[i][2]])

        columns = ['房号', '时间']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(show_list),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列

        )
        table.place(x=151 + 40, y=147, width=250, height=250)
        self.itm = 0

        def onSelect(e):
            self.itm = table.set(table.focus())
            pass

        table.bind("<<TreeviewSelect>>", onSelect)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.column(columns[0], width=50, minwidth=50)
        table.column(columns[1], width=200, minwidth=200)
        for i in range(len(show_list)):
            table.insert('', 'end', values=show_list[i])

        # 存储选择套餐信息的列表
        self.plist = []
        self.money = 0
        # 返回按钮
        t = ttk.Button(self.frame_new, text='返回', command=lambda: customer_1(id))
        t.place(x=50, y=150, width=50, height=25)

    def show_plist(self):
        n = self.itm['房号']
        t = self.itm['时间']
        is_in = '0'
        for i in range(0, len(self.plist)):
            if n == self.plist[i][0] and t == self.plist[i][1]:
                is_in = '1'
        if is_in == '0':
            self.plist.append([n, t])
        columns = ['房号', '时间']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(self.plist),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列

        )
        table.place(x=408 + 40, y=147, width=250, height=250)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.column(columns[0], width=50, minwidth=50)
        table.column(columns[1], width=200, minwidth=200)
        for i in range(len(self.plist)):
            table.insert('', 'end', values=self.plist[i])

    def dele_package(self):
        n = self.itm['房号']
        t = self.itm['时间']
        is_in = '0'
        for i in range(0, len(self.plist)):
            if n == self.plist[i][0] and t == self.plist[i][1]:
                del self.plist[i]
                break
        columns = ['房号', '时间']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(self.plist),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列

        )
        table.place(x=408 + 40, y=147, width=250, height=250)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.column(columns[0], width=50, minwidth=50)
        table.column(columns[1], width=200, minwidth=200)
        for i in range(len(self.plist)):
            table.insert('', 'end', values=self.plist[i])

    def finish(self, id):
        print(self.plist)
        final_list = []
        ####3函数！
        for i in range(len(self.plist)):
            for j in range(len(self.mes_list)):
                if self.plist[i][0] == self.mes_list[j][1] and self.plist[i][1] == self.mes_list[j][2]:
                    final_list.append(self.mes_list[j][0])
                    break
        k = del_ord(final_list)
        if k[0] == True:
            w = tk.Tk()
            w.geometry('150x150')
            ttk.Label(w, text='退订成功').place(x=0, y=0, width=150, height=150)
        else:
            w = tk.Tk()
            w.geometry('150x150')
            ttk.Label(w, text=k[1]).place(x=0, y=0, width=150, height=150)
            return
        customer_1(id)


# 顾客修改个人信息
class customer_change:
    def __init__(self, id):
        self.frame_new = tk.Frame(root, bg='#84877E')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/customer/background/顾客修改个人信息.png")
        ttk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=-2, y=0, width=864, height=576)
        trrn0_button = ttk.Button(self.frame_new, text='返回', command=lambda: customer_1(id))
        trrn0_button.place(x=781, y=26, width=50, height=25)

        list = fun_2(id)  # 返回list[id,姓名，电话，性别，生日，余额，备注]
        # list=['111','xss','19999999999','女','2004-01','200',None]
        name = tk.StringVar()
        phone = tk.StringVar()
        sex = tk.StringVar()
        birth1 = tk.StringVar()
        birth2 = tk.StringVar()
        note = tk.StringVar()
        name.set(list[1])
        phone.set(list[2])
        sex.set(list[3])
        birth1.set((list[4])[0:4])
        birth2.set((list[4])[5:7])
        note.set(list[6])
        # 个人信息框
        ttk.Entry(self.frame_new, textvariable=name).place(x=694, y=101, width=124, height=15)
        ttk.Entry(self.frame_new, textvariable=phone).place(x=694, y=124, width=124, height=15)
        ttk.Combobox(self.frame_new, state='readonly', textvariable=birth1, values=[
            '1930', '1931', '1932', '1933', '1934', '1935', '1936',
            '1937', '1938', '1939', '1940', '1941', '1942', '1943',
            '1944', '1945', '1946', '1947', '1948', '1949', '1950',
            '1951', '1952', '1953', '1954', '1955', '1956', '1957',
            '1958', '1959', '1960', '1961', '1962', '1963', '1964',
            '1965', '1966', '1967', '1968', '1969', '1970', '1971',
            '1972', '1973', '1974', '1975', '1976', '1977', '1978',
            '1979', '1980', '1981', '1982', '1983', '1984', '1985',
            '1986', '1987', '1988', '1989', '1990', '1991', '1992',
            '1993', '1994', '1995', '1996', '1997', '1998', '1999',
            '2000', '2001', '2002', '2003', '2004', '2005', '2006',
            '2007', '2008', '2009', '2010', '2011', '2012', '2013',
            '2014', '2015', '2016', '2017', '2018', '2019', '2020',
            '2021', '2022', '2023'
        ]).place(x=694, y=147, width=124 / 2, height=15)
        ttk.Combobox(self.frame_new, state='readonly', textvariable=birth2, values=[
            '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'
        ]).place(x=694 + 124 / 2, y=147, width=124 / 2, height=15)

        ttk.Combobox(self.frame_new, state='readonly', textvariable=sex, values=['男', '女']).place(x=694, y=170,
                                                                                                  width=124, height=15)
        ttk.Entry(self.frame_new, textvariable=note).place(x=633, y=295, width=185, height=74)
        self.i2 = tk.PhotoImage(file='image/customer/button/完成.png')
        # 按钮放置
        self.real_yes = tk.Button(self.frame_new, image=self.i2, bg='white', border='0',
                                  command=lambda: self.c(id, name.get(), phone.get(), sex.get(), birth1.get(),
                                                         birth2.get(), note.get()))
        self.real_yes.place(x=600, y=500, width=87, height=27)

    def c(self, id, name, phone, sex, birth1, birth2, note):
        k = f10(id, name, phone, sex, birth1 + '-' + birth2, note)
        # k=[True,'名字过长']
        if k[0] == False:
            ttk.Label(self.frame_new, text=k[1]).place(x=600, y=446, width=150, height=25)
        else:
            customer_1(id)


# 顾客预约房间
class book_room:
    def __init__(self, id):
        self.room_num = 'ffffff'
        self.frame_new = tk.Frame(root, bg='#84877E')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/customer/background/预约房间.png")
        ttk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=-2, y=0, width=864, height=576)
        # 按钮背景图导入
        self.i1 = tk.PhotoImage(file='image/customer/button/今天.png')
        self.i2 = tk.PhotoImage(file='image/customer/button/明天.png')
        self.i3 = tk.PhotoImage(file='image/customer/button/后天.png')
        self.i4 = tk.PhotoImage(file='image/customer/button/1.png')
        self.i5 = tk.PhotoImage(file='image/customer/button/2.png')
        self.i6 = tk.PhotoImage(file='image/customer/button/3.png')
        self.i7 = tk.PhotoImage(file='image/customer/button/4.png')
        self.i8 = tk.PhotoImage(file='image/customer/button/确定.png')
        self.i9 = tk.PhotoImage(file='image/customer/button/预约.png')
        self.room_bt_bk = tk.PhotoImage(file="image/customer/button/ROOM.png")
        self.order_bt_bk = tk.PhotoImage(file="image/customer/button/ORDER.png")
        self.more_bt_bk = tk.PhotoImage(file="image/customer/button/MORE.png")
        # 容纳人数按钮
        self.type = 1  # 默认为一人

        def change_type(i):
            self.type = i

        self.date = 2  # 默认为明天

        def change_date(i):
            self.date = i

        self.b1 = tk.Button(self.frame_new, image=self.i4, bg='#84877E', border='0', command=lambda: change_type(1))
        self.b1.place(x=483, y=180, width=16, height=16)
        self.b2 = tk.Button(self.frame_new, image=self.i5, bg='#84877E', border='0', command=lambda: change_type(2))
        self.b2.place(x=508, y=180, width=16, height=16)
        self.b6 = tk.Button(self.frame_new, image=self.i2, bg='#84877E', border='0', command=lambda: change_date(2))
        self.b6.place(x=252, y=140, width=87, height=36)
        self.b7 = tk.Button(self.frame_new, image=self.i3, bg='#84877E', border='0', command=lambda: change_date(3))
        self.b7.place(x=252, y=176, width=87, height=36)

        self.st = tk.StringVar()
        self.et = tk.StringVar()
        self.st.set('14:00')
        self.et.set('14:30')

        self.c1 = ttk.Combobox(self.frame_new, state='readonly',
                               values=(
                                   '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00',
                                   '18:30',
                                   '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00',)
                               , textvariable=self.st
                               )
        self.c1.place(x=483, y=107, width=93, height=16)
        self.c2 = ttk.Combobox(self.frame_new, state='readonly',
                               values=(
                                   '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30',
                                   '19:00',
                                   '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30',),
                               textvariable=self.et)
        self.c2.place(x=483, y=144, width=93, height=16)

        self.yes = tk.Button(self.frame_new, image=self.i8, bg='#84877E', border='0',
                             command=lambda: self.show_room(id))
        self.yes.place(x=499, y=219, width=87, height=27)
        self.real_yes = tk.Button(self.frame_new, image=self.i9, bg='#5A776A', border='0',
                                  command=lambda: self.book_package(id))
        self.real_yes.place(x=499, y=435, width=87, height=27)

        # 返回按钮
        t = ttk.Button(self.frame_new, text='返回', command=lambda: customer_1(id))
        t.place(x=50, y=150, width=50, height=25)

        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.f = 0

    def show_room(self, id):
        self.ll = tk.Label(self.frame_new, bg='#84877E', text='时间有误')
        if self.et.get() < self.st.get():
            self.ll.place(x=254, y=225, width=200, height=20)
            return
        self.room_num, real_type = f3(self.date, self.st.get(), self.et.get(), self.type)
        tk.Label(self.frame_new, bg='#84877E').place(x=254, y=225, width=200, height=20)
        # self.room_num='123'
        # real_type='2'
        st = self.st.get()
        et = self.et.get()
        if self.room_num != 'ffffff':
            tk.Label(self.frame_new, bg='#84877E').place(x=254, y=225, width=200, height=20)
            ttk.Label(self.frame_new, text=self.room_num).place(x=254 + 117, y=262 + 20, width=170, height=20)
            ttk.Label(self.frame_new, text=st + '-' + et).place(x=254 + 117, y=262 + 58, width=170, height=20)
            ttk.Label(self.frame_new, text=str(real_type)).place(x=254 + 117, y=262 + 96, width=170, height=20)
            self.a = self.date
            self.b = self.st.get()
            self.c = self.et.get()
            self.d = self.type
            self.f = self.room_num
        else:
            tk.Label(self.frame_new, bg='#84877E', text='抱歉没有空闲的房间，请重新选择').place(x=254, y=225, width=200, height=20)
            return

    def book_package(self, id):
        if self.room_num == 'ffffff':
            return
        book_package(id, self.f, self.b, self.c, self.d, self.a)


# 预约房间后选择套餐
class book_package:
    def __init__(self, id, room_num, st, et, type, date):
        self.top_count = int(type) * ((int(et[0:2]) - int(st[0:2])) * 60 + int(et[3:5]) - int(st[3:5])) / 30

        self.frame_new = tk.Frame(root, bg='#84877E')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/customer/background/成功预约房间.png")
        ttk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=-2, y=0, width=864, height=576)
        # 按钮背景图导入
        self.i1 = tk.PhotoImage(file='image/customer/button/确认.png')
        self.i2 = tk.PhotoImage(file='image/customer/button/完成.png')
        self.i3 = tk.PhotoImage(file='image/customer/button/删除.png')
        self.room_bt_bk = tk.PhotoImage(file="image/customer/button/ROOM.png")
        self.order_bt_bk = tk.PhotoImage(file="image/customer/button/ORDER.png")
        self.more_bt_bk = tk.PhotoImage(file="image/customer/button/MORE.png")
        # 按钮放置
        self.yes = tk.Button(self.frame_new, image=self.i1, bg='#677D71', border='0', command=self.show_plist)
        self.yes.place(x=415, y=421, width=87, height=27)
        self.real_yes = tk.Button(self.frame_new, image=self.i2, bg='#5A776A', border='0',
                                  command=lambda: self.finish(id, room_num, st, et, type, date))
        self.real_yes.place(x=658, y=421, width=87, height=27)
        self.dele = tk.Button(self.frame_new, image=self.i3, bg='#677D71', border='0', command=self.dele_package)
        self.dele.place(x=325, y=421, width=87, height=27)

        # 套餐展示框
        # 要改
        self.mes_list = f6()
        # self.mes_list=[
        #   ['id','按摩套餐','延年益寿','99',[['产品A','功效','10','id'],['产品B','功效','20','id'],['产品C','功效','40','id']]],
        #   ['id','推拿套餐','延年益寿','99',[['产品A','功效','10','id'],['产品B','功效','20','id']]],
        #   ['id','推拿套餐','延年益寿','99',[['产品A','功效','10','id'],['产品B','功效','20','id']]],
        #   ['id','推拿套餐','延年益寿','99',[['产品A','功效','10','id'],['产品B','功效','20','id']]],
        #   ['id','推拿套餐','延年益寿','99',[['产品A','功效','10','id'],['产品B','功效','20','id']]],
        # ]

        show_list = []
        for i in range(len(self.mes_list)):
            for j in range(len(self.mes_list[i][4])):
                if j == 0:
                    show_list.append([self.mes_list[i][1], self.mes_list[i][4][j][0],
                                      self.mes_list[i][2] + ',' + self.mes_list[i][4][j][1],
                                      str(int(self.mes_list[i][3]) + int(self.mes_list[i][4][j][2]))
                                      ])
                else:
                    show_list.append([self.mes_list[i][1], self.mes_list[i][4][j][0],
                                      self.mes_list[i][2] + ',' + self.mes_list[i][4][j][1],
                                      str(int(self.mes_list[i][3]) + int(self.mes_list[i][4][j][2]))
                                      ])
        columns = ['套餐名', '产品名', '功效', '价格']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(show_list),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列

        )
        table.place(x=72, y=212, width=422, height=151)
        self.itm = 0

        def onSelect(e):
            self.itm = table.set(table.focus())
            pass

        table.bind("<<TreeviewSelect>>", onSelect)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.heading(columns[2], text=columns[2])
        table.heading(columns[3], text=columns[3])
        table.column(columns[0], width=100, minwidth=100)
        table.column(columns[1], width=100 - 28, minwidth=100 - 28)
        table.column(columns[2], width=200, minwidth=200)
        table.column(columns[3], width=50, minwidth=50)
        for i in range(len(show_list)):
            table.insert('', 'end', values=show_list[i])

        self.count = tk.StringVar()
        self.count.set('1')
        self.index_count = ttk.Combobox(self.frame_new, state='readonly', textvariable=self.count, values=['1', '2'])
        self.index_count.place(x=333, y=378, width=30, height=17)

        # 存储选择套餐信息的列表
        self.plist = []
        self.money = 0
        # 返回按钮
        t = ttk.Button(self.frame_new, text='返回', command=lambda: book_room(id))
        t.place(x=50, y=150, width=50, height=25)

    def show_plist(self):

        n = self.itm['套餐名']
        p = self.itm['产品名']
        pr = self.itm['价格']
        count = self.count.get()

        p_count = 0
        for i in range(len(self.plist)):
            p_count += int(self.plist[i][2])
        p_count += int(count)
        if p_count > self.top_count:
            for i in range(len(self.plist)):
                if n == self.plist[i][0] and p == self.plist[i][1] and count == self.plist[i][2]:
                    return
            ttk.Label(self.frame_new, text='套餐过多，预约时间内无法完成', background='#657C70').place(x=172, y=397, width=200,
                                                                                         height=24)
            return
        ttk.Label(self.frame_new, background='#657C70').place(x=172, y=397, width=200, height=24)

        is_in = '0'
        for i in range(0, len(self.plist)):
            if n == self.plist[i][0] and p == self.plist[i][1]:
                is_in = '1'
                self.plist[i][2] = count
                self.plist[i][3] = pr
                break
        if is_in == '0':
            self.plist.append([n, p, count, pr])
        columns = ['套餐名', '产品名', '数量', '单价']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(self.plist),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列

        )
        table.place(x=534, y=117, width=200, height=278)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.heading(columns[2], text=columns[2])
        table.heading(columns[3], text=columns[3])
        table.column(columns[0], width=50, minwidth=50)
        table.column(columns[1], width=50, minwidth=50)
        table.column(columns[2], width=25, minwidth=25)
        table.column(columns[3], width=25, minwidth=25)
        for i in range(len(self.plist)):
            table.insert('', 'end', values=self.plist[i])

        self.money = 0
        for i in range(len(self.plist)):
            self.money += float(self.plist[i][2]) * float(self.plist[i][3])
        tk.Label(self.frame_new, bg='#5A776A', text='总价 ' + str(int(self.money)) + ' 元').place(x=534, y=117 + 278 - 20,
                                                                                               width=200, height=20)

    def dele_package(self):
        ttk.Label(self.frame_new, background='#657C70').place(x=172, y=397, width=200, height=24)
        n = self.itm['套餐名']
        p = self.itm['产品名']
        pr = self.itm['价格']
        count = self.count.get()
        for i in range(len(self.plist)):
            if n == self.plist[i][0] and p == self.plist[i][1]:
                del self.plist[i]
                break
        columns = ['套餐名', '产品名', '数量', '单价']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(self.plist),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列

        )
        table.place(x=534, y=117, width=200, height=278)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.heading(columns[2], text=columns[2])
        table.heading(columns[3], text=columns[3])
        table.column(columns[0], width=50, minwidth=50)
        table.column(columns[1], width=50, minwidth=50)
        table.column(columns[2], width=25, minwidth=25)
        table.column(columns[3], width=25, minwidth=25)
        for i in range(len(self.plist)):
            table.insert('', 'end', values=self.plist[i])
        self.money = 0
        for i in range(len(self.plist)):
            self.money += float(self.plist[i][2]) * float(self.plist[i][3])
        tk.Label(self.frame_new, bg='#5A776A', text='总价 ' + str(int(self.money)) + ' 元').place(x=534, y=117 + 278 - 20,
                                                                                               width=200, height=20)

    def finish(self, id, num, st, et, type, date):
        if self.money == 0:
            return
        # 为该id增加一个订单(id,list=[[套餐序号,套餐个数,套餐产品序号]...],房间号,开始时间,结束时间,容纳人数,日期)
        # ['套餐名','产品名','数量','单价']
        # self.mes_list=[
        #   ['id','按摩套餐','延年益寿','99',[['产品A','功效','10'],['产品B','功效','20'],['产品C','功效','40']]],
        #   ['id','推拿套餐','延年益寿','99',[['产品A','功效','10'],['产品B','功效','20']]],
        # ]
        final_list = []
        for i in range(len(self.plist)):
            for j in range(len(self.mes_list)):
                if self.plist[i][0] == self.mes_list[j][1]:
                    for k in range(len(self.mes_list[j][4])):
                        if self.plist[i][1] == self.mes_list[j][4][k][0]:
                            final_list.append([self.mes_list[j][0], self.mes_list[j][4][k][3], self.plist[i][2]])
                    break

        k = f7(id, final_list, num, st, et, date)
        # k=True
        if k != True:
            w = tk.Tk()
            w.geometry('500x150')
            ttk.Label(w, text=k[1]).place(x=0, y=0, width=500, height=150)
            return

        finish_book_room(id, self.plist, num, st, et, type, date)


# 房间预约完毕
class finish_book_room:
    def __init__(self, id, plist, room_num, st, et, type, date):
        self.plist = plist
        self.frame_new = tk.Frame(root, bg='#84877E')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/customer/background/预约完成.png")
        ttk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=-2, y=0, width=864, height=576)
        # 按钮背景图导入
        self.i2 = tk.PhotoImage(file='image/customer/button/完成.png')
        self.room_bt_bk = tk.PhotoImage(file="image/customer/button/ROOM.png")
        self.order_bt_bk = tk.PhotoImage(file="image/customer/button/ORDER.png")
        self.more_bt_bk = tk.PhotoImage(file="image/customer/button/MORE.png")
        # 按钮放置
        self.real_yes = tk.Button(self.frame_new, text='完成', bg='#5A776A', border='0',
                                  command=lambda: customer_1(id))
        self.real_yes.place(x=658, y=421, width=87, height=27)

        # 房间信息显示框架
        ttk.Label(self.frame_new, text=room_num).place(x=227 + 117, y=137 + 20, width=170, height=20)
        if date == 2:
            ttk.Label(self.frame_new, text='明天' + ' ' + st + '-' + et).place(x=227 + 117, y=137 + 58, width=170,
                                                                             height=20)
        else:
            ttk.Label(self.frame_new, text='后天' + ' ' + st + '-' + et).place(x=227 + 117, y=137 + 58, width=170,
                                                                             height=20)
        ttk.Label(self.frame_new, text=type).place(x=227 + 117, y=137 + 96, width=170, height=20)
        # 套餐信息
        columns = ['套餐名', '产品名', '数量', '单价']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(self.plist),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列

        )
        table.place(x=227, y=281, width=316, height=174)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.heading(columns[2], text=columns[2])
        table.heading(columns[3], text=columns[3])
        table.column(columns[0], width=100, minwidth=100)
        table.column(columns[1], width=100, minwidth=100)
        table.column(columns[2], width=50, minwidth=50)
        table.column(columns[3], width=50, minwidth=50)
        for i in range(len(self.plist)):
            table.insert('', 'end', values=self.plist[i])

        self.money = 0
        for i in range(len(self.plist)):
            self.money += float(self.plist[i][2]) * float(self.plist[i][3])
        tk.Label(self.frame_new, bg='#5A776A', text='总价 ' + str(int(self.money)) + ' 元').place(x=227, y=281 + 174 - 20,
                                                                                               width=316, height=20)

        w = tk.Tk()
        w.geometry('150x150')
        ttk.Label(w, text='预约成功').place(x=0, y=0, width=150, height=150)


# 顾客选购商品前先选对应房间
class order:
    def __init__(self, id):
        self.frame_new = tk.Frame(root, bg='#84877E')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/customer/background/订购.png")
        ttk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=-2, y=0, width=864, height=576)
        # 按钮背景图导入
        self.i2 = tk.PhotoImage(file='image/customer/button/继续.png')
        self.room_bt_bk = tk.PhotoImage(file="image/customer/button/ROOM.png")
        self.order_bt_bk = tk.PhotoImage(file="image/customer/button/ORDER.png")
        self.more_bt_bk = tk.PhotoImage(file="image/customer/button/MORE.png")
        # 按钮放置

        self.real_yes = tk.Button(self.frame_new, image=self.i2, bg='#5A776A', border='0',
                                  command=lambda: self.om(self.itm, id))
        self.real_yes.place(x=474, y=359, width=87, height=27)
        # 预约情况框
        # 查询该id所有未完成房间预约情况，返回list
        # my_list=[[订单号,房号1,日期,开始时间,结束时间]......]
        self.my_list = f5(id)
        # self.my_list=[
        #   ['1','123','2022-12-23','14:00','15:00'],
        #   ['2','122','2022-12-24','14:00','15:00'],
        #   ['3','113','2022-12-27','14:00','15:00']
        # ]

        show_list = []
        for i in range(len(self.my_list)):
            show_list.append([self.my_list[i][1], self.my_list[i][2], self.my_list[i][3], self.my_list[i][4]])
        columns = ['房号', '日期', '开始时间', '结束时间']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(show_list),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列

        )
        table.place(x=227, y=172, width=322, height=174)
        self.itm = 0

        def onSelect(e):
            self.itm = table.set(table.focus())
            pass

        table.bind("<<TreeviewSelect>>", onSelect)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.heading(columns[2], text=columns[2])
        table.heading(columns[3], text=columns[3])
        table.column(columns[0], width=100, minwidth=100)
        table.column(columns[1], width=100, minwidth=100)
        table.column(columns[2], width=50, minwidth=50)
        table.column(columns[3], width=50, minwidth=50)
        for i in range(len(show_list)):
            table.insert('', 'end', values=show_list[i])

        # 返回按钮
        t = ttk.Button(self.frame_new, text='返回', command=lambda: customer_1(id))
        t.place(x=50, y=150, width=50, height=25)

    def om(self, select, id):
        order_id = '0'
        for i in range(len(self.my_list)):
            if self.my_list[i][1] == select['房号'] and self.my_list[i][2] == select['日期'] and self.my_list[i][3] == \
                    select['开始时间'] and self.my_list[i][4] == select['结束时间']:
                order_id = self.my_list[i][0]
        if order_id == '0':
            return
        order_more(id, order_id)


# 顾客为对应房间选购商品
class order_more:
    def __init__(self, id, order_id):
        self.frame_new = tk.Frame(root, bg='#84877E')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/customer/background/订购食物酒水.png")
        ttk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=-2, y=0, width=864, height=576)
        # 按钮背景图导入
        self.i1 = tk.PhotoImage(file='image/customer/button/删除.png')
        self.i2 = tk.PhotoImage(file='image/customer/button/增加.png')
        self.i3 = tk.PhotoImage(file='image/customer/button/完成.png')
        self.room_bt_bk = tk.PhotoImage(file="image/customer/button/ROOM.png")
        self.order_bt_bk = tk.PhotoImage(file="image/customer/button/ORDER.png")
        self.more_bt_bk = tk.PhotoImage(file="image/customer/button/MORE.png")
        # 按钮放置
        self.b1 = tk.Button(self.frame_new, image=self.i1, bg='#5A776A', border='0', command=self.dele_good)
        self.b1.place(x=313, y=414, width=87, height=27)
        self.b2 = tk.Button(self.frame_new, image=self.i2, bg='#5A776A', border='0', command=self.show_plist)
        self.b2.place(x=424, y=414, width=87, height=27)
        self.b3 = tk.Button(self.frame_new, image=self.i3, bg='#5A776A', border='0',
                            command=lambda: self.finish(id, order_id))
        self.b3.place(x=653, y=414, width=87, height=27)
        # 商品显示框
        self.good_list = f8()
        # self.good_list=[
        #    ['name1','10','id1'],
        #    ['name2','20','id2']
        # ]

        show_list = []
        for i in range(len(self.good_list)):
            show_list.append([self.good_list[i][0], self.good_list[i][1]])
        columns = ['商品名', '单价']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(show_list),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列

        )
        table.place(x=228, y=174, width=272, height=173)
        self.itm = 0

        def onSelect(e):
            self.itm = table.set(table.focus())
            pass

        table.bind("<<TreeviewSelect>>", onSelect)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.column(columns[0], width=100, minwidth=100)
        table.column(columns[1], width=100, minwidth=100)
        for i in range(len(show_list)):
            table.insert('', 'end', values=show_list[i])

        # 商品数
        self.g_c = tk.StringVar()
        self.g_c.set('1')
        self.e1 = ttk.Combobox(self.frame_new, state='readonly', textvariable=self.g_c,
                               values=['1', '2', '3', '4', '5', '6'])
        self.e1.place(x=428, y=362, width=71, height=17)

        self.plist = []
        self.money = 0

        # 返回按钮
        t = ttk.Button(self.frame_new, text='返回', command=lambda: order(id))
        t.place(x=50, y=150, width=50, height=25)

    def show_plist(self):
        g_n = self.itm['商品名']
        g_c = self.g_c.get()
        g_p = self.itm['单价']
        is_in = '0'
        for i in range(0, len(self.plist)):
            if g_n == self.plist[i][0]:
                is_in = '1'
                self.plist[i][1] = g_c
                break
        if is_in == '0':
            self.plist.append([g_n, g_c, g_p])

        columns = ['商品名', '数量', '单价']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(self.plist),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列
        )
        table.place(x=572, y=118, width=157, height=261)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.heading(columns[2], text=columns[2])
        table.column(columns[0], width=50, minwidth=50)
        table.column(columns[1], width=30, minwidth=30)
        table.column(columns[2], width=38, minwidth=38)
        for i in range(len(self.plist)):
            table.insert('', 'end', values=self.plist[i])

        self.money = 0
        for i in range(len(self.plist)):
            self.money += int(self.plist[i][1]) * int(self.plist[i][2])
        tk.Label(self.frame_new, bg='#5A776A', text='总价 ' + str(self.money) + ' 元').place(x=572, y=118 + 261 - 20,
                                                                                          width=157, height=20)

    def dele_good(self):
        g_n = self.itm['商品名']
        g_c = self.g_c.get()
        g_p = self.itm['单价']
        for i in range(0, len(self.plist)):
            if g_n == self.plist[i][0]:
                del self.plist[i]
                break
        columns = ['商品名', '数量', '单价']
        table = ttk.Treeview(
            self.frame_new,  # 父容器
            height=len(self.plist),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列
        )
        table.place(x=572, y=118, width=157, height=261)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.heading(columns[2], text=columns[2])
        table.column(columns[0], width=50, minwidth=50)
        table.column(columns[1], width=30, minwidth=30)
        table.column(columns[2], width=38, minwidth=38)
        for i in range(len(self.plist)):
            table.insert('', 'end', values=self.plist[i])

        self.money = 0
        for i in range(len(self.plist)):
            self.money += int(self.plist[i][1]) * int(self.plist[i][2])
        tk.Label(self.frame_new, bg='#5A776A', text='总价 ' + str(self.money) + ' 元').place(x=572, y=118 + 261 - 20,
                                                                                          width=157, height=20)

    def finish(self, id, order_id):
        if self.money == 0:
            return
        llist = []
        for i in range(len(self.plist)):
            for j in range(len(self.good_list)):
                if self.plist[i][0] == self.good_list[j][0]:
                    llist.append([self.good_list[j][2], self.plist[i][1]])
                    break
        print(llist)
        # 为该id增加一个商品订单
        k = f9(id, llist, order_id)
        # k=[True,'123','134']
        if k[0] == False:
            t = k[1]
            for i in range(2, len(k)):
                t = t + ' and ' + k[i]
            ttk.Label(self.frame_new, text=t).place(x=0, y=390, width=500, height=25)
        else:
            w = tk.Tk()
            w.geometry('150x150')
            ttk.Label(w, text='下单成功').place(x=0, y=0, width=150, height=150)
            customer_1(id)


#########################################
class guanli:
    def __init__(self):

        self.frame_new = tk.Frame(root, bg='#84877E')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/guanli/background/管理界面.png")
        ttk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=-2, y=0, width=864, height=576)

        self.menubar = tk.Menu(self.frame_new)
        # 顾客
        self.customer = tk.Menu(self.frame_new, tearoff=False)
        self.customer.add_command(label='查看顾客信息', command=self.customer_look)
        self.customer.add_command(label='修改顾客余额', command=self.change_money)
        self.customer.add_command(label='注销顾客账户', command=self.dele_customer)
        self.customer.add_separator()
        self.menubar.add_cascade(label='顾客', menu=self.customer)
        # 员工
        self.worker = tk.Menu(self.frame_new, tearoff=False)
        self.worker.add_command(label='查看员工信息', command=self.worker_look)
        self.worker.add_command(label='增加员工信息', command=lambda: self.add(4))
        self.worker.add_command(label='修改员工信息', command=lambda: self.change(4))
        self.worker.add_separator()
        self.menubar.add_cascade(label='员工', menu=self.worker)
        # 货架
        self.huojia = tk.Menu(self.frame_new)
        # 套餐
        self.package = tk.Menu(self.frame_new, tearoff=False)
        self.package.add_command(label='查看套餐信息', command=self.package_look)
        self.package.add_command(label='增加套餐信息', command=lambda: self.add(1))
        self.package.add_command(label='修改套餐信息', command=lambda: self.change(1))
        self.package.add_separator()
        self.huojia.add_cascade(label='套餐', menu=self.package)
        # 产品
        self.product = tk.Menu(self.frame_new, tearoff=False)
        self.product.add_command(label='查看产品信息', command=self.product_look)
        self.product.add_command(label='增加产品信息', command=lambda: self.add(2))
        self.product.add_command(label='修改产品信息', command=lambda: self.change(2))
        self.product.add_separator()
        self.huojia.add_cascade(label='产品', menu=self.product)
        # 商品
        self.good = tk.Menu(self.frame_new, tearoff=False)
        self.good.add_command(label='查看商品信息', command=self.good_look)
        self.good.add_command(label='增加商品信息', command=lambda: self.add(3))
        self.good.add_command(label='修改商品信息', command=lambda: self.change(3))
        self.good.add_separator()
        self.huojia.add_cascade(label='商品', menu=self.good)
        self.menubar.add_cascade(label='货架', menu=self.huojia)
        # 房间
        self.room = tk.Menu(self.frame_new)
        self.room.add_command(label='查看房间状态', command=self.input_date)
        self.room.add_command(label='房间管理', command=self.change_room)
        self.menubar.add_cascade(label='房间', menu=self.room)
        # 店铺
        self.store = tk.Menu(self.frame_new)
        self.money = tk.Menu(self.frame_new)
        self.money.add_command(label='年营业额', command=lambda: self.input_date_type('1'))
        self.money.add_command(label='月营业额', command=lambda: self.input_date_type('2'))
        self.store.add_cascade(label='营业额', menu=self.money)
        self.menubar.add_cascade(label='店铺', menu=self.store)

        root.config(menu=self.menubar)
        w = tk.Tk()
        w.title('需要补货物品一览')
        w.geometry('600x600')

        def del_bh(master):
            buhuo = remind()
            # buhuo=[
            #   ['111','111','111'],
            #  ['111','111','111'],
            # ['111','111','111'],
            # ['111','111','111'],
            # ]
            bh(buhuo, master)

        def bh(buhuo, w):
            columns = ['id', '名字', '类型']
            table = ttk.Treeview(
                w,  # 父容器
                height=len(buhuo),  # 表格显示的行数,height行
                columns=columns,  # 显示的列
                show='headings',  # 隐藏首列
            )
            table.place(x=0, y=0, width=600, height=400)
            table.heading(columns[0], text=columns[0])
            table.heading(columns[1], text=columns[1])
            table.heading(columns[2], text=columns[2])
            table.column(columns[0], width=200, minwidth=200)
            table.column(columns[1], width=200, minwidth=200)
            table.column(columns[2], width=200, minwidth=200)
            for i in range(len(buhuo)):
                table.insert('', 'end', values=[buhuo[i][0], buhuo[i][1], buhuo[i][2]])
            w.protocol(del_bh)
            b = ttk.Button(w, text='刷新', command=lambda: del_bh(w))
            b.place(x=0, y=500, width=50, height=25)

        del_bh(w)
        w.mainloop()

    # 删除顾客
    def dele_customer(self):
        new_frame = tk.Frame(root)
        new_frame.place(x=0, y=0, width=864, height=576)

        def check(phone, pa):
            def real_delete(id):
                k = d1(id)
                k = True
                if k == False:
                    ttk.Label(new_frame, text='删除失败，有正在进行的订单').place(x=0, y=0, width=300, height=300)
                else:
                    ttk.Label(new_frame, text='删除成功').place(x=0, y=0, width=300, height=300)

            k = f11(phone, pa)
            # k=[True,'123']

            if k[0] == True:
                ttk.Label(new_frame, text='确认删除？').place(x=0, y=0, width=300, height=50)
                ttk.Label(new_frame, ).place(x=0, y=75, width=300, height=50)
                b = ttk.Button(new_frame, text='确认', command=lambda: real_delete(k[1]))
                b.place(x=250, y=50, width=50, height=25)
            else:
                ttk.Label(new_frame, text='电话或密码输入错误').place(x=0, y=75, width=300, height=50)

        ttk.Label(new_frame, text='电话').place(x=0, y=0, width=30, height=25)
        ttk.Label(new_frame, text='密码').place(x=0, y=25, width=30, height=25)
        phone = tk.StringVar()
        pa = tk.StringVar()
        e1 = ttk.Entry(new_frame, textvariable=phone)
        e1.place(x=50, y=0, width=250, height=25)
        e2 = ttk.Entry(new_frame, textvariable=pa, show='*')
        e2.place(x=50, y=25, width=250, height=25)
        b = ttk.Button(new_frame, text='确定', command=lambda: check(phone.get(), pa.get()))
        b.place(x=250, y=50, width=50, height=25)

    # 修改顾客余额
    def change_money(self):
        new_frame = tk.Frame(root)
        new_frame.place(x=0, y=0, width=864, height=576)

        def check(phone, pa):
            def real_change(id, new_money):
                d = fun_3(id, new_money)
                # d=True
                if d == False:
                    ttk.Label(new_frame, text='修改失败').place(x=0, y=100, width=300, height=25)
                else:
                    ttk.Label(new_frame, text='该账户余额为' + new_money).place(x=0, y=0, width=300, height=25)
                    ttk.Label(new_frame, text='修改成功').place(x=0, y=100, width=300, height=25)

            k = f11(phone, pa)
            print(k)
            # k=[True,'123']
            if k[0] == True:
                g = fun_2(k[1])
                # g = ['id', 'xxx', 'nv', '2002-11', '1200', None]
                ttk.Label(new_frame, text='该账户余额为' + g[5]).place(x=0, y=0, width=300, height=25)
                ttk.Label(new_frame, text='输入新数额').place(x=0, y=25, width=300, height=25)
                new_money = tk.StringVar()
                e = ttk.Entry(new_frame, textvariable=new_money)
                e.place(x=0, y=50, width=300, height=25)
                ttk.Label(new_frame, ).place(x=0, y=75, width=250, height=25)
                b = ttk.Button(new_frame, text='修改', command=lambda: real_change(k[1], new_money.get()))
                b.place(x=250, y=75, width=50, height=25)
            else:
                ttk.Label(new_frame, text=k[1]).place(x=0, y=75, width=300, height=25)

        ttk.Label(new_frame, text='电话').place(x=0, y=0, width=30, height=25)
        ttk.Label(new_frame, text='密码').place(x=0, y=25, width=30, height=25)
        phone = tk.StringVar()
        pa = tk.StringVar()
        e1 = ttk.Entry(new_frame, textvariable=phone)
        e1.place(x=50, y=0, width=250, height=25)
        e2 = ttk.Entry(new_frame, textvariable=pa, show='*')
        e2.place(x=50, y=25, width=250, height=25)
        b = ttk.Button(new_frame, text='确定', command=lambda: check(phone.get(), pa.get()))
        b.place(x=250, y=50, width=50, height=25)

    # 查看营业额
    def input_date_type(self, type):
        if type == '1':
            # 年营业额
            new_frame = tk.Frame(root)
            new_frame.place(x=0, y=0, width=864, height=576)

            def get_result(master, year):
                # 根据year返回三个
                package_list, product_list, good_list = year_money(year)
                ttk.Label(master, text='套餐总营业额').place(x=0, y=25, width=100, height=25)
                ttk.Label(master, text=package_list).place(x=100, y=25, width=200, height=25)
                ttk.Label(master, text='产品总营业额').place(x=0, y=75, width=100, height=25)
                ttk.Label(master, text=product_list).place(x=100, y=75, width=200, height=25)
                ttk.Label(master, text='商品总营业额').place(x=0, y=125, width=100, height=25)
                ttk.Label(master, text=good_list).place(x=100, y=125, width=200, height=25)
                ttk.Label(master, text='总营业额').place(x=0, y=175, width=100, height=25)
                ttk.Label(master, text=str(int(package_list) + int(product_list) + int(good_list))).place(x=100, y=175,
                                                                                                          width=200,
                                                                                                          height=25)

            year = tk.StringVar()
            year.set('2022')
            yc = ttk.Combobox(new_frame, state='readonly', textvariable=year, values=['2022', '2023'])
            yc.place(x=0, y=0, width=300, height=25)
            yb = ttk.Button(new_frame, text='查看', command=lambda: get_result(new_frame, year.get()))
            yb.place(x=300, y=0, width=50, height=25)
        if type == '2':
            # 月营业额
            new_frame = tk.Frame(root)
            new_frame.place(x=0, y=0, width=864, height=576)

            def get_result(master, year, month):
                # 根据year返回三个list#package_list#product_list#good_list
                package_list, product_list, good_list = month_money(year, month)
                ttk.Label(master, text='套餐总营业额').place(x=0, y=25, width=100, height=25)
                ttk.Label(master, text=package_list).place(x=100, y=25, width=200, height=25)
                ttk.Label(master, text='产品总营业额').place(x=0, y=75, width=100, height=25)
                ttk.Label(master, text=product_list).place(x=100, y=75, width=200, height=25)
                ttk.Label(master, text='商品总营业额').place(x=0, y=125, width=100, height=25)
                ttk.Label(master, text=good_list).place(x=100, y=125, width=200, height=25)
                ttk.Label(master, text='总营业额').place(x=0, y=175, width=100, height=25)
                ttk.Label(master, text=str(int(package_list) + int(product_list) + int(good_list))).place(x=100, y=175,
                                                                                                          width=200,
                                                                                                          height=25)

            year = tk.StringVar()
            month = tk.StringVar()
            year.set('2022')
            month.set('01')
            yc = ttk.Combobox(new_frame, state='readonly', textvariable=year, values=['2022', '2023'])
            yc.place(x=0, y=0, width=150, height=25)
            mc = ttk.Combobox(new_frame, state='readonly', textvariable=month,
                              values=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
            mc.place(x=150, y=0, width=150, height=25)
            yb = ttk.Button(new_frame, text='查看', command=lambda: get_result(new_frame, year.get(), month.get()))
            yb.place(x=300, y=0, width=50, height=25)

    # 查看房间状态
    def input_date(self):
        new_frame = tk.Frame(root)
        new_frame.place(x=0, y=0, width=864, height=576)

        ttk.Label(new_frame, text='输入日期').place(x=0, y=0, width=150, height=50)
        y = tk.StringVar()
        m = tk.StringVar()
        d = tk.StringVar()
        y.set('2023')
        m.set('01')
        d.set('01')
        i = ttk.Combobox(new_frame, state='readonly', textvariable=y, values=['2022', '2023'])
        i.place(x=0, y=50, width=50, height=50)
        j = ttk.Combobox(new_frame, state='readonly', textvariable=m,
                         values=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
        j.place(x=50, y=50, width=50, height=50)
        k = ttk.Combobox(new_frame, state='readonly', textvariable=d, values=[
            '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
            '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])
        k.place(x=100, y=50, width=50, height=50)
        b = ttk.Button(new_frame, text='确定', command=lambda: self.look_room(y.get() + '-' + m.get() + '-' + d.get()))
        b.place(x=0, y=100, width=150, height=50)

    def look_room(self, date):
        # 输入日期
        # 根据日期查询所有房间状态
        # list=房号，人数，shiyong
        list = a1(date)
        # list=[['123','1','14:00-14:30','15:30-16:00'],['223','2','14:30-15:30']]
        if list == []:
            w = tk.Tk()
            w.geometry('300x300')
            ttk.Label(w, text='该日无预约').place(x=0, y=0, width=300, height=300)
            return
        if list[0] == False:
            w = tk.Tk()
            w.geometry('300x300')
            ttk.Label(w, text=list[1]).place(x=0, y=0, width=300, height=300)
            return

        new_frame = tk.Frame(root)
        new_frame.place(x=0, y=0, width=864, height=576)
        if list[0] == False:
            return
        columns = ['房号', '容纳人数', '使用时间']
        table = ttk.Treeview(
            new_frame,  # 父容器
            height=len(list),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列
        )
        table.place(x=0, y=0, width=300, height=400)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.heading(columns[2], text=columns[2])
        table.column(columns[0], width=75, minwidth=75)
        table.column(columns[1], width=75, minwidth=75)
        table.column(columns[2], width=50, minwidth=50)
        for i in range(len(list)):
            for j in range(2, len(list[i])):
                table.insert('', 'end', values=[list[i][0], list[i][1], list[i][j]])

    # 修改房间状态
    def change_room(self):
        new_frame = tk.Frame(root)
        new_frame.place(x=0, y=0, width=864, height=576)
        ttk.Label(new_frame, text='现有房间一览').place(x=0, y=0, width=300, height=25)
        # 获取现有房间状态[房间号，容纳人数，服务员id，绑定服务员名字]
        room_list = room_all()
        # room_list=[
        # ['123','1','llx']
        # ]
        # room_list=[
        #   ['123','1','llx'],
        #   ['124','1','sse'],
        #   ['125','2','sse']
        # ]
        columns = ['房号', '可容纳人数', '服务员id', '服务员名字']
        table = ttk.Treeview(
            new_frame,  # 父容器
            height=len(room_list),  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列
        )
        table.place(x=0, y=25, width=400, height=400)
        table.heading(columns[0], text=columns[0])
        table.heading(columns[1], text=columns[1])
        table.heading(columns[2], text=columns[2])
        table.heading(columns[3], text=columns[3])
        table.column(columns[0], width=100, minwidth=100)
        table.column(columns[1], width=100, minwidth=100)
        table.column(columns[2], width=100, minwidth=100)
        table.column(columns[3], width=100, minwidth=100)
        for index, data in enumerate(room_list):
            table.insert('', 'end', values=data)  # 添加数据到末尾

    # 查看顾客，员工，套餐，产品，商品
    def customer_look(self):
        new_frame = tk.Frame(root)
        new_frame.place(x=0, y=0, width=864, height=576)

        def get_result():
            inp = ss.get()
            self.customer_list = a2(inp)
            # self.customer_list=[
            #    ['12345','mr li','mr','11111111111'],
            #    ['12036','miss liu','miss','22222222222']
            # ]
            columns = ['id', '姓名', '性别', '电话号码']
            table = ttk.Treeview(
                new_frame,  # 父容器
                height=len(self.customer_list),  # 表格显示的行数,height行
                columns=columns,  # 显示的列
                show='headings',  # 隐藏首列
            )
            table.place(x=0, y=50, width=350, height=400)
            table.heading(columns[0], text=columns[0])
            table.heading(columns[1], text=columns[1])
            table.heading(columns[2], text=columns[2])
            table.heading(columns[3], text=columns[3])
            table.column(columns[0], width=100, minwidth=100)
            table.column(columns[1], width=100, minwidth=100)
            table.column(columns[2], width=50, minwidth=50)
            table.column(columns[3], width=100, minwidth=100)
            for index, data in enumerate(self.customer_list):
                table.insert('', 'end', values=data)  # 添加数据到末尾

        ss = tk.StringVar()
        ttk.Label(new_frame, text='输入名字').place(x=0, y=0, width=300, height=25)
        s = ttk.Entry(new_frame, textvariable=ss)
        s.place(x=0, y=25, width=250, height=25)
        b = ttk.Button(new_frame, text='搜索', command=get_result)
        b.place(x=250, y=25, width=50, height=25)

    def worker_look(self):
        new_frame = tk.Frame(root)
        new_frame.place(x=0, y=0, width=864, height=576)

        # 放置搜索框
        def get_result(inp):
            self.customer_list_1 = a3(inp)
            # self.customer_list_1=[
            #    ['12345','mr li','mr','11111111111','技师','13'],
            #   ['12036','miss liu','miss','22222222222','服务员'],

            # ]
            self.columns = ['id', '姓名', '性别', '电话号码', '工种', '工时']
            table = ttk.Treeview(
                new_frame,  # 父容器
                height=len(self.customer_list_1),  # 表格显示的行数,height行
                columns=self.columns,  # 显示的列
                show='headings',  # 隐藏首列
            )
            table.place(x=0, y=50, width=450, height=400)
            table.heading(self.columns[0], text=self.columns[0])
            table.heading(self.columns[1], text=self.columns[1])
            table.heading(self.columns[2], text=self.columns[2])
            table.heading(self.columns[3], text=self.columns[3])
            table.heading(self.columns[4], text=self.columns[4])
            table.heading(self.columns[5], text=self.columns[5])
            table.column(self.columns[0], width=100, minwidth=100)
            table.column(self.columns[1], width=100, minwidth=100)
            table.column(self.columns[2], width=50, minwidth=50)
            table.column(self.columns[3], width=100, minwidth=100)
            table.column(self.columns[4], width=50, minwidth=50)
            table.column(self.columns[5], width=50, minwidth=50)
            for index, data in enumerate(self.customer_list_1):
                table.insert('', 'end', values=data)  # 添加数据到末尾

        ss = tk.StringVar()
        ttk.Label(new_frame, text='输入名字').place(x=0, y=0, width=300, height=25)
        s = ttk.Entry(new_frame, textvariable=ss)
        s.place(x=0, y=25, width=250, height=25)
        b = ttk.Button(new_frame, text='搜索', command=lambda: get_result(ss.get()))
        b.place(x=300, y=25, width=50, height=25)

    def package_look(self):
        new_frame = tk.Frame(root)
        new_frame.place(x=0, y=0, width=864, height=576)

        def get_result(inp):
            self.customer_list_1 = a4(inp)
            # self.customer_list_1=[
            #   ['12345','按摩套餐'],
            #    ['12036','足疗套餐']
            # ]
            self.columns = ['id', '套餐名', '价格', '功效']
            table = ttk.Treeview(
                new_frame,  # 父容器
                height=len(self.customer_list_1),  # 表格显示的行数,height行
                columns=self.columns,  # 显示的列
                show='headings',  # 隐藏首列
            )
            table.place(x=0, y=50, width=620, height=400)
            table.heading(self.columns[0], text=self.columns[0])
            table.heading(self.columns[1], text=self.columns[1])
            table.heading(self.columns[2], text=self.columns[2])
            table.heading(self.columns[3], text=self.columns[3])
            table.column(self.columns[0], width=70, minwidth=70)
            table.column(self.columns[1], width=100, minwidth=100)
            table.column(self.columns[2], width=50, minwidth=50)
            table.column(self.columns[3], width=400, minwidth=400)
            for index, data in enumerate(self.customer_list_1):
                table.insert('', 'end', values=data)  # 添加数据到末尾

        ss = tk.StringVar()
        ttk.Label(new_frame, text='输入名字').place(x=0, y=0, width=300, height=25)
        s = ttk.Entry(new_frame, textvariable=ss)
        s.place(x=0, y=25, width=250, height=25)
        b = ttk.Button(new_frame, text='搜索', command=lambda: get_result(ss.get()))
        b.place(x=300, y=25, width=50, height=25)

    def product_look(self):
        new_frame = tk.Frame(root)
        new_frame.place(x=0, y=0, width=864, height=576)

        def get_result(inp):
            self.customer_list_1 = a5(inp)
            # self.customer_list_1=[
            #    ['12345','精油','12','90'],
            #   ['12036','沐浴露','11','100']
            # ]
            self.columns = ['id', '产品名', '单价', '库存']
            table = ttk.Treeview(
                new_frame,  # 父容器
                height=len(self.customer_list_1),  # 表格显示的行数,height行
                columns=self.columns,  # 显示的列
                show='headings',  # 隐藏首列
            )
            table.place(x=0, y=50, width=350, height=400)
            table.heading(self.columns[0], text=self.columns[0])
            table.heading(self.columns[1], text=self.columns[1])
            table.heading(self.columns[2], text=self.columns[2])
            table.heading(self.columns[3], text=self.columns[3])
            table.column(self.columns[0], width=100, minwidth=100)
            table.column(self.columns[1], width=100, minwidth=100)
            table.column(self.columns[2], width=50, minwidth=50)
            table.column(self.columns[3], width=50, minwidth=50)
            for index, data in enumerate(self.customer_list_1):
                table.insert('', 'end', values=data)  # 添加数据到末尾

        ss = tk.StringVar()
        ttk.Label(new_frame, text='输入名字').place(x=0, y=0, width=300, height=25)
        s = ttk.Entry(new_frame, textvariable=ss)
        s.place(x=0, y=25, width=250, height=25)
        b = ttk.Button(new_frame, text='搜索', command=lambda: get_result(ss.get()))
        b.place(x=300, y=25, width=50, height=25)

    def good_look(self):
        new_frame = tk.Frame(root)
        new_frame.place(x=0, y=0, width=864, height=576)

        def get_result(inp):
            # 食物窗口
            self.customer_list_1 = a6(inp, 1)
            # self.customer_list_1=[
            #   ['12345','饼干','12','90'],
            #   ['12036','薯片','12','90']
            # ]
            self.columns = ['id', '产品名', '单价', '库存']
            table = ttk.Treeview(
                new_frame,  # 父容器
                height=len(self.customer_list_1),  # 表格显示的行数,height行
                columns=self.columns,  # 显示的列
                show='headings',  # 隐藏首列
            )
            table.place(x=0, y=50, width=350, height=400)
            table.heading(self.columns[0], text=self.columns[0])
            table.heading(self.columns[1], text=self.columns[1])
            table.heading(self.columns[2], text=self.columns[2])
            table.heading(self.columns[3], text=self.columns[3])
            table.column(self.columns[0], width=100, minwidth=100)
            table.column(self.columns[1], width=100, minwidth=100)
            table.column(self.columns[2], width=50, minwidth=50)
            table.column(self.columns[3], width=50, minwidth=50)
            for index, data in enumerate(self.customer_list_1):
                table.insert('', 'end', values=data)  # 添加数据到末尾
            # 酒水窗口
            self.customer_list_2 = a6(inp, 2)
            # self.customer_list_2=[
            #   ['12345','可乐','12','90'],
            #   ['12036','雪碧','12','90']
            # ]
            self.columns = ['id', '产品名', '单价', '库存']
            table2 = ttk.Treeview(
                new_frame,  # 父容器
                height=len(self.customer_list_2),  # 表格显示的行数,height行
                columns=self.columns,  # 显示的列
                show='headings',  # 隐藏首列
            )
            table2.place(x=360, y=50, width=350, height=400)
            table2.heading(self.columns[0], text=self.columns[0])
            table2.heading(self.columns[1], text=self.columns[1])
            table2.heading(self.columns[2], text=self.columns[2])
            table2.heading(self.columns[3], text=self.columns[3])
            table2.column(self.columns[0], width=100, minwidth=100)
            table2.column(self.columns[1], width=100, minwidth=100)
            table2.column(self.columns[2], width=50, minwidth=50)
            table2.column(self.columns[3], width=50, minwidth=50)
            for index, data in enumerate(self.customer_list_2):
                table2.insert('', 'end', values=data)  # 添加数据到末尾

        ss = tk.StringVar()
        ttk.Label(new_frame, text='输入名字').place(x=0, y=0, width=300, height=25)
        s = ttk.Entry(new_frame, textvariable=ss)
        s.place(x=0, y=25, width=250, height=25)
        b = ttk.Button(new_frame, text='搜索', command=lambda: get_result(ss.get()))
        b.place(x=300, y=25, width=50, height=25)

        # 修改/删除员工，套餐，产品，商品

    def change(self, type):
        new_frame = tk.Frame(root)
        new_frame.place(x=0, y=0, width=864, height=576)
        if type == 1:
            # 增加套餐
            global ls1
            ls1 = tk.PhotoImage(file="image/guanli/background/查询.png")
            ttk.Label(new_frame, image=ls1, background='#52755F').place(x=46, y=43, width=772, height=489)
            id = tk.StringVar()
            e1 = ttk.Entry(new_frame, textvariable=id)
            e1.place(x=254, y=89, width=361, height=27)
            global b1
            b1 = tk.PhotoImage(file="image/customer/button/确定.png")

            b = tk.Button(new_frame, image=b1, bg='#F7F6F2', border='0',
                          command=lambda: self.change_package(new_frame, id.get()))
            b.place(x=671, y=471, width=75, height=24)
        elif type == 2:
            # 增加产品
            global ls2
            ls2 = tk.PhotoImage(file="image/guanli/background/查询.png")
            ttk.Label(new_frame, image=ls2, background='#52755F').place(x=46, y=43, width=772, height=489)
            id = tk.StringVar()
            e1 = ttk.Entry(new_frame, textvariable=id)
            e1.place(x=254, y=89, width=361, height=27)
            global b2
            b2 = tk.PhotoImage(file="image/customer/button/确定.png")

            b = tk.Button(new_frame, image=b2, bg='#F7F6F2', border='0',
                          command=lambda: self.change_product(new_frame, id.get()))
            b.place(x=671, y=471, width=75, height=24)
        elif type == 3:
            # 增加商品
            global ls3
            ls3 = tk.PhotoImage(file="image/guanli/background/查询.png")
            ttk.Label(new_frame, image=ls3, background='#52755F').place(x=46, y=43, width=772, height=489)
            id = tk.StringVar()
            e1 = ttk.Entry(new_frame, textvariable=id)
            e1.place(x=254, y=89, width=361, height=27)
            global b4
            b4 = tk.PhotoImage(file="image/customer/button/确定.png")

            b = tk.Button(new_frame, image=b4, bg='#F7F6F2', border='0',
                          command=lambda: self.change_good(new_frame, id.get()))
            b.place(x=671, y=471, width=75, height=24)
        elif type == 4:
            # 修改员工
            global ls4
            ls4 = tk.PhotoImage(file="image/guanli/background/查询.png")
            ttk.Label(new_frame, image=ls4, background='#52755F').place(x=46, y=43, width=772, height=489)
            id = tk.StringVar()
            e1 = ttk.Entry(new_frame, textvariable=id)
            e1.place(x=254, y=89, width=361, height=27)
            global bl4
            bl4 = tk.PhotoImage(file="image/customer/button/确定.png")

            b = tk.Button(new_frame, image=bl4, bg='#F7F6F2', border='0',
                          command=lambda: self.change_worker(new_frame, id.get()))
            b.place(x=671, y=471, width=75, height=24)

    def change_worker(self, new_frame, id):
        # 查询id是否正确
        k = b1(id)
        # k = True
        if k == False:
            ttk.Label(new_frame, background='#F7F6F2', text='id错误').place(x=254, y=450, width=100, height=50)
        else:
            # 查询该id的信息
            this_list = fun_4(id)
            # this_list=['1234','xxy','女','123456789101','2001-12','技师','2000',None]
            global ll4
            ll4 = tk.PhotoImage(file="image/guanli/background/增加员工.png")
            ttk.Label(new_frame, image=ll4, background='#52755F').place(x=46, y=43, width=772, height=489)
            name = tk.StringVar()
            sex = tk.StringVar()
            phone = tk.StringVar()
            salary = tk.StringVar()
            note = tk.StringVar()
            name.set(this_list[1])
            sex.set(this_list[2])
            phone.set(this_list[3])
            typ = this_list[4]
            salary.set(this_list[5])
            note.set(this_list[6])

            e1 = ttk.Entry(new_frame, textvariable=name)
            e2 = ttk.Combobox(new_frame, state='readonly', textvariable=sex, values=['男', '女'])
            e3 = ttk.Entry(new_frame, textvariable=phone)
            e5 = ttk.Label(new_frame, text=typ)
            e6 = ttk.Entry(new_frame, textvariable=salary)
            e7 = ttk.Entry(new_frame, textvariable=note)
            e1.place(x=254, y=89, width=361, height=27)
            e2.place(x=254, y=130, width=361, height=27)
            e3.place(x=254, y=171, width=361, height=27)
            e5.place(x=254, y=253, width=361, height=27)
            e6.place(x=254, y=294, width=361, height=27)
            e7.place(x=254, y=335, width=361, height=121)
            # 增加按钮
            global bll4
            bll4 = tk.PhotoImage(file="image/customer/button/完成.png")

            b = tk.Button(new_frame, image=bll4, bg='#F7F6F2', border='0',
                          command=lambda: self.real_change_worker(new_frame, id, name.get(), sex.get(), phone.get(),
                                                                  typ, salary.get(),
                                                                  note.get()))
            b.place(x=671, y=471, width=75, height=24)
            # 删除按钮
            d = ttk.Button(new_frame, text='删除该员工', command=lambda: self.dele(id, 1))
            d.place(x=671 - 75, y=471, width=75, height=24)

    def real_change_worker(self, new_frame, id, name, sex, phone, type, salary, note):

        t = tk.StringVar()
        if name == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入姓名').place(x=254, y=470, width=100, height=50)
            return
        if sex == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入性别').place(x=254, y=470, width=100, height=50)
            return
        if phone == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入电话').place(x=254, y=470, width=100, height=50)
            return
        if type == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入工种').place(x=254, y=470, width=100, height=50)
            return
        list = [name, sex, phone, type, salary, note]
        # 修改信息
        k = bb2(id, list)
        # k='123'
        if k[0] == False:
            ttk.Label(new_frame, background='#F7F6F2', text=k[1]).place(x=254, y=470, width=100, height=50)
            return
        ttk.Label(new_frame, background='#F7F6F2', text='修改成功').place(x=254, y=470, width=100, height=50)

    def change_package(self, new_frame, id):
        # 查询id是否正确
        k = b3(id)
        # k=True
        if k == False:
            ttk.Label(new_frame, background='#F7F6F2', text='id错误').place(x=254, y=450, width=100, height=50)
        else:
            # 查询该id的信息
            this_list = bb4(id)
            print(this_list)
            # this_list=['1234','按摩套餐','123','456',None,'99',None]
            global l1
            l1 = tk.PhotoImage(file="image/guanli/background/增加套餐.png")
            ttk.Label(new_frame, image=l1, background='#52755F').place(x=46, y=43, width=772, height=489)
            pro_list = b5()
            # pro_list=[
            #   '123','456','789','102'
            # ]
            w = tk.Tk()
            w.geometry('650x600')
            self.columns = ['id', '产品名', '单价', '功效']
            table2 = ttk.Treeview(
                w,  # 父容器
                height=len(pro_list),  # 表格显示的行数,height行
                columns=self.columns,  # 显示的列
                show='headings',  # 隐藏首列
            )
            table2.place(x=0, y=0, width=650, height=600)
            table2.heading(self.columns[0], text=self.columns[0])
            table2.heading(self.columns[1], text=self.columns[1])
            table2.heading(self.columns[2], text=self.columns[2])
            table2.heading(self.columns[3], text=self.columns[3])
            table2.column(self.columns[0], width=100, minwidth=100)
            table2.column(self.columns[1], width=100, minwidth=100)
            table2.column(self.columns[2], width=50, minwidth=50)
            table2.column(self.columns[3], width=400, minwidth=400)
            for index, data in enumerate(pro_list):
                table2.insert('', 'end', values=data)  # 添加数据到末尾

            pr_list = []
            for i in range(len(pro_list)):
                pr_list.append(pro_list[i][0])
            name = tk.StringVar()
            price = tk.StringVar()
            eff = tk.StringVar()
            name.set(this_list[1])
            pro1 = this_list[2]
            pro2 = this_list[3]
            pro3 = this_list[4]
            price.set(this_list[5])
            eff.set(this_list[6])
            e1 = ttk.Entry(new_frame, textvariable=name)
            e2 = ttk.Entry(new_frame, textvariable=price)
            e3 = ttk.Entry(new_frame, textvariable=eff)
            c1 = ttk.Label(new_frame, text=pro1)
            c2 = ttk.Label(new_frame, text=pro2)
            c3 = ttk.Label(new_frame, text=pro3)
            e1.place(x=254, y=89, width=361, height=27)
            e2.place(x=254, y=171, width=361, height=27)
            e3.place(x=254, y=212, width=361, height=187)
            c1.place(x=254, y=130, width=99, height=27)
            c2.place(x=382, y=130, width=99, height=27)
            c3.place(x=516, y=130, width=99, height=27)
            # 增加按钮
            global bl
            bl = tk.PhotoImage(file="image/customer/button/完成.png")

            b = tk.Button(new_frame, image=bl, bg='#F7F6F2', border='0',
                          command=lambda: self.real_change_package(new_frame, id, name.get(), pro1, pro2,
                                                                   pro3,
                                                                   price.get(), eff.get()))
            b.place(x=671, y=471, width=75, height=24)
            # 删除按钮
            d = ttk.Button(new_frame, text='删除该套餐', command=lambda: self.dele(id, 2))
            d.place(x=671 - 75, y=471, width=75, height=24)

    def real_change_package(self, new_frame, id, name, pro1, pro2, pro3, price, eff):

        t = tk.StringVar()
        if name == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入套餐名').place(x=254, y=450, width=100, height=50)
            return
        if price == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入价格').place(x=254, y=450, width=100, height=50)
            return
        listt = [name, price, pro1, pro2, pro3, eff]
        k = b6(id, listt)
        # k='123'
        if k[0] == False:
            ttk.Label(new_frame, background='#F7F6F2', text=k[1]).place(x=254, y=450, width=100, height=50)
            return
        ttk.Label(new_frame, background='#F7F6F2', text='修改成功').place(x=254, y=450, width=100, height=50)

    def change_product(self, new_frame, id):
        # 查询id是否正确
        k = b7(id)
        # k=True
        if k == False:
            ttk.Label(new_frame, background='#F7F6F2', text='id错误').place(x=254, y=450, width=100, height=50)
        else:
            # 查询该id的信息
            this_list = fun_9(id)
            # 名字价格库存功效
            # this_list=['1234','精油','12','11',None]
            global ll2
            ll2 = tk.PhotoImage(file="image/guanli/background/增加产品.png")
            ttk.Label(new_frame, image=ll2, background='#52755F').place(x=46, y=43, width=772, height=489)
            name = tk.StringVar()
            pro1 = tk.StringVar()
            price = tk.StringVar()
            eff = tk.StringVar()
            name.set(this_list[1])
            pro1.set(this_list[3])
            price.set(this_list[2])
            eff.set(this_list[4])
            e1 = ttk.Entry(new_frame, textvariable=name)
            e2 = ttk.Entry(new_frame, textvariable=price)
            e3 = ttk.Entry(new_frame, textvariable=eff)
            c1 = ttk.Entry(new_frame, textvariable=pro1)
            e1.place(x=254, y=89, width=361, height=27)
            e2.place(x=254, y=171, width=361, height=27)
            e3.place(x=254, y=212, width=361, height=187)
            c1.place(x=254, y=130, width=361, height=27)
            # 增加按钮
            global bll2
            bll2 = tk.PhotoImage(file="image/customer/button/完成.png")

            b = tk.Button(new_frame, image=bll2, bg='#F7F6F2', border='0',
                          command=lambda: self.real_change_product(new_frame, id, name.get(), pro1.get(), price.get(),
                                                                   eff.get()))
            b.place(x=671, y=471, width=75, height=24)
            # 删除按钮
            d = ttk.Button(new_frame, text='删除该产品', command=lambda: self.dele(id, 2))
            d.place(x=671 - 75, y=471, width=75, height=24)

    def real_change_product(self, new_frame, id, name, count, price, eff):

        t = tk.StringVar()
        if name == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入产品名').place(x=254, y=450, width=100, height=50)
            return
        if price == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入价格').place(x=254, y=450, width=100, height=50)
            return
        list = [id, name, count, price, eff]
        # 修改信息
        k = fun_10(list)
        # k='123'
        if k[0] == False:
            ttk.Label(new_frame, background='#F7F6F2', text=k[1]).place(x=254, y=450, width=100, height=50)
            return
        ttk.Label(new_frame, background='#F7F6F2', text='修改成功').place(x=254, y=450, width=100, height=50)

    def change_good(self, new_frame, id):
        # 查询id是否正确
        k = b8(id)
        # k=True
        if k == False:
            ttk.Label(new_frame, background='#F7F6F2', text='id错误').place(x=254, y=450, width=100, height=50)
        else:
            # 查询该id的信息
            this_list = fun_99(id)
            # this_list=['1234','薯片','12','12','食品']
            global ll3
            ll3 = tk.PhotoImage(file="image/guanli/background/增加商品.png")
            ttk.Label(new_frame, image=ll3, background='#52755F').place(x=46, y=43, width=772, height=489)
            name = tk.StringVar()
            pro1 = tk.StringVar()
            price = tk.StringVar()
            name.set(this_list[1])
            price.set(this_list[2])
            pro1.set(this_list[3])
            eff = this_list[4]
            e1 = ttk.Entry(new_frame, textvariable=name)
            e2 = ttk.Entry(new_frame, textvariable=price)
            e3 = ttk.Label(new_frame, text=eff)
            c1 = ttk.Entry(new_frame, textvariable=pro1)
            e1.place(x=254, y=89, width=361, height=27)
            e2.place(x=254, y=171, width=361, height=27)
            e3.place(x=254, y=212, width=361, height=27)
            c1.place(x=254, y=130, width=361, height=27)
            # 增加按钮
            global bll3
            bll3 = tk.PhotoImage(file="image/customer/button/完成.png")

            b = tk.Button(new_frame, image=bll3, bg='#F7F6F2', border='0',
                          command=lambda: self.real_change_good(new_frame, id, name.get(), pro1.get(), price.get(),
                                                                eff))
            b.place(x=671, y=471, width=75, height=24)
            # 删除按钮
            d = ttk.Button(new_frame, text='删除该商品', command=lambda: self.dele(id, 2))
            d.place(x=671 - 75, y=471, width=75, height=24)

    def real_change_good(self, new_frame, id, name, count, price, type):

        t = tk.StringVar()
        if name == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入商品名').place(x=254, y=450, width=100, height=50)
            return
        if price == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入价格').place(x=254, y=450, width=100, height=50)
            return
        if type == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入商品类型').place(x=254, y=450, width=100, height=50)
            return
        list = [id, name, price,count ]
        # 修改信息
        k = fun_10(list)
        # k='123'
        if k[0] == False:
            ttk.Label(new_frame, background='#F7F6F2', text=k[1]).place(x=254, y=450, width=100, height=50)
            return
        ttk.Label(new_frame, background='#F7F6F2', text='修改成功').place(x=254, y=450, width=100, height=50)

    # 删除函数
    def dele(self, id, type):
        if type == 1:
            # 删除员工
            new_frame = tk.Frame(root)
            new_frame.place(x=0, y=0, width=864, height=576)

            def real_delete(id):
                k = dd1(id)
                # k=False
                if k == False:
                    ttk.Label(new_frame, text='删除失败').place(x=0, y=0, width=300, height=250)
                else:
                    ttk.Label(new_frame, text='删除成功').place(x=0, y=0, width=300, height=250)

            ttk.Label(new_frame, text='确认删除？').place(x=0, y=0, width=300, height=50)
            b = ttk.Button(new_frame, text='确认', command=lambda: real_delete(id))
            b.place(x=250, y=50, width=50, height=25)

        if type == 2:
            # 删除套餐
            new_frame = tk.Frame(root)
            new_frame.place(x=0, y=0, width=864, height=576)

            def real_delete(id):
                print(123)
                k = d2(id)
                # k=False
                if k[0] == False:
                    ttk.Label(new_frame, text=k[1]).place(x=0, y=0, width=300, height=250)
                else:
                    ttk.Label(new_frame, text='删除成功').place(x=0, y=0, width=300, height=250)

            ttk.Label(new_frame, text='确认删除？').place(x=0, y=0, width=300, height=25)

            b = ttk.Button(new_frame, text='确认', command=lambda: real_delete(id))
            b.place(x=250, y=50, width=50, height=25)

    # 增加套餐，产品，商品，员工
    def add(self, type):
        new_frame = tk.Frame(root)
        new_frame.place(x=0, y=0, width=864, height=576)
        if type == 1:
            # 增加套餐
            global l1
            l1 = tk.PhotoImage(file="image/guanli/background/增加套餐.png")
            ttk.Label(new_frame, image=l1, background='#52755F').place(x=46, y=43, width=772, height=489)
            pro_list = b5()
            # pro_list=[
            #   '123','456','789','102'
            # ]
            w = tk.Tk()
            w.geometry('650x600')
            self.columns = ['id', '产品名', '单价', '功效']
            table2 = ttk.Treeview(
                w,  # 父容器
                height=len(pro_list),  # 表格显示的行数,height行
                columns=self.columns,  # 显示的列
                show='headings',  # 隐藏首列
            )
            table2.place(x=0, y=0, width=650, height=600)
            table2.heading(self.columns[0], text=self.columns[0])
            table2.heading(self.columns[1], text=self.columns[1])
            table2.heading(self.columns[2], text=self.columns[2])
            table2.heading(self.columns[3], text=self.columns[3])
            table2.column(self.columns[0], width=100, minwidth=100)
            table2.column(self.columns[1], width=100, minwidth=100)
            table2.column(self.columns[2], width=50, minwidth=50)
            table2.column(self.columns[3], width=400, minwidth=400)
            for index, data in enumerate(pro_list):
                table2.insert('', 'end', values=data)  # 添加数据到末尾

            pr_list = []
            for i in range(len(pro_list)):
                pr_list.append(pro_list[i][0])

            name = tk.StringVar()
            pro1 = tk.StringVar()
            pro2 = tk.StringVar()
            pro3 = tk.StringVar()
            price = tk.StringVar()
            eff = tk.StringVar()
            e1 = ttk.Entry(new_frame, textvariable=name)
            e2 = ttk.Entry(new_frame, textvariable=price)
            e3 = ttk.Entry(new_frame, textvariable=eff)
            c1 = ttk.Combobox(new_frame, state='readonly', textvariable=pro1, values=pr_list)
            c2 = ttk.Combobox(new_frame, state='readonly', textvariable=pro2, values=pr_list)
            c3 = ttk.Combobox(new_frame, state='readonly', textvariable=pro3, values=pr_list)
            e1.place(x=254, y=89, width=361, height=27)
            e2.place(x=254, y=171, width=361, height=27)
            e3.place(x=254, y=212, width=361, height=187)
            c1.place(x=254, y=130, width=99, height=27)
            c2.place(x=382, y=130, width=99, height=27)
            c3.place(x=516, y=130, width=99, height=27)
            # 增加按钮
            global bl
            bl = tk.PhotoImage(file="image/customer/button/完成.png")

            b = tk.Button(new_frame, image=bl, bg='#F7F6F2', border='0',
                          command=lambda: self.add_package(new_frame, name.get(), pro1.get(), pro2.get(), pro3.get(),
                                                           price.get(),
                                                           eff.get()))
            b.place(x=671, y=471, width=75, height=24)
        elif type == 2:
            # 增加产品
            global l2
            l2 = tk.PhotoImage(file="image/guanli/background/增加产品.png")
            ttk.Label(new_frame, image=l2, background='#52755F').place(x=46, y=43, width=772, height=489)
            name = tk.StringVar()
            pro1 = tk.StringVar()
            pro2 = tk.StringVar()
            pro3 = tk.StringVar()
            price = tk.StringVar()
            eff = tk.StringVar()
            e1 = ttk.Entry(new_frame, textvariable=name)
            e2 = ttk.Entry(new_frame, textvariable=price)
            e3 = ttk.Entry(new_frame, textvariable=eff)
            c1 = ttk.Entry(new_frame, textvariable=pro1)
            e1.place(x=254, y=89, width=361, height=27)
            e2.place(x=254, y=171, width=361, height=27)
            e3.place(x=254, y=212, width=361, height=187)
            c1.place(x=254, y=130, width=361, height=27)
            # 增加按钮
            global bl2
            bl2 = tk.PhotoImage(file="image/customer/button/完成.png")

            b = tk.Button(new_frame, image=bl2, bg='#F7F6F2', border='0',
                          command=lambda: self.add_product(new_frame, name.get(), pro1.get(), price.get(), eff.get()))
            b.place(x=671, y=471, width=75, height=24)
        elif type == 3:
            # 增加商品
            global l3
            l3 = tk.PhotoImage(file="image/guanli/background/增加商品.png")
            ttk.Label(new_frame, image=l3, background='#52755F').place(x=46, y=43, width=772, height=489)
            name = tk.StringVar()
            pro1 = tk.StringVar()
            pro2 = tk.StringVar()
            pro3 = tk.StringVar()
            price = tk.StringVar()
            eff = tk.StringVar()
            e1 = ttk.Entry(new_frame, textvariable=name)
            e2 = ttk.Entry(new_frame, textvariable=price)
            e3 = ttk.Combobox(new_frame, state='readonly', textvariable=eff, values=['食物', '酒水'])
            c1 = ttk.Entry(new_frame, textvariable=pro1)
            e1.place(x=254, y=89, width=361, height=27)
            e2.place(x=254, y=171, width=361, height=27)
            e3.place(x=254, y=212, width=361, height=27)
            c1.place(x=254, y=130, width=361, height=27)
            # 增加按钮
            global bl3
            bl3 = tk.PhotoImage(file="image/customer/button/完成.png")

            b = tk.Button(new_frame, image=bl3, bg='#F7F6F2', border='0',
                          command=lambda: self.add_good(new_frame, name.get(), pro1.get(), price.get(), eff.get()))
            b.place(x=671, y=471, width=75, height=24)
        elif type == 4:
            # 增加员工
            global l4
            l4 = tk.PhotoImage(file="image/guanli/background/增加员工.png")
            ttk.Label(new_frame, image=l4, background='#52755F').place(x=46, y=43, width=772, height=489)
            name = tk.StringVar()
            sex = tk.StringVar()
            phone = tk.StringVar()
            birth1 = tk.StringVar()
            birth2 = tk.StringVar()
            typ = tk.StringVar()
            salary = tk.StringVar()
            note = tk.StringVar()

            e1 = ttk.Entry(new_frame, textvariable=name)
            e2 = ttk.Combobox(new_frame, state='readonly', textvariable=sex, values=['男', '女'])
            e3 = ttk.Entry(new_frame, textvariable=phone)

            e5 = ttk.Combobox(new_frame, state='readonly', textvariable=typ, values=['技师', '服务员'])
            e6 = ttk.Entry(new_frame, textvariable=salary)
            e7 = ttk.Entry(new_frame, textvariable=note)
            e1.place(x=254, y=89, width=361, height=27)
            e2.place(x=254, y=130, width=361, height=27)
            e3.place(x=254, y=171, width=361, height=27)
            e5.place(x=254, y=253, width=361, height=27)
            e6.place(x=254, y=294, width=361, height=27)
            e7.place(x=254, y=335, width=361, height=121)
            # 增加按钮
            global bl4
            bl4 = tk.PhotoImage(file="image/customer/button/完成.png")

            b = tk.Button(new_frame, image=bl4, bg='#F7F6F2', border='0',
                          command=lambda: self.add_worker(new_frame, name.get(), sex.get(), phone.get(), typ.get(),
                                                          salary.get(),
                                                          note.get()))
            b.place(x=671, y=471, width=75, height=24)

    def add_worker(self, new_frame, name, sex, phone, type, salary, note):

        t = tk.StringVar()
        if name == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入姓名').place(x=254, y=470, width=100, height=50)
            return
        if sex == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入性别').place(x=254, y=470, width=100, height=50)
            return
        if phone == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入电话').place(x=254, y=470, width=100, height=50)
            return
        if type == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入工种').place(x=254, y=470, width=100, height=50)
            return
        listt = [name, sex, phone, type, salary, note]
        k = b9(listt)
        # k='123'
        if k[0] == False:
            ttk.Label(new_frame, background='#F7F6F2', text=k[1]).place(x=254, y=470, width=100, height=50)
            return
        ttk.Label(new_frame, background='#F7F6F2', text='添加成功').place(x=0, y=0, width=864, height=597)

    def add_package(self, new_frame, name, pro1, pro2, pro3, price, eff):

        t = tk.StringVar()
        if name == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入套餐名').place(x=254, y=450, width=100, height=50)
            return
        if pro1 == t.get() and pro2 == t.get() and pro3 == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='至少选择一个产品').place(x=254, y=450, width=100, height=50)
            return
        if price == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入价格').place(x=254, y=450, width=100, height=50)
            return
        listt = [name, price, pro1, pro2, pro3, eff]
        k = b10(listt)
        # k='123'
        if k[0] == False:
            ttk.Label(new_frame, background='#F7F6F2', text=k[1]).place(x=254, y=450, width=100, height=50)
            return
        ttk.Label(new_frame, background='#F7F6F2', text='添加成功').place(x=0, y=0, width=864, height=597)

    def add_product(self, new_frame, name, count, price, eff):

        t = tk.StringVar()
        if name == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入产品名').place(x=254, y=450, width=100, height=50)
            return
        if price == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入价格').place(x=254, y=450, width=100, height=50)
            return
        list = [name, count, price, eff]
        k = fun_11(list)
        # k='123'
        if k[0] == False:
            ttk.Label(new_frame, background='#F7F6F2', text=k[1]).place(x=254, y=450, width=100, height=50)
            return
        ttk.Label(new_frame, background='#F7F6F2', text='添加成功').place(x=0, y=0, width=864, height=597)

    def add_good(self, new_frame, name, count, price, type):
        t = tk.StringVar()
        if name == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入商品名').place(x=254, y=450, width=100, height=50)
            return
        if price == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入价格').place(x=254, y=450, width=100, height=50)
            return
        if type == t.get():
            ttk.Label(new_frame, background='#F7F6F2', text='未输入商品类型').place(x=254, y=450, width=100, height=50)
            return
        listt = [type, name, price, count]
        k = fun_12(listt)
        # k='123'
        if k[0] == False:
            ttk.Label(new_frame, background='#F7F6F2', text=k[1]).place(x=254, y=450, width=100, height=50)
            return
        ttk.Label(new_frame, background='#F7F6F2', text='添加成功').place(x=0, y=0, width=864, height=597)


##########3员工端#########################
class yuangong:
    def __init__(self, id):
        self.frame_new = tk.Frame(root, bg='#84877E')
        # 背景图导入
        global landf
        landf = tk.PhotoImage(file="image/guanli/background/管理界面.png")
        ttk.Label(self.frame_new, image=landf).place(x=0 * 40, y=0 * 40, width=864, height=576)
        self.frame_new.place(x=-2, y=0, width=864, height=576)

        self.menubar = tk.Menu(self.frame_new)
        self.menubar.add_command(label='工作安排', command=lambda: self.work_arrange(id))
        self.menubar.add_command(label='个人信息', command=lambda: self.message(id))
        root.config(menu=self.menubar)

    def work_arrange(self, id):
        work_arrange(id)

    def message(self, id):
        worker_message(id)


class work_arrange:
    def __init__(self, id):
        w = tk.Tk()
        w.geometry('900x900')
        type = c1(id)
        if type == '技师':
            # 根据id返回工作安排
            work_list = c2(id)
            # work_list = [
            #     ['123', '14:30', '15:30', [['147', '001'], ['258', '001'], ['369', '002']]],
            #    ['125', '15:30', '16:30', [['147', '001'], ['258', '001'], ['369', '002']]],
            # ]

            columns = ['房号', '开始时间', '结束时间', '套餐', '产品']
            table = ttk.Treeview(
                w,  # 父容器
                height=len(work_list),  # 表格显示的行数,height行
                columns=columns,  # 显示的列
                show='headings',  # 隐藏首列
            )
            table.place(x=0, y=0, width=700, height=400)
            table.heading(columns[0], text=columns[0])
            table.heading(columns[1], text=columns[1])
            table.heading(columns[2], text=columns[2])
            table.heading(columns[3], text=columns[3])
            table.heading(columns[4], text=columns[4])
            table.column(columns[0], width=100, minwidth=100)
            table.column(columns[1], width=200, minwidth=200)
            table.column(columns[2], width=200, minwidth=200)
            table.column(columns[3], width=100, minwidth=100)
            table.column(columns[4], width=100, minwidth=100)
            for i in range(len(work_list)):
                table.insert('', 'end',
                             values=[work_list[i][0], work_list[i][1], work_list[i][2], work_list[i][3][0],
                                     work_list[i][3][1]])

        else:
            # 根据id返回工作安排
            global new_work_list
            new_work_list = c3(id)

            # 商品集合包括[[商品名,数量]......]
            # 数量也是字符串
            # work_list=[房号,订单号
            #      ['2022-12-28 20:11',[商品集合]],
            #       ['2022-12-28 20:20',[商品集合]],
            # ]
            # work_list = ['123', '1234',
            #             ['2022-12-28 20:11', [['薯片', '3'], ['可乐', '1']]],
            #             ['2022-12-28 20:20', [['薯片', '3'], ['矿泉水', '1']]],
            #             ['2022-12-28 20:25', [['饼干', '3'], ['可乐', '1']]],
            #             ]
            def show_arrange(id, work_list):
                # 将work_list回传，获取新的work_list
                new_work_list = c33(id, work_list)
                show_list(id, new_work_list)

            def show_list(id, new_work_list):
                if new_work_list == False:
                    ttk.Label(w, text='暂无新任务').place(x=0, y=0, width=450, height=400)
                    b = ttk.Button(w, text='刷新', command=lambda: show_arrange(new_work_list))
                    b.place(x=0, y=400, width=250, height=25)
                else:
                    show_list = []
                    # show_list格式为[[商品名,数量]]
                    show_list.append([new_work_list[2][1][0][0], new_work_list[2][1][0][1]])
                    for i in range(2, len(new_work_list)):
                        if i == 2:
                            for j in range(1, len(new_work_list[i][1])):
                                for k in range(len(show_list)):
                                    print(new_work_list[i][1][j])
                                    if new_work_list[i][1][j][0] == show_list[k][0]:
                                        show_list[k][1] = str(int(show_list[k][1]) + int(new_work_list[i][1][j][1]))

                                        break
                                    if k == len(show_list) - 1 and new_work_list[i][1][j][0] != show_list[k][0]:
                                        show_list.append([new_work_list[i][1][j][0], new_work_list[i][1][j][1]])
                        else:
                            for j in range(len(new_work_list[i][1])):
                                for k in range(len(show_list)):
                                    print(new_work_list[i][1][j])
                                    if new_work_list[i][1][j][0] == show_list[k][0]:
                                        show_list[k][1] = str(int(show_list[k][1]) + int(new_work_list[i][1][j][1]))

                                        break
                                    if k == len(show_list) - 1 and new_work_list[i][1][j][0] != show_list[k][0]:
                                        show_list.append([new_work_list[i][1][j][0], new_work_list[i][1][j][1]])
                    columns = ['房号', '商品名', '数量']
                    table = ttk.Treeview(
                        w,  # 父容器
                        height=len(new_work_list),  # 表格显示的行数,height行
                        columns=columns,  # 显示的列
                        show='headings',  # 隐藏首列
                    )
                    table.place(x=0, y=0, width=450, height=400)
                    table.heading(columns[0], text=columns[0])
                    table.heading(columns[1], text=columns[1])
                    table.heading(columns[2], text=columns[2])
                    table.column(columns[0], width=100, minwidth=100)
                    table.column(columns[1], width=100, minwidth=100)
                    table.column(columns[2], width=50, minwidth=50)
                    for i in range(len(show_list)):
                        table.insert('', 'end', values=[new_work_list[0], show_list[i][0], show_list[i][1]])

                    b = ttk.Button(w, text='完成任务，查看下一条', command=lambda: show_arrange(id, new_work_list))
                    b.place(x=0, y=400, width=250, height=25)

            show_list(id, new_work_list)
        w.mainloop()


class worker_message:
    def __init__(self, id):
        w = tk.Toplevel()
        w.geometry('375x651')
        type = c1(id)
        # type = '服务员'
        if type == '技师':
            # 背景图导入
            global landff
            landff = tk.PhotoImage(file="image/yuangong/技师.png")
            ttk.Label(w, image=landff).place(x=0 * 40, y=-5, width=375, height=651)
            list = c4(id)
            # list = ['123', 'xxy', '女', '11111111111', '技师', None, '13', '2000']
            ttk.Label(w, text=list[0], background='white', font=('宋体', '16'), foreground='#7F7F7F').place(x=119, y=67,
                                                                                                          width=190,
                                                                                                          height=24)
            ttk.Label(w, text=list[1], background='white', font=('宋体', '16'), foreground='#7F7F7F').place(x=119, y=101,
                                                                                                          width=190,
                                                                                                          height=24)
            ttk.Label(w, text=list[2], background='white', font=('宋体', '16'), foreground='#7F7F7F').place(x=119, y=135,
                                                                                                          width=190,
                                                                                                          height=24)
            ttk.Label(w, text=list[3], background='white', font=('宋体', '16'), foreground='#7F7F7F').place(x=119, y=169,
                                                                                                          width=190,
                                                                                                          height=24)

            ttk.Label(w, text=list[4], background='white', font=('宋体', '16'), foreground='#7F7F7F').place(x=119, y=237,
                                                                                                          width=190,
                                                                                                          height=24)
            ttk.Label(w, text=list[5], background='white', font=('宋体', '16'), foreground='#7F7F7F').place(x=119, y=271,
                                                                                                          width=190,
                                                                                                          height=24)
            ttk.Label(w, text=list[6], background='white', font=('宋体', '16'), foreground='#7F7F7F').place(x=119, y=339,
                                                                                                          width=190,
                                                                                                          height=24)
            ttk.Label(w, text=str(int(int(list[7]) + float(list[6]) * 60)) + ' RMB', background='white',
                      font=('宋体', '36'),
                      foreground='#7F7F7F', anchor='center').place(x=59, y=417, width=250, height=132)
        else:
            # 背景图导入
            global landfff
            landfff = tk.PhotoImage(file="image/yuangong/服务员.png")
            ttk.Label(w, image=landfff).place(x=0 * 40, y=-5, width=375, height=651)
            list = c5(id)
            # list = ['123', 'xxy', '女', '11111111111', '2022-13', '服务员', None, '2000']
            ttk.Label(w, text=list[0], background='white', font=('宋体', '16'), foreground='#7F7F7F').place(x=119, y=67,
                                                                                                          width=190,
                                                                                                          height=24)
            ttk.Label(w, text=list[1], background='white', font=('宋体', '16'), foreground='#7F7F7F').place(x=119, y=101,
                                                                                                          width=190,
                                                                                                          height=24)
            ttk.Label(w, text=list[2], background='white', font=('宋体', '16'), foreground='#7F7F7F').place(x=119, y=135,
                                                                                                          width=190,
                                                                                                          height=24)
            ttk.Label(w, text=list[3], background='white', font=('宋体', '16'), foreground='#7F7F7F').place(x=119, y=169,
                                                                                                          width=190,
                                                                                                          height=24)

            ttk.Label(w, text=list[4], background='white', font=('宋体', '16'), foreground='#7F7F7F').place(x=119, y=237,
                                                                                                          width=190,
                                                                                                          height=24)
            ttk.Label(w, text=list[5], background='white', font=('宋体', '16'), foreground='#7F7F7F').place(x=119, y=271,
                                                                                                          width=190,
                                                                                                          height=24)
            ttk.Label(w, text=list[6] + ' RMB', background='white', font=('宋体', '36'), foreground='#7F7F7F',
                      anchor='center').place(x=59, y=417, width=250, height=132)

        w.mainloop()


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from time import sleep

root = tk.Tk()
# 网页名称大小背景色
root.title('山青阁足疗城管理系统')
root.geometry('864x576')
root.attributes('-alpha', 1)
#page = guanli()
#page = customer_1('2')
page = login()
root.mainloop()
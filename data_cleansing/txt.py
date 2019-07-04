import os, re, MySQLdb
conn = MySQLdb.Connect(host='127.0.0.1', user='root', password='123456', db='end_project', port=3306, charset='utf8')
cursor = conn.cursor()
path = r'F:\real_python\git_project\data_cleansing\txt'
for d in os.listdir(path):
    print(4, d)
    with open(path+'\\'+d, 'r') as r:
        text = r.readlines()
    print(text)
    text1 = []
    for i in text:
        if i != '\n':
            i = i.replace('\n', '')
            text1.append(i)
    name = " "
    job_p = " "
    sex = " "
    age = " "
    birthday = " "
    academic = " "
    nation = " "
    politics = " "
    exper = " "
    addr = " "
    census = " "
    phone = " "
    email = " "
    job_status = " "
    job_addr = " "
    job_exp = " "
    job_ind = " "
    job_salary = " "
    edu = " "
    marry = " "
    # text.remove('\n')
    print(text1)
    name = text1[0].split(' ')[0]
    job_p = ''.join(text1[0].split(' ')[1:])
    for q in text1[1].split('|'):
        if re.search('男', q) or re.search('女', q):
            sex = q
        elif re.search('婚', q):
            marry = q
        elif re.search('年', q):
            birthday = q
        elif re.search('岁', q):
            age = q
        elif re.search('本科', q) or re.search('大专', q) or re.search('硕士', q) or re.search('MBA', q) or re.search('博士',q) or re.search('高中', q):
            academic = q
        elif re.search('国籍', q):
            nation = q
        elif re.search('群众', q) or re.search('党员', q) or re.search('团员', q) or re.search('派', q):
            politics = q
    for w in text1:
        if re.search('工作经验：', w):
            exper = w.split('：')[1]
        elif re.search('现居住地', w):
            addr = w.split('：')[1]
        elif re.search('户 籍 地', w):
            census = w.split('：')[1]
        elif re.search('电话', w):
            phone = w.split('：')[1]
        elif re.search('邮箱', w):
            email = w.split('：')[1]
        elif re.search('求职状态', w):
            job_status = text1[text1.index(w)+1]
        elif re.search('期望地点', w):
            job_addr = text1[text1.index(w)+1]
        elif re.search('工作性质', w):
            job_exp = text1[text1.index(w)+1]
        elif re.search('期望行业', w):
            job_ind = text1[text1.index(w)+1]
        elif re.search('期望薪资', w):
            job_salary = text1[text1.index(w)+1]
            #edu = ''.join(text1[text1.index(w)+2])

    print(33, name)
    print(34, job_p)
    print(35, sex)
    print(36, age)
    print(37, birthday)
    print(38, academic)
    print(39, nation)
    print(40, politics)
    print(41, exper)
    print(42, addr)
    print(43, census)
    print(44, phone)
    print(45, email)
    print(46, job_status)
    print(47, job_addr)
    print(48, job_exp)
    print(49, job_ind)
    print(50, job_salary)
    print(51, edu)
    sql = "insert into t_excel (name,sex,marry,academic,job_exp,exper,age,census,job_addr,job_p,job_salary,job_ind,job_status,addr,birthday,email,phone,edu,politics,nation) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql,[name, sex, marry, academic, job_exp, exper, age, census, job_addr, job_p, job_salary, job_ind,job_status, addr, birthday, email, phone, edu, politics, nation])
    conn.commit()





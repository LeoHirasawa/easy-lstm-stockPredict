#coding:utf-8
import pymysql as mdb
def sample():
    con = None
        #连接mysql的方法：connect(host='localhost',user='root',passwd='root',db='test',port=3306)
    con = mdb.connect('202.118.228.197', 'ntlab607','1518sudu', 'stock_analyze')
        #所有的查询，都在连接con的一个模块cursor上面运行的
    with con:
        cur = con.cursor(mdb.cursors.DictCursor)
        #执行一个查询
        cur.execute("SELECT yesterday_open, date FROM stock_quotations_601857 WHERE time like '15:00%'")
        rows=cur.fetchall()
        # for row in rows:
        #     print '%s %s' %(row['date'],row['yesterday_open'])
    print(rows)
    s=[]
    s_date = []
    for row in rows:
        s.append(row['yesterday_open'])
        s_date.append(row['date'])
    allsamplex=[]
    allsampley= []
    for index, row in enumerate(s):
        try:
            xsample = []

            xsample=s[index:index+10]
            allsamplex.append(xsample)
            allsampley.append([s[index+10]])
            # print 'ssss'
            # print onesample

        except Exception as e:
            print(e)
            break

    s_date = s_date[:len(allsampley)]
    return allsamplex[1:],allsampley,s_date

sample()
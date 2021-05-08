from pymysql import *
def main():
    # 建立資料庫連結
    conn = connect(host='localhost', port=3306, database='api',user='root',password='123456', charset='utf8')
    # 取得Cursor物件
    cursor1 = conn.cursor()
    # 新增一筆資料
    count = cursor1.execute('insert into users(name) values("Joe")')
    #顯示影響的行數
    print(count)
    count = cursor1.execute('insert into users(name) values("Mary")')
    print(count)
# # 更新
    count = cursor1.execute('update users set name="Joe1" where name="Joe"')
    # # 刪除
    count = cursor1.execute('delete from users where id=2')

    # 進行資料提交
    conn.commit()

    # 關閉Cursor物件
    cursor1.close()
    # 關閉Connection物件
    conn.close()
if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
from stats.sql.model.testModel import Post

DB_config = {
    'user':'root',
    'password':'tt43uu22',
    'host':'127.0.0.1',
    'database':'MLBSTATS',
    'raise_on_warnings': True
}
DB_NAME = 'MLBSTATS'


def create_db(cnx, cursor):
    print('create_db_exec function exec')
    # try:
    #     cursor.execute(
    #         "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME)
    #     )
    # except mysql.connector.Error as err:
    #     print("Failed creating database: {}".format(err))
    #     cnx.close()
    #     exit(1)


def transformListData(tupleData):
    post_data = {}
    post_data['id'] = tupleData[0]
    post_data['title'] = tupleData[1]
    post_data['text'] = tupleData[2]
    post_data['created_date'] = tupleData[3]
    post_data['published_date'] = tupleData[4]
    post_data['author_id'] = tupleData[5]
    return post_data

def query_with_fetchall(cnx, cursor):
    # fetchone -> strike/NewProducts/views.py
    # fetchall -> strike/strike3/views.py
    # strike/strike3/views.py

    cursor.execute("SELECT * FROM stats_post")
    selectedList = []
    rows = cursor.fetchall()
    # 방법1
    # for row in rows:
    #     # print 'row is : ', type(row) --> tuple
    #     selectedList.append(transformListData(row))

    # 방법2
    # for idx, row in enumerate(rows):
    for row in rows:
        post_data = {}
        post_data['id'] = row[0]
        post_data['title'] = row[1]
        post_data['text'] = row[2]
        post_data['created_date'] = row[3]
        post_data['published_date'] = row[4]
        post_data['author_id'] = row[5]
        selectedList.append(post_data)

    return selectedList
    cursor.close()
    cnx.close()

def post_select_test(cnx, cursor):
    test = Post.objects.all()
    # print type(test) --> <class 'django.db.models.query.QuerySet'>
    return Post.objects.all()
    cursor.close()
    cnx.close()

def DB_connect(func=None) :
    try:
        cnx = mysql.connector.connect(**DB_config)
        cursor = cnx.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        # print ("cnx : " , cnx) --> ('cnx : ', <mysql.connector.connection.MySQLConnection object at 0x10a79a6d0>)
        # print ("cursor : " , cursor) --> ('cursor : ', <mysql.connector.cursor.MySQLCursor object at 0x10a79a990>)

        # if ( func != None and callable(func) ) :
        if ( func is not None and callable(eval(func)) ):
            resultList = eval(func)(cnx, cursor)

            # for item in enumerate(resultList) :
            #     print item

            return resultList
        else :
            print 'just close'
            cnx.close()





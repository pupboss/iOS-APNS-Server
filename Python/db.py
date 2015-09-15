#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

def getNewestToken():

        connection = MySQLdb.connect(user="userName", passwd="pwd", db="yourDBName")
        cursor = connection.cursor()
        sql = "select deviceToken from user_token"
        n = cursor.execute(sql)
        rows = cursor.fetchall()
        array = []
        for n in rows:
            array.append(n[0])

        cursor.close()
        connection.commit()
        connection.close()

        nop_array = []
        for token in array:
                if token in nop_array:
                        pass
                else:
                        nop_array.append(token)

        return nop_array
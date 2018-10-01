#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import pymysql

import config
from schema.db import PassDB

dbconn = PassDB(config.mysql)


def purify(s):
    return s.decode('utf8', 'ignore')


def init():
    dbconn.cleardb()
    addCSDN()
    addYahoo()


def recordError(path, datas):
    with open(path, 'ab') as fh:
        for data in datas:
            fh.write(":".join(data) + '\n')


def addCSDN(batchSize=1000):
    count = 0
    csdn = open(config.csdn, 'rb')
    temp = []
    for line in csdn:
        data = line.strip().split(" # ")
        if len(data) != 3:
            continue
        temp.append(data)
        if len(temp) >= batchSize:
            try:
                dbconn.insertCSDN(temp)
            except pymysql.err.InternalError as e:
                recordError(config.csdnTodo, temp)
            except Exception as e:
                print(e)
                recordError(config.csdnTodo, temp)
            finally:
                temp = []
                count += batchSize
                print count, "\r",
    csdn.close()


def addYahoo(batchSize=1000):
    count = 0
    yahoo = open(config.yahoo, 'rb')
    temp = []
    for line in yahoo:
        data = line.strip().split(":", 2)[1:]
        if len(data) != 2:
            continue
        temp.append(data)
        if len(temp) >= batchSize:
            try:
                dbconn.insertYahoo(temp)
            except pymysql.err.InternalError as e:
                recordError(config.csdnTodo, temp)
            except Exception as e:
                print(e)
                recordError(config.csdnTodo, temp)
            finally:
                temp = []
                count += batchSize
                print count, "\r",


def main():
    if sys.argv[1] == 'init':
        init()


if __name__ == '__main__':
    main()

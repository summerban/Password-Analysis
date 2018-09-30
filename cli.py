#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pymysql
import config
from schema.db import PassDB

dbconn = PassDB(config.mysql)


def init():
    dbconn.cleardb()
    count = 0
    batchSize = 1000

    with open(config.csdn, 'rb') as fh:
        temp = []
        for line in fh:
            temp.append(line.strip().split(" # "))
            if len(temp) > batchSize:
                dbconn.insertCSDN(temp)
                temp = []
                count += batchSize
                print count, "\r",

    with open(config.yahoo, 'rb') as fh:
        temp = []
        for line in fh:
            data = line.strip().split(":", 2)[1:]
            if len(data) != 2:
                continue
            temp.append(data)
            if len(temp) >= batchSize:
                try:
                    dbconn.insertYahoo(temp)
                except pymysql.err.InternalError as e:
                    pass
                except Exception as e:
                    print(e)
                    print(temp)
                temp = []
                count += batchSize
                print count, "\r",


def main():
    if sys.argv[1] == 'init':
        init()


if __name__ == '__main__':
    main()

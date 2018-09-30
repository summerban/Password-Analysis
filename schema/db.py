#!/usr/bin/env python
# -*- coding: utf-8 -*-

from schema.dbbase import DB


class PassDB(DB):

    def insertCSDN(self, lines):
        sql = "INSERT INTO `info` (`username`, `password`, `email`) VALUES (%s, %s, %s)"
        self.insert(sql, data=lines, multip=True)

    def insertYahoo(self, lines):
        sql = "INSERT INTO `info` (`username`, `password`) VALUES (%s, %s)"
        self.insert(sql, data=lines, multip=True)

    def cleardb(self):
        self.execute('DELETE FROM `info`')
        self.conn.commit()

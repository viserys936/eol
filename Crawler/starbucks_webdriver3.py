# -*- coding:utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import sqlite3

con = sqlite3.connect("starbucks.db") 

list1 = ['14', '11', '1', '4', '2', '21', '23', '7', '15', '3', '12',
       '9', '26', '24', '13', '16', '20', '17', '5', '19', '25',
       '10', '22', '29']
c = webdriver.Firefox()
c.get('http://www.starbucks.com.tw/stores/storesearch/stores_storesearch.jspx')
input1 = Select(c.find_element_by_id("selCity"))
input2 = Select(c.find_element_by_id("selRegion"))
input3 = c.find_elements_by_id("byRegion")
input4 = c.find_elements_by_id("sbForm:btnByRegion")
input3[0].click()

with con:
    cur = con.cursor()
##    cur.execute('''CREATE TABLE IF NOT EXISTS branch(
##                    name TEXT,
##                    address TEXT,
##                    phone TEXT,
##                    time TEXT
##                    )''')
    for location in list1:
        input1.select_by_value(location)
        input4[0].click()
        time.sleep(8)
        input5 = c.find_elements_by_id('searchstore1')
        for i in input5:
            s = i.text.split('\n')
            name = s[0][3:]
            address = s[1][5:]
            phone = s[2][5:]
            time_open = s[3][5:]
            sql = "INSERT INTO branch (name,address,phone,time) VALUES (?,?,?,?)"
            cur.execute(sql, [name, address, phone, time_open])
        con.commit()
con.close()

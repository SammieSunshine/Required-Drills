#
#
# Assignment 164(revision for required drills)
#
#
# Python ver. 3.8.5
#
# Author: Samantha Bilips
#
#
# Purpose: Use sqlite3 module reate database with a table of files with a ".txt" extension


import sqlite3
#creates db; connects to and holds connection
conn = sqlite3.connect('164_redo.db')

# Table with autoincremented primary key
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS table_Files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        fname TEXT)')
    conn.commit()#won't work if not commited
conn.close()#close connecton


import sqlite3

conn = sqlite3.connect('164_redo.db')
#insert .txt files into table

with conn:
    fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt', 'data.pdf' ,'myPhoto.jpg')
    cur = conn.cursor()
    cur.execute("fileList")
 
    for files in fileList:
        if files.endswith(".txt"):
            cur.execute("INSERT INTO table_Files VALUES(?,?)")
            cur.execute("SELECT fname FROM tbl_Files")#view corrected table with .txt files
    conn.commit()
conn.close()



    

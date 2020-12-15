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
conn = sqlite3.connect('185_redo.db')

# Table with autoincremented primary key
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS table_Files1(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        fname TEXT)')
    conn.commit()#won't work if not commited
conn.close()#close connecton


import sqlite3

conn = sqlite3.connect('185_redo.db')
#insert .txt files into table

with conn:
    fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt', 'data.pdf' ,'myPhoto.jpg')
    cur = conn.cursor()
 
    for files in fileList:
        if files.endswith(".txt"):
            cur.execute("INSERT INTO table_Files1 (fname)VALUES(?)",(files,))
    conn.commit()
conn.close()


import sqlite3

conn = sqlite3.connect('185_redo.db')

cur = conn.cursor()
with conn:
    cur.execute("SELECT fname FROM tbl_Files1")#view corrected table with .txt files
    results = cur.fetchall()
    print(results)
    conn.commit()
conn.close()




    

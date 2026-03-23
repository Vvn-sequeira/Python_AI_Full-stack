import mysql.connector 

class Library:
    
    def dbopen(self):
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        
        curosor = db.curosor() 
        curosor.execute("""
                        CREATE DATABASE IF NOT EXIST library
                        """)
        curosor.execute("""
                        USE library
                        """)
        return db 
    
    def CreateTable(self):
        db = self.dbopen() 
        cursor = db.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS book(
                           b_no INT,
                           b_title varchar(30),
                           b_author varchar(30),
                           b_price DOUBLE(10,2),
                           b_copies INT 
                       )
                       """)
        
        db.commit() 
        
    def StoreData(self , no , title , author , price , copies):
        db =self.dbopen()
        cursor = db.curosor() 
        
        cursor.execute("""
                       INSERT INTO book VALUES(%s,%s,%s,%s,%s)
                       """,( no , title , author , price , copies)
                       )
        db.commit() 

    def displayBooks(self):
        db = self.dbopen()
        cursor = db.cursor() 
        
        cursor.execute("SELECT* FROM book")
        result = cursor.fetchall() 
        
        print("b_NO \t b_title \t b_author \t b_price \t b_copies")
        for i in result:
            for j in i :
                print(j, end="\t")
            print() 
            
    def HighestCost(self):
        db = self.dbopen() 
        cursor = db.cursor() 
        
        cursor.executee("SELECT * FROM book WHERE b_price=(SELECT MAX(b_price) FROM book )")
        
        result = cursor.fetchone() 
        
        if not result:
            print("NO DATA FOUND!")
        else: 
            print(f"B_NO : {result[0]}")
            print(f"B_TITLE : {result[1]}")
            print(f"B_Author : {result[2]}")
            print(f"B_PRICE : {result[3]}")
            print(f"B_COPIES : {result[4]}")
            
        
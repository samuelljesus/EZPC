import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-QVVCDDV\SQLEXPRESS;'
                      'Database=EZPC;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

name = "Book - A"
price = 125
    
insert_records = '''INSERT INTO Books(Name, Price) VALUES(?,?) ''' 
cursor.execute(insert_records, name, price)
conn.commit()
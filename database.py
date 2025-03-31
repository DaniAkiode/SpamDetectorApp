import sqlite3 # import sqlite module 

def create_table(): #This function will create table 
    conn = sqlite3.connect("spam_results.db") # Create/connects table 
    cursor = conn.cursor() #turns database into an object 

    cursor.execute('''CREATE TABLE IF NOT EXISTS results (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        message TEXT, 
                        prediction TEXT,
                        timestamp DATATIME DEFAULT CURRENT_TIMESTAMP)''') #run sql commands 
    conn.commit() #save changes in database 
    conn.close() #close connection 


def insert_result(message, prediction): # This function collects the results from users 
    conn = sqlite3.connect("spam_results.db") #connect table  
    cursor = conn.cursor() # turn table into an executable object 

    # Insert data into the table 

    cursor.execute("INSERT INTO results (message, prediction) VALUES (?, ?)", (message, prediction))

    
    conn.commit() #save changes in database 
    conn.close() #save changes in database 

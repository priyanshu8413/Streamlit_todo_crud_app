import sqlite3

# Function to create a new database connection
def create_connection():
    return sqlite3.connect("data.db")


#Database
#table
#field/column
#datatype

def create_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS tasktable(task TEXT, task_status TEXT, due_date DATE)')
    conn.commit()
    conn.close()
def add_data(task, task_status, task_due_date):
    conn = create_connection()
    c = conn.cursor()
    c.execute('INSERT INTO tasktable(task, task_status, due_date) VALUES (?, ?, ?)', (task, task_status, task_due_date))
    conn.commit()
    conn.close()

def view_all_data():
    conn=create_connection()
    c=conn.cursor()
    c.execute('SELECT * FROM tasktable')
    data=c.fetchall()
    return data

def view_unique_task():
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT DISTINCT task FROM tasktable')
    data = c.fetchall()
    return data
def get_task(task):
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM tasktable WHERE task="{}"'.format(task))
    #c.execute('SELECT * FROM tasktable WHERE task=?',task)
    data = c.fetchall()
    return data
def edit_task_data(new_task,new_task_status,new_task_date,task,task_status,task_due_date):
    conn = create_connection()
    c = conn.cursor()
    c.execute("UPDATE tasktable SET task=?,task_status=?,due_date=? WHERE task=? and task_status=? and due_date=? ",(new_task,new_task_status,new_task_date,task,task_status,task_due_date))
    conn.commit()
    #conn.close()
    data = c.fetchall()
    return data

def delete_data(task):
    conn = create_connection()
    c = conn.cursor()
    c.execute('DELETE FROM tasktable WHERE task=?',(task,))
    conn.commit()
    conn.close()





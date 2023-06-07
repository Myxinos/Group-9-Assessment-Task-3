from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import sqlite3 
from sqlite3 import Error
 
app = Flask(__name__) 
 
# Here I create a DB and a connection
def create_connection(db_file):
    connection = None;
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
     
    return conn 
 
# This is were I call the function for my db
 
create_connection("Create.Event.db") 
 
# This is were I create the tables I want in the database 
 
def create_table(conn, events):
    sql = """ INSERT INTO events(Event_ID, Event_Image, Event_Name, 
                        Event_Organizer, Category, 
                        Musician, Tags, Event_Date, Start_Time, 
                        End_Time, Timezone, 
                        Event_Language, Venue_Location)""" 
 
    c = conn.cursor()
    c.execute(sql,events)
    return cur.lastrowid
 
 
# here I insert the created tables
def main():
    database = r"CreateEvent.db" 
    sql_create_event_table = """ CREATE TABLE IF NOT EXISTS events (
		                                Event_ID AUTO_INCREMENT INTEGER NOT NULL,
	                                    Event_Name TEXT NOT NULL,
	                                    Event_Image NTEXT DEFAULT0,
	                                    Event_Organizer TEXT NOT NULL,
	                                    Category TEXT NOT NULL,
	                                    Musician TEXT NOT NULL,
	                                    Tags TEXT NOT NULL,
	                                    Event_Date INTEGER NOT NULL,
	                                    Start_Time INTEGER NOT NULL,
	                                    End_Time INTEGER NOT NULL,
	                                    Timezone TEXT NOT NULL,
	                                    Event_Language TEXT NOT NULL,
	                                    Venue_Location TEXT NOT NULL,
                                        PRIMARY KEY (Event_ID)
                                    ); """
    
 
 
    conn = create_connection(database)
 
    if conn is not None:
        # event table
        create_table(conn, sql_create_event_table)
 
    else:
        print("Error! cannot create the database connection.")
 
 
 
# index for the html page
@app.route('/')
def index():
    return render_template("index.html")
 
 
# sending input form form to db
@app.route('/my_form', methods=['POST'])
def my_form():
 
    if request.method == 'POST':
        c = conn.cursor()
        Event_Name = request.form.get('Event Name:')
        Event_Image = request.form.get('Event Image:')
        Event_Organizer = request.form.get('Event Organizer:')
        Category = request.form.get('Category:')
        Muscician = request.form.get('Muscician:')
        Tags = request.form.get('Tags:')
        Event_Date = request.form.get('Event Date:')
        Start_Time = request.form.get('Start Time:')
        End_Time = request.form.get('End Time:')
        Event_language = request.form.get('Event Language:')
        Venue_Location = request.form.get('Venue_Location:')
        
        try:
            sql = ("INSERT INTO databasename.tablename (columnName,columnName,columnName,columnName Ci) VALUES (%s, %s, %s, %s)")
            c.execute(sql,(Event_Name, Event_Image, Event_Organizer,  Category, Muscician,
                    Tags, Event_Date, Start_Time, End_Time, Event_language, Venue_Location))
            connection.commit() 
            #or "conn.commit()" (one of the two)
            return redirect('/')
        except:
            return 'Something went wrong when creating your event. Please try again.'
 
# This is where I run the app 
if __name__ == '__main__':
    app.run(debug=True)
 
     

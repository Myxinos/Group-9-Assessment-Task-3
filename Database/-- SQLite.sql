-- SQLite

CREATE TABLE IF NOT EXISTS events (
	
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
);

INSERT INTO events (Event_ID, Event_Image, Event_Name, Event_Organizer, Category, 
Musician, Tags, Event_Date, Start_Time, End_Time, Timezone, 
Event_Language, Venue_Location)

Values ('1', '"C:\Users\liamg\Downloads\Sqancho Brothers.webp"','The Squancho Brothers Live', 'Squingly Co.', 'Rock', 
'The Squancho Brothers', 'Rock & Roll', '13:10:2023', '16:30', 
'18:30', 'AEST', 'English', 'Brisbane Powerhouse');

SELECT * FROM events;

DELETE FROM events WHERE Event_ID=''; 

DROP TABLE events;
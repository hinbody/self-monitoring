import sqlite3

create_table = """CREATE TABLE IF NOT EXISTS feelings(
                  ID INT PRIMARY KEY NOT NULL,
                  date_time TEXT,
                  situation TEXT,
                  thoughts TEXT,
                  thought_intensity INT,
                  emotions TEXT,
                  emotions_intensity INT, 
                  physical_senstations TEXT,
                  phy_sense_intensity INT)
"""
connect = sqlite3.connect('feelings.db')
cursor = connect.cursor()
cursor.execute(create_table)

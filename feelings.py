import sqlite3
import datetime

create_table = """CREATE TABLE IF NOT EXISTS feelings(
                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  date_time TEXT,
                  situation TEXT,
                  thoughts TEXT,
                  thought_intensity INT,
                  emotions TEXT,
                  emotions_intensity INT, 
                  physical_sensations TEXT,
                  phy_sense_intensity INT)
"""
connect = sqlite3.connect('feelings.db')
cursor = connect.cursor()
cursor.execute(create_table)

#def log_feelings(situation, thoughts, ti, emotions, ei, pyhs_sensations, pi):
def log_feelings(entry):
  if len(entry) == 7 and type(entry) is list:
    time = datetime.datetime.now().isoformat()
    entry.append(time)
    cursor.execute("""INSERT INTO feelings(
                      situation, thoughts, thought_intensity, emotions,
                      emotions_intensity, physical_sensations, phy_sense_intensity,
                      date_time) VALUES (?,?,?,?,?,?,?,?)""", entry)
    connect.commit()
  else:
    print('the list must contain 7 items')
connect.commit()

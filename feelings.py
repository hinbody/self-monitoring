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

def log_feelings(entry):
  """Inserts a log of feelings into the database.
  
  Accepts 7 item list, then adds it plus the current time to the database
  """
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

def get_intense():
  """Get intense emotions.

  Gets entries with an emotion_intensity of 7 or more.
  **NOTE** 7 is an arbitrary number I chose. It means nothing.
  """
  f = cursor.execute("""SELECT * FROM feelings WHERE emotions_intensity >= 7""")
  return f.fetchall()

def get_emotions():
  """ Get list and count of all emotions."""

  f = cursor.execute("""SELECT emotions FROM feelings""")
  emo = {}

  for row in f:
    for e in row:
      emo[e] = emo.get(e, 1)
  return emo

connect.commit()

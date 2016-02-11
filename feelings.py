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

def get_entries_for_emotion(emo):
  """Get all entries for a particular emotion.
  
  Returns a list of all entries containg the emotion represented by emo
  """

  e = cursor.execute("SELECT * FROM feelings WHERE emotions=?", (emo,))
  return e.fetchall()

def avg_emo_intensity():
  """Get average intensity for each emotion."""

  emotions = []
  emotions_avg = {}
  emos = cursor.execute("SELECT emotions FROM feelings")
  for e in emos:
    if e[0] in emotions:
      print('')
    else:
      emotions.append(e[0])

  for e in emotions:
    print('emotion:', e)
    count = 0
    emos_intense = cursor.execute("""SELECT emotions, emotions_intensity FROM
    feelings WHERE emotions = ?""", (e,))# ('emotions', e))
    emotions_avg[e] = 0
    for emo in emos_intense:
      count = count + 1
      print(e, 'intensity:', emo[1])
      emotions_avg[e] = emotions_avg[e] + emo[1]
      avg = emotions_avg[e]  / count
      print(e,'average',avg)


#  for e in emotions:
#    print(e, 'is type:', type(e))

connect.commit()

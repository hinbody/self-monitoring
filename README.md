# Thoughts and Feelings Self-monitoring form

## Summary
This module contains functions to get input from the user about their
uncomfortable thoughts and feelings as discussed in  
http://ptsd.about.com/od/selfhelp/ht/selfmonitor.htm and store them in an SQLite
database

## DISCLAIMER
I am neither a doctor nor medical professional. This is based off of an
interesting article that I found, and is being created for the sole purpose of
my programming education.

### *IMPORTANT*
If you feel that you have PTSD or any other mental illness, please see a doctor
or other medical professional that can give you the help you may need. 

## Functions
log_feelings() accepts a 7 item list and stores it in an sqlite3 database

## Data
The data that will be received and stored into the database:
- date and time
- situation that caused or brought forward the uncomfortable thoughts or feelings
- thoughts you are having about the situation
  - intensity of thoughts
- emotions you are feeling
  - intensity of feelings
- physical sensations you are experiencing
  - intensity of physical sensations

## Data analysis
As data is entered, it is stored in the database. There will be a function to
pull this data from the db and identify patterns from the data

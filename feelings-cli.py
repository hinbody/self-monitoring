#!/usr/bin/env python3
# This is a cli front end to the feelings.py backend
# feelings data can be passed in as arguments when calling this script, and if
# they do not exist, the script will prompt for the appropriate information
import feelings
import sys

f = []

#if len(sys.argv) == 8:
#  for r in range(1,9):
#    if r == 3:# or r == 5 or r ==7:
#      f.append(int(sys.argv[r]))
#    else:
#      f.append(sys.argv[r])

f.append(input('Describe the situation: '))
f.append(input('Enter any thoughts you have: '))
f.append(int(input('Rate the intensity of these thoughts from 0-9: ')))
f.append(input('List the emotions you\'re feeling: '))
f.append(int(input('Rate the intensity of these emotions from 0-9: ')))
f.append(input('List any physical sensations you feel: '))
f.append(int(input('Rate the intensity of these sensations from 0-9: ')))

#for s in f:
#  print(s, 'is type:', type(s))
feelings.log_feelings(f)

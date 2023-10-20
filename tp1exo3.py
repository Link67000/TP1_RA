#!/usr/bin/python3.6

jour = input()
heure = input()
minute = input()
jour = int(jour)
heure = int(heure)
minute = int(minute)
print("minute = {})".format((jour*24*60)+(heure*60)+minute))


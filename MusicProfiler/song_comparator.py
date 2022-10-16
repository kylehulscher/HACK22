import os
import sys
import glob
import time
import datetime
import sqlite3

class song:
	name = None        #song name
	tid = None 		   #track id
	term = None        #genre
	tempo = None       #tempo
	duration = None    #song length
	hotttnesss = None  #hotness?
	year = None        #release year
	artistId = None    #artist id
	artistName = None  #artist name

	def __init__(self, name, tid, term, tempo, duration, hotttnesss, year, artistId, artistName):
		self.name = name
		self.tid = tid
		self.term = term
		self.tempo = tempo
		self.duration = duration
		self.hotttnesss = hotttnesss
		self.year = year
		self.artistId = artistId
		self.artistName = artistName

	def __str__(self):
		return "{}({},{},{},{},{},{},{},{})".format(name, tid, term, tempo, duration, hotttnesss, year, artistId, artistName)

def compareSongs(tid1, tid2):

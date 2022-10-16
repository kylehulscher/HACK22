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


#term x5: genre is same(+1), same parent genre/category (+variable amount)
#tempo x3: - 0.03 for every point of abs difference
#duration x1: - 0.15 for a difference of 20s
#hotttnesss x3: 1 - (max hotttnesss value - min hotttness value)
#year x1: 1 - (max year - min year) *0.01
#artistId x2: if artists are similar 1 otherwise 0
def compareSongs(tid1, tid2):
	song1 = song.
	totalSum = 0
	if 

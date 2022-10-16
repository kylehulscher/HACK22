import os
import sys
import glob
import time
import datetime
import sqlite3
import output_similar

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
	song1 = song(0, 0, 0, 0, 0, 0, 0, 0, 0)
	song2 = song(0, 0, 0, 0, 0, 0, 0, 0, 0)
	totalSum = 0
	year = 0
	term = 0
	tempo = 0
	duration = 0
	hotttnesss = 0
	artistSimilarity =0

	#year
	year = 1 - 0.01(abs(tid1.year-tid2.year))
	#term
	if tid1.term == tid2.term:
		term = 1
	#tempo
	tempo = -0.03(abs(tid1.tempo - tid2.tempo))
	#duration
	duration = -0.15(abs(tid1.duration-tid2.duration))
	#hotttnesss 
	hotttnesss = 1 - (abs(tid1.hotttnesss-tid2.hotttnesss))

	#artist same or similar
	if tid1.artistId == tid2.artistId:
		artistSimilarity = 1

	else:	
		a1Sim = output_similar.compare(1, song1.artistId, 1)
		a2Sim = output_similar.compare(1, song2.artistId, 1)
		for entry in a1Sim:
			if entry[0] == tid2.artistId:
				artistSimilarity = 0.75
		for entry in a2Sim:
			if entry[0] == tid1.artistId:
				artistSimilarity = min(artistSimilarity + 0.75, 1)

	totalSum = (year + term + tempo + duration + hotttnesss + artistSimilarity) / 15




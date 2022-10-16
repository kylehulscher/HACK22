import os
from os.path import exists
import sys
import glob
import time
import datetime
import sqlite3
import getopt
import output_similar

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
	numIns = {"similarArtistById" : 2,
				"aid" : 2,
				"similarArtistByName" : 2,
				"abn" : 2,
				"compareSongById" : 3,
				"sid" : 3,
				"compareSongByName" : 3,
				"sbn" : 3,
				"getPlaylistWId" : 2,
				"pid" : 2,
				"getPlaylistWName" : 2,
				"pbn" : 2,
				"userTopSongs" : 2,
				"uts" : 2}
	print("Type 'help' for more info")
	while True:
		userCMD = input(bcolors.OKGREEN + "Osusu >> " + bcolors.ENDC)
		if(userCMD == 'help' or userCMD =='Help' or userCMD == 'h'):
			print("Commands:")
			print("\tsimilarArtistById(aid)   artistId")
			print("\tsimilarArtistByName(abn) artistName")
			print("\tcompareSongById(sid)     songId1    songId2")
			print("\tcompareSongByName(sbn)   songName1  songName2")
			print("\tgetPlaylistWId(pid)      songId")
			print("\tgetPlaylistWName(pbn)    songName")
			print("\tuserTopSongs(uts)        userName")
			print("\tquit(q)/exit")
			print()

		elif(userCMD == 'exit' or userCMD == 'quit' or userCMD == 'q'):
			sys.exit(0)
		else:
			cmdList = userCMD.split(" ")
			if len(cmdList) > 0 and cmdList[0] in numIns and numIns.get(cmdList[0]) > len(cmdList):
				print("Not enough inputs")
				print()
			elif cmdList[0] == "similarArtistById" or cmdList[0] == "aid":
				output_similar.compare(1, "%" + cmdList[1] + "%")
				print()
			elif cmdList[0] == "similarArtistByName" or cmdList[0] == "abn":
				output_similar.compare(0, "%" + cmdList[1] + "%")
				print()
			elif cmdList[0] == "compareSongById" or cmdList[0] == "sid":
				print(cmdList)
				print()
			elif cmdList[0] == "compareSongByName" or cmdList[0] == "sbn":
				print(cmdList)
				print()
			elif cmdList[0] == "getPlaylistWId" or cmdList[0] == "pid":
				print(cmdList)
				print()
			elif cmdList[0] == "getPlaylistWName" or cmdList[0] == "pbn":
				print(cmdList)
				print()
			elif cmdList[0] == "userTopSongs" or cmdList[0] == "uts":
				print(cmdList)
				print()
			else:
				print("Invalid input, please see 'help'")
				print()
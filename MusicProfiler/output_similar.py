import os
import sys
import glob
import time
import datetime
import sqlite3
import getopt

def die_with_usage():
	""" HELP MENU """
	print('output_similar.py')
	print('usage:')
	print('  python list_all_artists.py <DATASET DIR> output.txt')
	print('')
	print('This code lets you list all artists contained in all')
	print('subdirectories of a given directory.')
	print('This script puts the result in a text file, but its main')
	print('function can be used by other codes.')
	print('The txt file format is: (we use <SEP> as separator symbol):')
	print('artist Echo Nest ID<SEP>artist Musicbrainz ID<SEP>one track Echo Nest ID<SEP>artist name')
	sys.exit(0)

def compare(inType, inId):
	# go!
	t1 = time.time()
	dArtists = list_all(maindir)
	t2 = time.time()
	stimelength = str(datetime.timedelta(seconds=t2-t1))


	prof_exists = exists("profiler.db")
	sim_exists = exists("artist_similarity.db")
	if (prof_exists and sim_exists):
		con_prof = sqlite3.connect("profiler.db")
		cur_prof = con_prof.cursor()

		con_sim = sqlite3.connect("artist_similarity.db")
		cur_sim = con_sim.cursor()

		res_prof = cur_prof.execute("SELECT name FROM sqlite_master WHERE name='artists'")
		res_sim = cur_sim.execute("SELECT name FROM sqlite_master WHERE name='similarity'")
		if res_prof.fetchone() is None:
			print('Table "artists" does not exist')
			sys.exit(0)
		if res_sim.fetchone() is None:
			print('Table "similarity" does not exist')
			sys.exit(0)
		for aid in dArtists.keys():
			cur.execute("INSERT INTO artists VALUES(?, ?, ?)", (aid, dArtists[aid][0], dArtists[aid][1]))
			con.commit()



def main(argv):
	inType = -1
	inId = ""
	try:
		opts, args = getopt.getopt(argv,"hn:i:",["iName=","iId="])
	except getopt.GetoptError:
		print('output_similar.py -n <iName>/-i <iId>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('output_similar.py -n <iName>/-i <iId>')
			sys.exit()
		elif opt in ("-n", "--iName"):
			inType = 0
			inId = arg
		elif opt in ("-i", "--iId"):
			inType = 1
			inId = arg

	compare(inType, inId)

if __name__ == '__main__':
	pythonsrc = os.path.join(sys.argv[0],'../PythonSrc')
	print(pythonsrc)
	pythonsrc = os.path.abspath( pythonsrc )
	sys.path.append( pythonsrc )
	import normalizer

	print(normalize_artist("ÄI-TIEM"))
	#main(sys.argv[1:])
	
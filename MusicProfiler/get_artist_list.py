import os
import sys
import glob
import time
import datetime
import sqlite3

def get_artist_ids(trackfile):
	"""
	Utility function, opens a h5 file, gets the 4 following fields:
	 - artist Echo Nest ID
	 - artist Musicbrainz ID
	 - artist name
	It is returns as a triple (,,)
	Assumes one song per file only!
	"""
	h5 = hdf5_utils.open_h5_file_read(trackfile)
	aid = GETTERS.get_artist_id(h5)
	ambid = GETTERS.get_artist_mbid(h5)
	aname = GETTERS.get_artist_name(h5)
	h5.close()
	return aid,ambid,aname

def list_all(maindir):
	"""
	Goes through all subdirectories, open every song file,
	and list all artists it finds.
	It returns a dictionary of string -> tuples:
	   artistID -> (musicbrainz ID, trackID, artist_name)
	The track ID is random, i.e. the first one we find for that
	artist. The artist information should be the same in all track
	files from that artist.
	We assume one song per file, if not, must be modified to take
	into account the number of songs in each file.
	INPUT
	  maindir  - top directory of the dataset, we will parse all
				 subdirectories for .h5 files
	RETURN
	  dictionary that maps artist ID to tuple (MBID, track ID, artist name)
	"""
	results = {}
	numfiles = 0
	# iterate over all files in all subdirectories
	for root, dirs, files in os.walk(maindir):
		# keep the .h5 files
		files = glob.glob(os.path.join(root,'*.h5'))
		for f in files :
			numfiles +=1
			# get the info we want
			aid,ambid,aname = get_artist_ids(f)
			assert aid != '','null artist id in track file: '+f
			# check if we know that artist
			if aid in list(results.keys()):
				continue
			# we add to the results dictionary
			results[aid] = (ambid,aname)
	# done
	return results

def die_with_usage():
	""" HELP MENU """
	print('list_all_artists.py')
	print('   by T. Bertin-Mahieux (2010) Columbia University')
	print('')
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

if __name__ == '__main__':
	# help menu
	if len(sys.argv) < 3:
		die_with_usage()

	pythonsrc = os.path.join(sys.argv[0],'../PythonSrc')
	print(pythonsrc)
	pythonsrc = os.path.abspath( pythonsrc )
	sys.path.append( pythonsrc )
	import hdf5_utils
	import hdf5_getters as GETTERS

	# params
	maindir = sys.argv[1]
	output = sys.argv[2]

	# sanity checks
	if not os.path.isdir(maindir):
		print(maindir,'is not a directory')
		sys.exit(0)
	if os.path.isfile(output):
		print('output file:',output,'exists, please delete or choose new one')
		sys.exit(0)

	# go!
	t1 = time.time()
	dArtists = list_all(maindir)
	t2 = time.time()
	stimelength = str(datetime.timedelta(seconds=t2-t1))

	con = sqlite3.connect("profiler.db")
	cur = con.cursor()
	res = cur.execute("SELECT name FROM sqlite_master WHERE name='artists'")
	if res.fetchone() is None:
		cur.execute("CREATE TABLE artists(aid TEXT, ambid TEXT, aname TEXT)")
	for aid in dArtists.keys():
		print("{}: {}, {}".format(aid.decode("utf-8"),dArtists[aid][0].decode("utf-8"),dArtists[aid][1].decode("utf-8")))
		cur.execute("INSERT INTO artists VALUES(?, ?, ?)", (str(aid.decode("utf-8")), str(dArtists[aid][0].decode("utf-8")), str(dArtists[aid][1].decode("utf-8"))))
		con.commit()

	print('number of artists found:', len(dArtists),'in',stimelength)
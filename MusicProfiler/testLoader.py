import h5py
import numpy as np

# open the file as 'f'
with h5py.File('TRAMMTK128F4279CD2.h5', 'r') as f:
	Datasetnames=f.keys()
	print(Datasetnames)
	
	analysisData=f['analysis']
	metaData=f['metadata']
	musicbrainz=f['musicbrainz']
	
	print("analysis:")
	for item in analysisData:
		print(item)
	print("\n")
	
	print("metadata:")
	for item in metaData:
		print(item)
	print("\n")
	
	print("musicbrainz:")
	for item in musicbrainz:
		print(item)
	print("\n")
	
	print("musicbrainz songs:")
	print(musicbrainz['songs'])
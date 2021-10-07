import os
import csv

TRACK_METADATA_PATH = '../../Datasets/fma_metadata/tracks_new.csv'
GENRE_METADATA_PATH = '../../Datasets/fma_metadata/genres.csv'
TRACK_ID_COLUMN = 0
TRACK_GENRE_COLUMN = 42
GENRE_ID_COLUMN = 0
GENRE_NAME_COLUMN = 3

genres = {}

genre_file = open(GENRE_METADATA_PATH, newline='', encoding='utf-8')
reader = csv.reader(genre_file)

header = next(reader)
for row in reader:
    genres[row[GENRE_ID_COLUMN]] = row[GENRE_NAME_COLUMN]

tracks_file = open(TRACK_METADATA_PATH, newline='', encoding='utf-8')
reader = csv.reader(tracks_file)

track_genres = {}

header = next(reader)
for row in reader:
    split_string = row[TRACK_GENRE_COLUMN][1:-1].strip().split(",")
    track_genre_top = split_string[0]
    if(track_genre_top in genres.keys()):
        track_genres[row[TRACK_ID_COLUMN]] = genres[track_genre_top]

print(track_genres['2'])


     
   

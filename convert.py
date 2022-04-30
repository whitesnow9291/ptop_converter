from lib2to3.pytree import convert
import docx2txt
from os import listdir, mkdir
from os.path import isfile, join
import tinify
import json
tinypng_api_key = 'cr8J4CzvN0W1QcyRXHVb6vxLjMb49fTl'
directory = r"../chords"
destionation = r'./extracted'

tinify.key = tinypng_api_key

def convertDirectory(dir_path):
    files = listdir(directory)
    file_id = 0
    chord_data = []
    for file_name in files:
        chordname = file_name.rsplit('.', 1)[0]

        docPath = join(dir_path, file_name)
        destPath = join(destionation, str(file_id))
        mkdir(destPath)
        docx2txt.process(docPath, destPath)

        images = listdir(destPath)
        chord = {
            'id': file_id,
            'label': chordname,
            'images': images
        }
        chord_data.append(chord)
        file_id = file_id + 1
    print(json.dumps(chord_data))
convertDirectory(directory)
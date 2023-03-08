from lib2to3.pytree import convert
import docx2txt
from os import listdir, mkdir, rmdir
import shutil
from os.path import isfile, join
import tinify
import json
tinypng_api_key = 'cr8J4CzvN0W1QcyRXHVb6vxLjMb49fTl'
directory = r"./chords"
destionation = r'./output'

tinify.key = tinypng_api_key

def convertDirectory(dir_path):
    # init 
    shutil.rmtree(destionation, ignore_errors=True)
    mkdir(destionation)
    # start
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
        require_images = []
        for img in images:
            img = f"require('../assets/chords/{file_id}/{img}')"
            require_images.append(img)
        chord = {
            'id': file_id,
            'label': chordname,
            'images': require_images
        }
        chord_data.append(chord)
        file_id = file_id + 1
    with open('chords.json', 'w') as outfile:
        json.dump(chord_data, outfile)
convertDirectory(directory)
from lib2to3.pytree import convert
import docx2txt
from os import listdir, mkdir, rmdir
from os.path import isfile, join
import tinify
import json
from shutil import rmtree
import docx
import os, re

directory = r"../chords"
destionation = r'./output'

def get_pictures(word_path, result_path):
    """
     Picture extraction 
    :param word_path: word route 
    :return: 
    """
    try:
        doc = docx.Document(word_path)
        dict_rel = doc.part._rels
        for rel in dict_rel:
            rel = dict_rel[rel]
            if "image" in rel.target_ref:

                if not os.path.exists(result_path):
                    os.makedirs(result_path)
                source_img_name = re.findall("/(.*)", rel.target_ref)[0]
                file_ext = os.path.splitext(source_img_name)[1]
                target_img_name = f'image{rel._rId}{file_ext}'
                print(source_img_name +":"+target_img_name)

                with open(f'{result_path}/{target_img_name}', "wb") as f:
                    f.write(rel.target_part.blob)
    except:
        pass




def convertDirectory(dir_path):
    files = listdir(directory)
    file_id = 0
    chord_data = []
    for file_name in files:
        chordname = file_name.rsplit('.', 1)[0]

        docPath = join(dir_path, file_name)
        destPath = join(destionation, str(file_id))
        
        get_pictures(docPath,destPath)

        images = listdir(destPath)
        require_images = []
        for img in images:
            img = f'require("../assets/chords/{file_id}/{img}")'
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

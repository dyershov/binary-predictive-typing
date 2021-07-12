import fast_autocomplete as _fac
import itertools as _itertools
import mcpt as _mcpt
import os as _os
import csv as _csv

def search_data_file(file_name):
    all_path = [_os.path.join(base, "data", file_name + ext) for base, ext in _itertools.product(_mcpt.__path__, ["", ".csv"])]
    for path in all_path:
        if _os.path.isfile(path):
            return path
    return ""

def default_data_file():
    return "english-wiki"

def word_frquency_from_csv_file(csv_file_name):
    words = dict()
    with open(csv_file_name, newline='') as csvfile:
         word_freq = _csv.reader(csvfile, delimiter=' ')
         for word, freq in word_freq:
             words[word] = _fac.loader.WordValue(context={}, display=word.lower(), count=int(freq))
    return words

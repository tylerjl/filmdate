#!/usr/bin/env python

import omdb

from sys      import exit
from guessit  import guess_file_info
from argparse import ArgumentParser

def year(filename):

    ret = None

    metadata = guess_file_info(filename)

    mediatype = metadata['type']
    if mediatype == 'unknown':
        print('File "{0}" failed to parse'.format(filename))
    elif mediatype != 'movie':
        print('File "{0}" is not a movie, quitting'.format(filename))
    else:
        omdb.set_default('tomatoes', True)
        tomato_data = omdb.title(metadata['title'])
        if len(tomato_data) <= 0:
            print('Could not retrieve Rotten Tomatoes metadata for {0}'.format(
                metadata['title']))
        else:
            ret = tomato_data['year']

    return ret

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    year = year(args.filename)
    if year is not None:
        print(year)
    else:
        exit(1)

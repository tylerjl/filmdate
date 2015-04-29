#!/usr/bin/env python

import omdb

from sys      import exit
from argparse import ArgumentParser

def year(filename):

    ret = None

    title_search = omdb.title(filename)
    if len(title_search) > 0:
        ret = title_search['year']
    else:
        movie_search = omdb.search_movie(filename)
        if len(movie_search) > 0:
            ret = movie_search[0]['year']
        else:
            print('Could not find year for "{0}"'.format(filename))

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

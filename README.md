# filmdate.py [![Build Status](https://travis-ci.org/tylerjl/filmdate.svg?branch=master)](https://travis-ci.org/tylerjl/filmdate)

Make a best-guess effort at a film title's release date.

This script leverages the excellent [Open Movie Database (OMDb)](https://github.com/dgilland/omdb.py) library to figure out a film title's release date.

Returns zero and prints the year if the script can parse a release date, exits non-zero with an error message if something fails.

## Use

Pretty easy. Note that you need the modules listed in `requirements.txt`, so get them installed however you like (usually `pip install -r requirements.txt`.)

As a command-line script:

```shellsession
$ ./filmdate.py True.Grit.avi
2010
```

From within python:

```
>>> import filmdate
>>> filmdate.year('The.Birds.mp4')
u'1963'
>>>
```

## Testing

Also easy:

```shellsession
$ nosetests
```

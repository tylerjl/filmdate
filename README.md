# filmdate.py

Make a best-guess effort at a film title's release date.

This script leverages both the excellent [guessit](https://github.com/wackou/guessit) library and the [Open Movie Database (OMDb)](https://github.com/dgilland/omdb.py) data and client to figure out a film title's release date.

## Use

Pretty easy:

```shellsession
$ filmdate True.Grit.avi
2010
```

## Testing

Also easy:

```shellsession
$ nosetests
```

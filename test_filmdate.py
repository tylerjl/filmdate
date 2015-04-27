from filmdate import year

def test_bad_filename():
    assert year('abcdefg') == None

def test_tv_filename():
    assert year('House.S01.E01.avi') == None

def test_old_movie_filename():
    assert year('Jaws.mp4') == '1975'

def test_new_movie_filename():
    assert year('Easy A.mkv') == '2010'

def test_newer_movie_filename():
    assert year('Interstellar.avi') == '2014'

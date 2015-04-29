from filmdate import year

def test_bad_filename():
    assert year('abcdefg') == None

def test_tv_filename():
    assert year('House.S01.E01') == None

def test_old_movie_filename():
    assert year('Jaws') == '1975'

def test_new_movie_filename():
    assert year('Easy A') == '2010'

def test_newer_movie_filename():
    assert year('Interstellar') == '2014'

def test_numeric_movie_filename():
    assert year('17 Again') == '2009'

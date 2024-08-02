from one_to_four.api.call import ice_b, req, gen_url, get_key, req2list, list2df, save2df
import pandas as pd

def test_ice_b():
    
    assert ice_b() == "ice breaking"


    assert True

def test_list2df():
    df = list2df()
    assert isinstance(df, pd.DataFrame)
    assert 'rnum' in df.columns
    assert 'openDt' in df.columns
    assert 'movieNm' in df.columns
    assert 'audiAcc' in df.columns 
def test_req2list():
    l = req2list()
    assert len(l) > 0
    v = l[0]
    assert 'rnum' in v.keys()
    assert v['rnum'] == '1'

def test_비밀키숨기기():
    key = get_key()
    assert key


def test_유알엘테스트():
    url = gen_url()
    assert "http" in url
    assert "kobis" in url
    
    d = {"multiMovieYn": "N"}
    url = gen_url(url_params = d)
    print(url)
    assert "multiMovieYn" in url
    

def test_req():
    
    code, data = req()
    assert code == 200

    code, data = req('20230101')
    print(data)
    assert code == 200


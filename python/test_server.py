from server import app

def test_home():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.json['Page'] == 'Home'
    
def test_urlinfo():
    response = app.test_client().get('/urlinfo/1/worksgreat.it:8080/foo/?sortBy=dependency&order=asc&page=1&perPage=500')
    
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json['isSafe'] == True
    
    
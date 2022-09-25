from application import app,greet,checkURL

def test_quick():
  a = "jeff"
  greeting = greet(a)
  assert greeting == "Hi jeff"

def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_urls_json():
    url = {'url': 'http://google.com'}
    bool = checkURL(url) 
    assert bool == True
     
            
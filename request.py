import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Mg':20, 'Na':90, 'Mg':6,'Al':55.9,'K':0.3,'Ca':23.0,'B':0,'Fe':0})

print(r.json())

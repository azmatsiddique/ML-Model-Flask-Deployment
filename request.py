import requests
url = 'http://localhost:5000/predict_api'
r = requests.post(url, json={
    'Mg': 1.52101,
    'Na': 13.64,
    'Mg': 4.49,
    'Al': 1.1,
    'Si': 71.78,
    'K': 0.06,
    'Ca': 8.75,
    'B': 0,
    'Fe': 0,
    })

return requests.get(r).json()


			
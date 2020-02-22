import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':20, 'test_score':90, 'interview_score':6})

print(r.json())

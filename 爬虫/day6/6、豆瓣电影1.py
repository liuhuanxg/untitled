import requests
import json
#第1屏：https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&start=0&limit=20
#第2屏：https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&start=20&limit=20

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&limit=589&start=0'
print(url)
response = requests.get(url)
moive_list = json.loads(response.text)
print(len(moive_list))
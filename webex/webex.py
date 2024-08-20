import requests
import json

access_token = 'YzVjMGRlNGItNmI5Yi00ODA1LTk3MDQtYmE0MTc2MWRjM2M3Yjc1YTAzNzAtMDI1_PF84_3f179706-f11a-4ab7-ba3e-57a4a96b089f'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
params = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vNTFmNTJiMjAtNWQwYi0xMWVmLWE5YTAtNzlkNTQ0ZjRkNGZi', 'max': '10'}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4, ensure_ascii=False).encode('utf8').decode())

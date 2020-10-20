# ref: https://docs.gitlab.com/ee/api/members.html
import requests

'''list member'''
list_member_api = 'http://hostname.co.jp/api/v4/projects/182/members?page=1'
res = requests.get(list_member_api, headers={'PRIVATE-TOKEN': 'xxxmytockenxxx'}).json()
# print(res)

'''add member'''
add_member_api = 'http://hostname.co.jp/api/v4/groups/15/members'

for item in res:
    res_added = requests.post(add_member_api, headers={'PRIVATE-TOKEN': 'xxxmytockenxxx'}, data={'user_id': item['id'], 'access_level': 30})
    print(res_added.json())

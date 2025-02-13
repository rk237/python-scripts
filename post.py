import requests
import json
import os

token = os.environ.get("github_token")
#below command checks if github token has been exported successfully or not
#print(f"Token: {token}")
reponame = input("enter repo name to be created : ")
url = f"https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}
r = requests.post(url+"user/repos", data=json.dumps(data),headers=headers)
print(r)
#print(r.json())



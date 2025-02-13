import os
import requests
import json
token = os.environ.get("github_token")
url = f"https://api.github.com"
reponame = input("enter reponame to be deleted : ")
headers = {"Authorization": "token {}".format(token)}
user = input("enter your github username : ")
data = {"name": "{}".format(reponame)}
r = requests.delete(url+"/repos/{}/{}".format(user,reponame),headers=headers)
print(r)

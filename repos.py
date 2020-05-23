import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print(r.status_code)

response_dict = r.json()
print(response_dict.keys())
print("Total repositories: " + str(response_dict['total_count']))

repo_dicts = response_dict['items']
print("Number of repositories returned: " + str(len(repo_dicts)))

repo_dict = repo_dicts[0]
print("Number of keys in the first repository: " + str(len(repo_dict)))

n = 1
for x in repo_dict.keys():
    print(str(n) + '\t' + x)
    n = n + 1

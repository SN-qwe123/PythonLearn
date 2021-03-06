import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print(r.status_code)

response_dict = r.json()
print(response_dict.keys())
print("Total repositories: " + str(response_dict['total_count']))

repo_dicts = response_dict['items']
print("Number of repositories returned: " + str(len(repo_dicts)))

print("\nSelected information about each repository:")

for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])

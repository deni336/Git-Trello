from github import Github
from prettytable import PrettyTable

g = Github("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")
x = PrettyTable()
for repo in g.get_user().get_repos():
    x.add_column(repo.name, dir(repo))
    repo.edit(has_wiki=False)
    
    #print(dir(repo))
    print(x)
    


import re
from trello import TrelloClient
from github import Github
import time

client = TrelloClient(api_key='4cd5173d5fbf8dceb732ac54a410e406',
                    api_secret='f5c1b76a7357592163e84cf2d6b3cd5f4e8efb8b98e37125f64adb4400814383',
                    token='4326574bb0721e0194c3d977df9c592fb1f2ba8808707bd8d1efbc4fbcdb173d')

def getTrelloCard():    
    testBoard = client.get_board('5baced22fe21ce0c7b8fb54a')
    boardList = testBoard.get_list('5baced22fe21ce0c7b8fb54b')
    boardCards = boardList.list_cards()
    cardDesc = boardCards[0].description
    cardProfile = [boardCards[0].name, cardDesc]
    return cardProfile

def recurringLoop(cardProfile):
    n = 5
    oldTrelloCard = getTrelloCard
    while n > 0:
        newTrelloCard = getTrelloCard()
        if newTrelloCard != oldTrelloCard:
            stringParser(newTrelloCard)
            oldTrelloCard = newTrelloCard
        else:
            time.sleep(30)

header = '''<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="index.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="icon" href="ViperWhite.ico">
        <title>ViperVisionReleaseNotes</title>
    </head>
    <body>
        <div class="main">
            <div class="header">
                <h1 id="title">ViperVision Release Notes</h1></div>'''

def stringParser(newTrelloCard):
    versionTitle = newTrelloCard[0]
    versionDescription = newTrelloCard[1]
    splitString = versionDescription.split('\n')
    completedString = ''
    with open("index.html", "r") as od:
        oldData = od.read()
    if oldData.find(versionTitle) == False:
        for string in splitString:
            if string.endswith('.') == True:
                line = "<li>" + string + "</li>"
                completedString = completedString + line
            elif string.isspace() == True:
                pass
            else:
                head = "<h3>" + string + "</h3>"
                completedString = completedString + head
        completedOutput = f'''<div id={versionTitle}><div class="align"><i id="i34" class="fa fa-minus" onclick="makeLittle('collapse-34', 'i34')" aria-hidden="true"></i><h2>ViperVision4.7.13.19</h2></div><ul id="collapse-34" class="active" style="display: block;"> {completedString}</ul></div>'''
        oldData = oldData.replace('''style="display: block;"''', "")
        oldData = oldData.replace("minus", "plus")
        finishedOutput = header + completedOutput + oldData
        file = open("index.html", "w")
        file.write(finishedOutput)
        file.close
    else:
        splitOldData = re.split("(\</div>)", oldData)
        for i in range(0,6):    
            splitOldData.pop(0)
        newOldData = ""
        oldDataWithoutPreviousVersion = newOldData.join(splitOldData)
        for string in splitString:
            if string.endswith('.') == True:
                line = "<li>" + string + "</li>\n"
                completedString = completedString + line
            elif string == "":
                pass
            else:
                head = "<h3>" + string + "</h3>\n"
                completedString = completedString + head
        completedOutput = f'''<div id="{versionTitle}"><div class="align"><i id="i34" class="fa fa-minus" onclick="makeLittle('collapse-34', 'i34')" aria-hidden="true"></i><h2>ViperVision4.7.13.19</h2></div><ul id="collapse-34" class="active" style="display: block;"> {completedString}</ul></div>'''
        oldData = oldData.replace('''style="display: block;"''', "")
        oldData = oldData.replace("minus", "plus")
        
        finishedOutput = header + completedOutput + oldDataWithoutPreviousVersion
        file = open("index.html", "w")
        file.write(finishedOutput)
        file.close
        githubPush()

def githubPush():
    g = Github("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")
    repo = g.get_user().get_repo("TestRepo")
    all_files = []
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents("index.html"))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))
    with open('index.html', 'r') as file:
        content = file.read()
    git_file = 'index.html'
    if git_file in all_files:
        contents = repo.get_contents(git_file)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch="main")
        print(git_file + ' UPDATED')
    else:
        repo.create_file(git_file, "committing files", content, branch="main")
        print(git_file + ' CREATED')
githubPush()
recurringLoop(getTrelloCard())
    


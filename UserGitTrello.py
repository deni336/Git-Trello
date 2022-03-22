from trello import TrelloClient
from github import Github
from html.parser import HTMLParser
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
    oldTrelloCard = []
    while n > 0:
        newTrelloCard = getTrelloCard()
        if newTrelloCard != oldTrelloCard:
            stringParser(newTrelloCard)
            oldTrelloCard = newTrelloCard
        else:
            time.sleep(30)

header = '''</div><!DOCTYPE html>
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
                <h1 id="title">ViperVision Release Notes</h1>\n'''
def stringParser(newTrelloCard):
    versionTitle = newTrelloCard[0]
    versionDescription = newTrelloCard[1]
    splitString = versionDescription.split('\n')
    completedString = ''
    with open("index.html", "r") as od:
        oldData = od.read()
    checkVersion = oldData.split('div')
    checkVersion = checkVersion[5].split('"')
    if checkVersion[1] != versionTitle:
        for string in splitString:
            if string.endswith('.') == True:
                line = "<li>" + string + "</li>\n"
                completedString = completedString + line
            else:
                head = "<h3>" + string + "</h3>\n"
                completedString = completedString + head
        completedOutput = f'''<div id={versionTitle}><div class="align"><i id="i34" class="fa fa-minus" onclick="makeLittle('collapse-34', 'i34')" aria-hidden="true"></i><h2>ViperVision4.7.13.19</h2></div><ul id="collapse-34" class="active" style="display: block;">\n {completedString}</div>'''
        oldData = oldData.replace('''</div><!DOCTYPE html>
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
                <h1 id="title">ViperVision Release Notes</h1>\n''', "")
        oldData = oldData.replace('''style="display: block;"''', "")
        oldData = oldData.replace("minus", "plus")
        
        finishedOutput = header + completedOutput + oldData
        file = open("index.html", "w")
        file.write(finishedOutput)
        file.close
    else:
        splitOldData = oldData.split("</div")
        removedData1 = splitOldData.pop(1)
        removedData2 = splitOldData.pop(1)
        newOldData = ""
        oldDataWithoutPreviousVersion = newOldData.join(splitOldData)
        for string in splitString:
            if string.endswith('.') == True:
                line = "<li>" + string + "</li>\n"
                completedString = completedString + line
            else:
                head = "<h3>" + string + "</h3>\n"
                completedString = completedString + head
        completedOutput = f'''<div id="{versionTitle}"><div class="align"><i id="i34" class="fa fa-minus" onclick="makeLittle('collapse-34', 'i34')" aria-hidden="true"></i><h2>ViperVision4.7.13.19</h2></div><ul id="collapse-34" class="active" style="display: block;">\n {completedString}</div>'''
        oldData = oldData.replace('''</div><!DOCTYPE html>
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
                <h1 id="title">ViperVision Release Notes</h1>\n''', "")
        oldData = oldData.replace('''style="display: block;"''', "")
        oldData = oldData.replace("minus", "plus")
        
        finishedOutput = header + completedOutput + oldDataWithoutPreviousVersion
        file = open("index.html", "w")
        file.write(finishedOutput)
        file.close

def githubPush():
    g = Github("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")
    pass

recurringLoop(getTrelloCard())
    


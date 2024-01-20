# Carter Savage 1103661
import urllib.request
import json
from crypt import methods
from distutils import filelist
from unittest import result
from urllib import request
from urllib.request import urlopen
from flask import Response
from os.path import exists
import os
from flask import Flask, redirect, url_for, send_from_directory, request, render_template, make_response

app = Flask(__name__, static_url_path = '')

@app.route("/")
def homePage():
    # making cookie name very unique
    pref = request.cookies.get("subPref12345678","None")
    if pref == "ApexKeys":
        return displayCached("ApexKeys.txt", "https://www.apexkeyboards.ca/products/")
    elif pref == "MinoKeys":
        return displayCached("MinoKeys.txt", "https://minokeys.com/products/")
    elif pref == "MechMark":
        return displayCached("MechMarket.txt", "")
    else:
        return render_template('index.html', list = "", prefix = "")


@app.route('/ApexKeys')
def getAK():
    results = "<ul>"
    File = open("ApexKeys.txt", "w")
    contents = urllib.request.urlopen("https://www.apexkeyboards.ca/products.json?limit=250&page=1")
    contentsJSON = json.loads(contents.read())
    numChildren = len(contentsJSON["products"])
    for x in range(0, numChildren):
        temp = json.dumps(contentsJSON["products"][x]["handle"])
        temp = temp.replace('"','')
        # we do not want just pictures but the whole article
        if ".jpg" not in temp and ".png" not in temp:
            results += "<li>" + "<a href=https://www.apexkeyboards.ca/products/" + temp + ">" + temp + "</li>"
            File.write(temp)
            File.write("\n")
    File.close()
    results += "</ul>"
    resp = make_response(Response(results, status=200))
    resp.set_cookie("subPref12345678", "ApexKeys")
    return resp

@app.route('/ApexKeysNoJS')
def getAKNoJS():
    results = []
    contents = urllib.request.urlopen("https://www.apexkeyboards.ca/products.json?limit=250&page=1")
    contentsJSON = json.loads(contents.read())
    numChildren = len(contentsJSON["products"])
    for x in range(0, numChildren):
        temp = json.dumps(contentsJSON["products"][x]["handle"])
        temp = temp.replace('"','')
        # we do not want just pictures but the whole article
        if ".jpg" not in temp and ".png" not in temp:
            results.append(temp)
    File = open("ApexKeys.txt", "w")
    for url in results:
        File.write(url)
        File.write("\n")
    File.close()
    resp = make_response(render_template('index.html', list = results, prefix = "https://www.apexkeyboards.ca/products/"))
    resp.set_cookie("subPref12345678", "ApexKeys")
    return resp, 200
    

@app.route('/MinoKeys')
def getMinoKeys():
    results = "<ul>"
    File = open("MinoKeys.txt", "w")
    contents = urllib.request.urlopen("https://minokeys.com/products.json?limit=250&page=1")
    contentsJSON = json.loads(contents.read())
    numChildren = len(contentsJSON["products"])
    for x in range(0, numChildren):
        temp = json.dumps(contentsJSON["products"][x]["handle"])
        temp = temp.replace('"','')
        # we do not want just pictures but the whole article
        if ".jpg" not in temp and ".png" not in temp:
            results += "<li>" + "<a href=https://minokeys.com/products/" + temp + ">" + temp + "</li>"
            File.write(temp)
            File.write("\n")
    File.close()
    results += "</ul>"
    resp = make_response(Response(results, status=200))
    resp.set_cookie("subPref12345678", "MinoKeys")
    return resp

@app.route('/getMinoKeysNoJS')
def getMinoKeysNoJS():
    results = []
    contents = urllib.request.urlopen("https://minokeys.com/products.json?limit=250&page=1")
    contentsJSON = json.loads(contents.read())
    numChildren = len(contentsJSON["products"])
    for x in range(0, numChildren):
        temp = json.dumps(contentsJSON["products"][x]["handle"])
        temp = temp.replace('"','')
        # we do not want just pictures but the whole article
        if ".jpg" not in temp and ".png" not in temp:
            results.append(temp)
    File = open("MinoKeys.txt", "w")
    for url in results:
        File.write(url)
        File.write("\n")
    File.close()
    resp = make_response(render_template('index.html', list = results, prefix = "https://minokeys.com/products/"))
    resp.set_cookie("subPref12345678", "MinoKeys")
    return resp, 200

@app.route('/MechMarket')
def getMechMarket():
    results = "<ul>"
    File = open("MechMarket.txt", "w")
    # preventing 429 too many requests response from reddit
    req = urllib.request.Request("https://www.reddit.com/r/mechmarket/.json")
    req.add_header('User-agent', 'your bot 0.1')
    contents = urlopen(req)
    contentsJSON = json.loads(contents.read())
    numChildren = len(contentsJSON["data"]["children"])
    for x in range(0, numChildren):
        temp = json.dumps(contentsJSON["data"]["children"][x]["data"]["url"])
        temp = temp.replace('"','')
        # we do not want just pictures but the whole article
        if ".jpg" not in temp and ".png" not in temp:
            results += "<li>" + "<a href=" + temp + ">" + temp + "</li>"
            File.write(temp)
            File.write("\n")
    File.close()
    results += "</ul>"
    resp = make_response(Response(results, status=200))
    resp.set_cookie("subPref12345678", "MechMark")
    return resp

@app.route('/MechMarketNoJS')
def getMechMarketNoJS():
    results = []
    # preventing 429 too many requests response from reddit
    req = urllib.request.Request("https://www.reddit.com/r/mechmarket/.json")
    req.add_header('User-agent', 'your bot 0.1')
    contents = urlopen(req)
    contentsJSON = json.loads(contents.read())
    numChildren = len(contentsJSON["data"]["children"])
    for x in range(0, numChildren):
        temp = json.dumps(contentsJSON["data"]["children"][x]["data"]["url"])
        temp = temp.replace('"','')
            
        # we do not want just pictures but the whole article
        if ".jpg" not in temp and ".png" not in temp:
            results.append(temp)
    File = open("MechMarket.txt", "w")
    for url in results:
        File.write(url)
        File.write("\n")
    File.close()
    resp = make_response(render_template('index.html', list = results, prefix = ""))
    resp.set_cookie("subPref12345678", "MechMark")
    return resp, 200

def displayCached(file, Prefix):
    results = []
    File = open(file, "r")
    for line in File:
        results.append(line)
    File.close()
    resp = make_response(render_template('index.html', list = results, prefix = Prefix))

    return resp, 200

if __name__ == "__main__":
    app.run()
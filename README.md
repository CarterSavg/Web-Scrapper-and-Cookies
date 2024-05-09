Web-Scrapper and Cookies README \
Author: Carter Savage

## Description
Welcome to the web-scrapper and tracking cookies project. This project uses flask to simulate a website running locally. The scrapping is done on the server side but only when a button is pushed. Meaning that if a user comes back to the website after closing it their preferences will be saved and loaded from the cache on the server instead on rescrapping the website. This allows for very fast initial load times. 

## Usage
To make this application work simply run the app.py file (python app.py). 
This will start the flask application in the terminal. Control click on the local host address (eg. http://127.0.0.1:5000) to open the webpage.
From there you will see a webpage with 3 buttons.  

When clicked each button will display a list of links and save a cookie as this website is their preference. 
When coming back to the site with cookies the persons prefered preference(the button they clicked on last) will already be displayed.
This list is retrieved from a chached list of links on the server (the appropriate txt file). This chache is updated everytime data is pulled from its website (its button gets pressed).This allows the website to have a very fast load time as it does not need to pull information from another website. 
To change preference simply click on a different button. \
The CSS on this page is very limited with it just being a nice looking charcoal background and positional css. 

All of my python code is in app.py in the root directory \
All of my javascript code is in the static/js directory in the index.js file \
The homepage html is in the templates directory in the index.html file 

## Features

* Tracking Cookies 
* Web-Scrapping
* Flask 
* Caching 

## Credits
* This project was created by me!
Enjoy the web-scrapper!

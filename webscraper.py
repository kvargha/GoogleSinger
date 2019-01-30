#Imports BeautifulSoup library
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#Imports method from googlebot that converts text to speech
from googlebot import constructMP3

#Base search url for AZ Lyrics
base_url = "https://search.azlyrics.com/search.php?q="

#Prompts for the song name
songName = input("Please enter the name of the song you'd like me to sing: ")

#Replaces spaces with +
songName = songName.replace(" ", "+")
print(songName)
#Searches for song on AZ Lyrics
url = base_url + songName
print(url)

################################
#Parsing song results page
################################

#Opening up connecting to page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

#HTML parsing
page_soup = soup(page_html, "html.parser")

#Grabs container with lists of songs
allContainers = page_soup.findAll("table",{"class":"table table-condensed"})
container = allContainers[2]
#print(allContainers)
#container = allContainers.findAll("td", {"class":"text-left visitedlyr"})
#container = container[0]

#Grabs first song result
songUrl = container.a["href"]
print(songUrl)
artist = container.findAll('b')[1].text
songName = container.b.text

#Prints song name and artist
print("This is " + songName + " by " + artist + ".")



################################
#Parsing song page
################################

#Opening up connecting to page
uClient = uReq(songUrl)
page_html = uClient.read()
uClient.close()

#HTML parsing
page_soup = soup(page_html, "html.parser")

#Grabs song lyrics
allContainers = page_soup.find("div",{"class": "col-xs-12 col-lg-8 text-center"})
allContainers = allContainers.findAll("div")
lyrics = allContainers[6].text

#Converts song lyrics into mp3 using Google's Nautral Language
constructMP3(lyrics, songName + "-" + artist)


from bs4 import BeautifulSoup as BSoup
import requests
import re

class Crawler:
  def __init__(self):
    self.baseUrl = "https://leagueoflegends.fandom.com/"
    self.specificAudioPath = "champion/LoL/Audio"
    self.allAudioPath = "wiki/Category:Champion_audio"
    self.championNameRegex = "/wiki/Category:([\w'.]+)_voice-overs"  # test on: Rek'sai Aurelion_Sol etc.

  # start crawling and get all the '.ogg' files urls
  # Returns dictionary: { champion: [list of ogg urls] }
  def getOggUrls(self):
    championNames = self.getChampionNames()
    print('Found {} champions'.format(len(championNames)))

    championAudioDict = {}
    for champion in championNames:
      print('Fetching oggs for ' + champion)
      pathToChampionAudio = self.specificAudioPath.replace("champion", champion)
      audioPage = self.fetchSoupPage(self.baseUrl + pathToChampionAudio)

      listOfOggFiles = []
      
      # find all '.ogg' files as  url links (<a href="/wiki/File:SadRobotAmumu.attack1.ogg" title="File:SadRobotAmumu.attack1.ogg" />)
      # TODO : check if these Soup things work
      for link in audioPage.find_all('sup'):
        print("Got link and found: " + link.a['href'])
        listOfOggFiles.append(link.a['href'])

      if len(listOfOggFiles) == 0:
        print('Couldn\'t find any audio file for champion: ' + champion)
      else:
        print('Found {} oggs'.format(len(listOfOggFiles)))
        championAudioDict[champion] = listOfOggFiles
    
      if True:
        break

    return championAudioDict

  # returns list of champion names in link format (i.e. Aurelion_sol)
  def getChampionNames(self):
    championsPage = self.fetchSoupPage(self.baseUrl + self.allAudioPath)
    
    names = []
    # <a class="category-page__member-link" href="/wiki/Category:Old_champion_audio" title="Category:Old champion audio">Category:Old champion audio</a>
    for link in championsPage.find_all("a", class_="category-page__member-link"):
      championName = re.search(self.championNameRegex, link['href'])

      if championName is not None:
        names.append(championName.group(1))
      else:
        print('Champion name not found in: ' + link['href'])

  def fetchSoupPage(self, url):
    html = requests.get(url)
    if not html.ok:
      print('Couldn\'t fetch url: ' + url)
      return None
    return BSoup(html.text, 'html.parser')
from calendar import c
from crawler.crawler import Crawler 

if __name__ == '__main__':
  print("Starting...")
  crawler = Crawler()
  championOggsDict = crawler.getOggUrls()
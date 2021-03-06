from urllib.request import urlopen
import re

# list of albums is broken up into separate pages for every 50 albums
# this list is from bottom (500) to top (1) ranking
url_list = ["https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/",
            "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/linda-mccartney-and-paul-ram-1062783/",
            "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/the-go-gos-beauty-and-the-beat-1062833/",
            "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/stevie-wonder-music-of-my-mind-2-1062883/",
            "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/shania-twain-come-on-over-1062933/",
            "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/whitney-houston-whitney-houston-2-1062984/",
            "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/sade-diamond-life-1063033",
            "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/bruce-springsteen-nebraska-3-1063083",
            "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/the-band-music-from-big-pink-2-1063133/",
            "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/jay-z-the-blueprint-3-1063183"]

album_re = "{\"ID\".*?}" # matches all relevant data for a particular album

for u in url_list:
  html = urlopen(u).read().decode("utf-8")
  data_start = html.find("pmcGalleryExports") # album data is stored in the variable "pmcGalleryExports"
  data_end = html.find("galleryCount")        # end of the album data
  album_data = html[data_start:data_end]
  albums = re.findall(album_re, album_data)
  break
  # TODO: for each album, extract relevant data and store in a csv
  # relevant data = "positionDisplay" (rank)
  #                 "title" (form of Artist, Album)
  #                 "subtitle" (form of Label, Year)
  #                 "description" (text is inside <p> tags)

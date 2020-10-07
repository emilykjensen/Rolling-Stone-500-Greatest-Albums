from urllib.request import urlopen

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

for u in url_list:
  html = urlopen(u).read().decode("utf-8")
            
            
#album data is stored in the variable "pmcGalleryExports"

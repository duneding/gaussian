from skimage import data, io, filters
from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib2 import Request
import urllib

image = data.coins()
# ... or any other NumPy array!
edges = filters.sobel(image)
#io.imshow(edges)
#io.show()

file_dist_london = '../resources/distractors/distractors_urls_london.csv'

'''
with open(file_dist_london, 'r') as file:
    for index, url in enumerate(file):
        name = index
        urllib.urlretrieve(url.strip(), '../resources/london/'+`name`+'.jpg')
'''
'''
def make_soup(url):
    header = {'User-Agent': 'Mozilla/5.0'}
    request = Request(url,headers=header)
    page = urlopen(request)
    #html = urlopen(url).read()
    return BeautifulSoup(page)

def get_images(url):
    soup = make_soup(url)
    #this makes a list of bs4 element tags
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + "images found.")
    print 'Downloading images to current working directory.'
    #compile our unicode list of image links
    image_links = [each.get('src') for each in images]
    for each in image_links:
        filename=each.split('/')[-1]
        urllib.urlretrieve(each, '../resources/london2/'+filename)
    return image_links

get_images('http://www.bugbog.com/gallery/london_pictures')
'''


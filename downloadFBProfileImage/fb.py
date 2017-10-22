#!/usr/bin/python

"""
    Get random FB profile image
"""

import json
import random
import urllib2
import os, sys

DEFAULT_PATH = "."
DEFAULT_TOT_IMAGE = 10
FB_URL = "https://graph.facebook.com/{0}/picture?type=large&width=250&height=250&redirect=false"

""" get a resource by url """
def getResource(url):
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        return response.read()
    except:
        return ""

""" save content in a file """
def saveFile(content, path, filename):
    filename = os.path.join(path, filename + ".jpg")
    with open(filename, 'w') as file:
        file.write(content)

""" get a random image """
def main(path_to_save, tot_image_request):
    i = 0
    while i < tot_image_request:
        rnd = str(random.randint(1120000000, 1199999999))
        url = FB_URL.format(rnd)
        data = getResource(url)
        
        if data == "":
            continue

        data = json.loads(data)
        if not data["data"]["is_silhouette"]:
            saveFile(getResource(data["data"]["url"]), path_to_save, rnd)
            i += 1

if __name__ == '__main__':

    path_to_save = DEFAULT_PATH
    tot_image_request = DEFAULT_TOT_IMAGE

    if len(sys.argv) >= 3:
        path_to_save = sys.argv[1]
        try:
            tot_image_request = int(sys.argv[2])
        except:
            print "Not valid argument"
            sys.exit()
    elif len(sys.argv) == 2:
        path_to_save = sys.argv[1]

    main(path_to_save, tot_image_request)

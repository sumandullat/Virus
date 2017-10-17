#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
"""
Webscraper that downloads xkcd comics
Checks if comic already downloaded so for increased efficiency on rerun.

Two run modess: Full and Quick
Full mode goes through every comic.
Quick mode quits when it reaches the first comic that is already downloaded.

Needs feature update where title text is in properties of downloaded image.

https://automatetheboringstuff.com/chapter11/
"""
import time
import os
import requests
import bs4

print('This script searches xkcd.com and downloads each comic.')

# User input for full run or until finding already downloaded comic.
print('There are two mode options:\n'
      '\nQuick mode: Or "refresh mode", checked until it finds '
      'a previously downloaded comic.\n'
      ' Full mode: Checks for every comic, downloads undownloaded comics.\n'
      )

while True:
    try:
        print('Please select mode:\n'
              'Enter 0 for Quick mode, or 1 for Full Mode')
        run_mode_selection = input('Mode: ')
        if int(run_mode_selection) == 0:
            run_mode = False  # Quick mode
            break
        if int(run_mode_selection) == 1:
            run_mode = True    # Full mode
            break
    except ValueError:
        continue

start = time.time()


def getPrevLink(soup, url):
    prevLink = soup.select('a[rel="prev"]')[0]
    return 'https://xkcd.com' + prevLink.get('href')


url = 'https://xkcd.com'              # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd

while not url.endswith('#'):
    # Download the page.
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'https:' + comicElem[0].get('src')
            # Download the image.
            print(f'Downloading image {comicUrl}...')
            res = requests.get(comicUrl)
            res.raise_for_status()
            # Check if comic previously downloaded.
            imageFile = open(os.path.join(
                    'xkcd',
                    (f'{urlNumber} - {os.path.basename(comicUrl)}')), 'xb')
        except requests.exceptions.MissingSchema:
            # skip this comic
            url = getPrevLink(soup, url)
            continue
        except FileExistsError:
            print(f'--- Comic {urlNumber} already downloaded.---')
            if run_mode:   # Full mode
                # skip this comic
                url = getPrevLink(soup, url)
                continue
            if not run_mode:
                print('Finished updating archive.')
                break
        # TODO: Needs feature update where title text
        #       is in properties of downloaded image.

        # Save the image to ./xkcd.
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    url = getPrevLink(soup, url)

print('Done.')

timetotal = time.time() - start
if timetotal > 60:
    mins = timetotal//60
    sec = timetotal-mins*60
    print(f"Runtime: {mins:.0f} minutes, {sec:.2f} seconds")
else:
    print(f"Runtime: {timetotal:.2f} seconds")

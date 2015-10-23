from bs4 import BeautifulSoup
from urllib2 import urlopen
from os import listdir
from os.path import isfile, join
from apiclient.discovery import build
import json, sys
import os
import shutil


filepath = "/Users/acheng/Documents/Songs"


def get_file_names(directory):
    return [f for f in listdir(directory) if isfile(join(directory, f))]

def is_good_name(filename):
    if filename.count("-") != 1:
        return False

    return True


def get_artist_name(filename):
    return filename.split("-", 1)[0].strip()

def get_song_name(filename):
    temp = filename.split("-", 1)
    substr = temp[1].split(".", 1)
    return substr[0].strip()

def get_beatport_url(search_term):
    search_engine_id = '007803631241409669231:dqrjqhyoywq'
    api_key = 'AIzaSyChjdmce1stSrQPMG8pt-XVBvsMDhKssPc'
    service = build("customsearch", "v1", developerKey = api_key)
    collection = service.cse()
    request = collection.list(q = search_term, num = 10,
            start = 1, cx = search_engine_id)
    response = request.execute()
    output = json.dumps(response, sort_keys = True, indent = 2)
    data = json.loads(output)
    if "items" in data:
        print data["items"][0]["formattedUrl"]
        return data["items"][0]["formattedUrl"]
    else:
        print "%s yielded no results in Beatport" % search_term
        return "SKIP"

def get_bpm_key(beatport_url):
    html = urlopen(beatport_url).read()
    soup = BeautifulSoup(html, "lxml")
    content_list = soup.find("ul", "interior-track-content-list")
    bpm_content = content_list.find("li", {"class": "interior-track-content-item interior-track-bpm"})
    key_content = content_list.find("li", {"class": "interior-track-content-item interior-track-key"})
    bpm = bpm_content.find("span", {"class": "value"}).text
    key = key_content.find("span", {"class": "value"}).text
    return {"BPM": bpm, "Key": key}

if __name__ == '__main__':
    filenames = get_file_names(filepath)
    num_files = len(filenames) - 1
    num_renamed = 0
    iterfiles = iter(filenames)
    next(iterfiles)
    for file in iterfiles:
        if not is_good_name(file):
            print "%s is not formatted properly" % file
            continue
        filepath_all =  filepath + "/" + file
        artist = get_artist_name(file)
        song = get_song_name(file)
        beatport_url = get_beatport_url(artist + " " + song)
        if beatport_url == "SKIP":
            continue
        track_data = get_bpm_key(beatport_url)
        bpm = track_data["BPM"]
        key = track_data["Key"]
        new_filepath = filepath + "/%s_%sbpm_%s--%s.mp3" % (key, bpm, artist, song)
        shutil.copyfile(filepath_all, new_filepath)
        os.remove(filepath_all)
        num_renamed += 1
    print "=== Renamed %i/%i files. ===" % (num_renamed, num_files)

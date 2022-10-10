#!/usr/bin/python
import json
import sys
import requests
from mysecrets import spotify_user_id
import json
import requests
from mysecrets import spotify_user_id,  discover_weekly_id
from refresh import Refresh


class Playlists:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = ""
        self.discover_weekly_id = discover_weekly_id
        self.playlistNames =[] 
        self.playlistURI =[] 
        self.playlists = {} 
        self.playlistToChangeTo = -1 
        if len(sys.argv) > 1:
            self.playlistToChangeTo = int(sys.argv[1])

    def get_playlists(self):

        query = "https://api.spotify.com/v1/me/playlists"
        response = requests.get(query,
                                headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format(self.spotify_token)})
        response_json = response.json()
        #  print(response_json)
        
        for i in response_json["items"]:
            self.playlistNames.append(i["name"])
            self.playlistURI.append(i["uri"])

        for key in self.playlistNames:
            for value in self.playlistURI:
                self.playlists[key] = value

        #  with open("playlists.json", "wt") as outfile:
        #      json.dumps(self.playlists, indent = 4)
        #      #  print(self.playlists)

    def change_playlist(self):
        query = "https://api.spotify.com/v1/me/player/play"
        request_body = json.dumps({
                            "context_uri": self.playlistURI[self.playlistToChangeTo],
                            "offset": {
                                "position": 5
                            },
                            "position_ms": 0
                        })
        response = requests.put(query, data=request_body,
                                headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format(self.spotify_token)})
        print(response.json)

        

    def call_refresh(self):

        print("Refreshing token")
        refreshCaller = Refresh()
        self.spotify_token = refreshCaller.refresh()
        self.get_playlists()
        if self.playlistToChangeTo != -1:
            self.change_playlist()
a = Playlists()
a.call_refresh()


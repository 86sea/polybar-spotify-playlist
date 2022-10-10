# polybar-spotify-playlist
uses spotify web api to change/view playlists.
Usage: 
  rename secrets.py to mysecrets.py and add your data, see https://developer.spotify.com/documentation/general/guides/authorization/
   note for base64 variable:encoded string that contains the client ID and client secret key. 
   The field must have the format: Authorization: Basic <base64 encoded client_id:client_secret>
   can be used for general API requests
   
polybar config.ini, a little bit janky as polybar doesn't support viables with exec:

```INI
[module/menu-apps]
type = custom/menu

; If true, <label-toggle> will be to the left of the menu items (default).
; If false, it will be on the right of all the items.
expand-right = true

; "menu-LEVEL-N" has the same properties as "label-NAME" with
; the additional "exec" property
;
; Commands will be executed using "/bin/sh -c $COMMAND"

menu-0-0 =  ${names.0}
menu-0-0-exec =  python ~/.config/polybar/scripts/spotify_playlist/main.py '0'
menu-0-1 = ${names.1}
menu-0-1-exec = python ~/.config/polybar/scripts/spotify_playlist/main.py '1' 

menu-0-2 = ${names.2}
menu-0-2-exec = python ~/.config/polybar/scripts/spotify_playlist/main.py '2' 

menu-0-3 = ${names.3}
menu-0-3-exec = python ~/.config/polybar/scripts/spotify_playlist/main.py '3' 

menu-0-4 = ${names.4}
menu-0-4-exec = python ~/.config/polybar/scripts/spotify_playlist/main.py '4' 

label-open = Playlist 
label-close = x
```
   

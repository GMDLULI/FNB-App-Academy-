
import requests

API_URL = "https://6ade03414e88f1bba4a4e17d.mockapi.io/api/colledgedropout/songs"

# 1. Getting all songs
print("*****************************GET ALL SONGS*******************************")

try:
    get_all_songs = requests.get(API_URL)
    get_all_songs.raise_for_status
    api_response = get_all_songs.json()
    print("Status Code: ", get_all_songs.status_code)
    print("All Songs: ", api_response )
except requests.exceptions.HTTPError as http:
    print("An Error Occurred: ", http)

#1.creating a song

print("*****************************CREATING SONG*******************************")
try: 
    new_song = {
        "id": "6",
        "name": "Racking Ball",
        "rating": 9
    }
    create_new_song = requests.post(API_URL,json= new_song)
    create_new_song.raise_for_status
    api_response = create_new_song.json()
    print('Status Code: ', create_new_song.status_code)
    print('Son Created!!!!  New Song: ', api_response['name'])
except requests.exceptions.HTTPError as http:
    print(http)


# 2.Replacing a song 
print("*****************************Updating a song*******************************")

try:
    updated_song  = {
        'id': '1',
        "name": "Girls just want to have fun",
        "rating": 8
    }
    update_song = requests.put(API_URL + '/1', updated_song)
    update_song.raise_for_status
    api_response = update_song.json()
    print('Status Code: ' ,update_song.status_code)
    print("Updated song: ", api_response)
except requests.exceptions.HTTPError as http:
    print(http)


# Deleting song 
print("*****************************delete a song*******************************")

try:
   
    delete_song = requests.delete(API_URL + '/6')
    delete_song.raise_for_status
    api_response = delete_song.json()
    print('Status Code: ' ,delete_song.status_code)
    print("Updated song: ", api_response)
except requests.exceptions.HTTPError as http:
    print(http)
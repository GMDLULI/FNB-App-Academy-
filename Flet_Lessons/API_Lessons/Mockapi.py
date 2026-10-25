# API_Endpoint = https://6accd920b406cb8ec0c68f3a.mockapi.io/album/Graduation
import requests



API_Endpoint = "https://6accd920b406cb8ec0c68f3a.mockapi.io/album/Graduation"

#Get all songs
try:
    getAllSongs = requests.get(API_Endpoint)
    getAllSongs.raise_for_status()
    print('Status Code:', getAllSongs.status_code)
    response = getAllSongs.json()
    print('Graduation Songs:', response)
    print()
    print('************OneSong************')
    getOneSong = requests.get(API_Endpoint + '/1')
    getOneSong.raise_for_status()
    responseOneSong = getOneSong.json()['name']
    print('One Song:', responseOneSong)
    print()
    print("\n************Rating************")
    rating = getOneSong.json()['rating']
    print('Rating:', rating)
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")


# Post method to add a new song
# print("\n************Add New Song************")
# try:
#     new_song = {
#         'id': '4',
#         'name': 'Good Life',
#         'rating': '7'
#     }
#     responseNewSong = requests.post(API_Endpoint, json=new_song)
#     responseNewSong.raise_for_status()
#     print('Status Code:', responseNewSong.status_code)
#     print('New Song Added:', responseNewSong.json())

# except requests.exceptions.HTTPError as err:
#     print(f"HTTP error occurred: {err}")

#PUT method to update a song
print()
print("\n************Update Song************")

"""
try:
    replace_song = {
        'id': '2',
        'name': 'Good Night',
        'rating': 7
    }
    responseReplacement= requests.put(API_Endpoint + '/2', json=replace_song)
    responseReplacement.raise_for_status()
    print('Status Code:', responseReplacement.status_code)
    print('Replacement:', responseReplacement.json())

except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
""" 

print()
print("\n************Delete Song************")
try:
    deleteSong = requests.delete(API_Endpoint + '/3')
    deleteSong.raise_for_status()
    print('Status Code:', deleteSong.status_code)
    print('Song Deleted:', deleteSong.json())

except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")



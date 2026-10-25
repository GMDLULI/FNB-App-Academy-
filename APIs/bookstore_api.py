import requests


def get_books(API_KEY):
    print("*****************************GET ALL SONGS*******************************")


    try:
        get_all_books = requests.get(API_KEY)
        get_all_books.raise_for_status
        api_response = get_all_books.json()
        print("Status Code: ", get_all_books.status_code)
        print("All Books: ", api_response)

        return api_response
    except requests.exceptions.HTTPError as http:
        print('Error: ', http)

def add_book(API_KEY, new_book):
    print("***************************** ADD A SONG *******************************")


    try:
        get_all_books = requests.post(API_KEY, json=new_book)
        get_all_books.raise_for_status
        api_response = get_all_books.json()
        print("Status Code: ", get_all_books.status_code)
        print("All Books: ", api_response)

        return api_response
    except requests.exceptions.HTTPError as http:
        print('Error: ', http)

def update_book(API_KEY, update_book):
    print("***************************** UPDATING  A SONG *******************************")


    try:
        update_a_book = requests.put(API_KEY +'/3', json=update_book)
        update_a_book.raise_for_status
        api_response = update_a_book.json()
        print("Status Code: ", update_a_book.status_code)
        print("Updated Book: ", api_response['title'])
        return api_response
    except requests.exceptions.HTTPError as http:
        print('Error: ', http)

def delete_book(API_KEY, id):
    print("***************************** DELETING ALL SONGS*******************************")



    try:
        delete_book = requests.delete(API_KEY + id)
        delete_book.raise_for_status
        api_response = delete_book.json()
        print("Status Code: ", delete_book.status_code)
        print("Deleted Book: ", api_response)

        return api_response
    except requests.exceptions.HTTPError as http:
        print('Error: ', http)


if __name__ == "__main__":
    API_KEY ="https://6ade154b4e88f1bba4a4f19c.mockapi.io/api/bookstore/books"

    get_books(API_KEY)

    new_book = {
        "id": 6,
        "title": "Killing Mr Griffin",
        "author": "Lois Duncan",
        "rating": "6"
    }
    add_book(API_KEY, new_book)

    updated_book = {
         "id": "3",
    "title": "How To Make Friends With The Dark",
    "author": "Kathleen Glasgow",
    "rating": "10"
    }
    update_book(API_KEY, updated_book)
    delete_book(API_KEY, '/5')
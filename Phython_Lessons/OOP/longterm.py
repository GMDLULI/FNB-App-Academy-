
# try:
#     f = open('text2.txt', 'w')
#     f.write('Hello, World!')
#     f.close()
# except FileNotFoundError as e:
#     print(f"Could not open file: {e.filename}")

# finally:
#     f = open('text3.txt', 'w')
#     f.write("the sky is blue")
#     f.close()


#Working with json files 


import json


try:
   with open('zoo.json', 'r') as ZA:
      zoo = json.load(ZA)
      print(zoo)
   with open('new_zoo.json', '') as new_zoo:
      json.dump(zoo, new_zoo, indent=4)
except FileNotFoundError as e:
    print(f"Could not open file: {e.filename}")

finally:
  pass
# Python program to get a set of
# places according to your search
# query using Google Places API

# importing required modules
import requests, json

# enter your api key here
api_key = 'AIzaSyACP3KKL5n-3aowlZOhQ5QBaOSrzyh3h7Q'

# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"


food_item = 'chicken biriyani'
city = 'jaffna'
country = 'sri lanka'
# The text string on which to search
query = f'{food_item} in {city} {country}'

# get method of requests module
# return response object
r = requests.get(url + 'query=' + query +
                 '&key=' + api_key)

# json method of response object convert
# json format data into python format data
x = r.json()
print(x['results'][0].keys())
# now x contains list of nested dictionaries
# we know dictionary contain key value pair
# store the value of result key in variable y
y = x['results']

# keep looping upto length of y
for i in range(len(y)):
    # Print value corresponding to the
    # 'name' key at the ith index of y
    #print(y[i]['name'], y[i]['rating'], y[i]['user_ratings_total'])
    print('\n')
    print(y[i])

import pickle
import streamlit as st
import requests
import pandas as pd
import numpy as np
import imdb


# def fetch_poster(poster_path):

#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

def getMovie(movie_id):
    movie_url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
 
    data = requests.get(movie_url)
    data = data.json() 
    # imdb_id = data["imdb_id"]
    title = data["original_title"]
    poster_path = "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    runtime = data["runtime"]
    overview = data["overview"]
    genres = []
    for i in data["genres"]:
        genres.append(i["name"])

    print("##############################################")

    # print(imdb_id = data["imdb_id"])
    print(data["vote_average"])

    print("##############################################")
    
    # print(data)

def casts(movie_id):

    casts_url = "https://api.themoviedb.org/3/movie/{}/credits?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)



    data = requests.get(casts_url)
    data = data.json() 
    cast = data["cast"]

    cast_ids = []
    
    for i in range(10):
        cast_ids.append(cast[i]['id'])
    return (cast_ids)

def actor(actor_id):
    actor_url = "https://api.themoviedb.org/3/person/{}?api_key=15d3cb7ab0eca84f881d16a6b8cd936c".format(actor_id)
   

    data = requests.get(actor_url)
    data = data.json() 
    # cast = data[""]
    # print(data)
    popularity = data["popularity"] 
    id = data["id"] 
    place_of_birth = data["place_of_birth"] 
    name = data["name"]
    gender = data["gender"]
    birthday = data["birthday"], 
    profile_path = "https://image.tmdb.org/t/p/w500/" + data["profile_path"]

    pdata = {
        "popularity": popularity, 
        "id": popularity, 
        "place_of_birth": place_of_birth, 
        "name": name, 
        "gender": gender, 
        "birthday": birthday, 
        "profile_path": profile_path
    }

    return pdata
    
    # for i in range(11):
    #     print(cast[i])

    


getMovie("49026")
castIds = casts("49026")
actorsDeatils = []
for mid in castIds:
    actorsDeatils.append(actor(mid))

print(actorsDeatils[0]['profile_path'])



# moviesDB = imdb.IMDb()
# movies = moviesDB.search_movie('The Dark Knight Rises')
# id = movies[0].getID()
# # print(id)
# movie = moviesDB.get_movie(id)
# print("####################################################################")
# print(type(movie))
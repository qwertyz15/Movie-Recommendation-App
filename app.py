from argparse import Action
from cgi import print_form
from faulthandler import disable
import pickle
from turtle import onclick

from click import style
import streamlit as st
# import SessionState
import requests
import pandas as pd
import numpy as np

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

df = pd.DataFrame(
np.random.randn(10, 5),
columns=('col %d' % i for i in range(5))
)

def getMovie(movie_id):
    movie_url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
 
    data = requests.get(movie_url)
    data = data.json() 
    # imdb_id = data["imdb_id"]
    title = data["original_title"]
    poster_path = "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    runtime = data["runtime"]
    overview = data["overview"]
    rating = data["vote_average"]
    genres = []
    for i in data["genres"]:
        genres.append(i["name"])
    
    return(title, poster_path, runtime, overview, genres, rating)

def fetch_poster(movie_id):
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        print(poster_path)
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        # print(full_path)
        # if(full_path == ):
        #     full_path =
    except:
        full_path = "https://source.unsplash.com/500x700/?black"
    return full_path

def getIndex(movie):
    index = movies[movies['title'] == movie]['movie_id'].values[0]
    return index


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:21]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('models/movie_list.pkl','rb'))
similarity = pickle.load(open('models/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


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
        





#########################################################
###########################################################
if st.button('Show Recommendation'):

    print(selected_movie)

    id = getIndex(selected_movie)
    print(id)
    title, poster_path, runtime, overview, genres, rating = getMovie(id)

    castIds = casts(id)
    actorsDeatils = []
    for mid in castIds:
        actorsDeatils.append(actor(mid))



    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)

    moviePosterColumn, movieOverviewColumn = st.columns(2)

    with moviePosterColumn:
        # st.text(recommended_movie_names[0])
        st.image(poster_path)
    with movieOverviewColumn:
        st.title(f"{title}")
        st.text(f"Runtime : {runtime} min")
        st.text(f"Overview : {overview}")
        st.text(f"Genres : {genres}")
        st.text(f"Ratings : {rating}")
    
    st.header("Top Casts")

    actor1, actor2, actor3, actor4, actor5, actor6, actor7, actor8, actor9, actor10 = st.columns(10)
    # actor4, actor5, actor6 = st.columns(3)
    # actor7, actor8, actor9 = st.columns(3)



    with actor1:
        st.image(actorsDeatils[0]["profile_path"])
        st.text(actorsDeatils[0]["name"])
    with actor2:
        st.image(actorsDeatils[1]["profile_path"])
        st.text(actorsDeatils[1]["name"])
    with actor3:
        st.image(actorsDeatils[2]["profile_path"])
        st.text(actorsDeatils[2]["name"])
    with actor4:
        st.image(actorsDeatils[3]["profile_path"])
        st.text(actorsDeatils[3]["name"])
    with actor5:
        st.image(actorsDeatils[4]["profile_path"])
        st.text(actorsDeatils[4]["name"])
    with actor6:
        st.image(actorsDeatils[5]["profile_path"])
        st.text(actorsDeatils[5]["name"])
    with actor7:
        st.image(actorsDeatils[6]["profile_path"])
        st.text(actorsDeatils[6]["name"])
    with actor8:
        st.image(actorsDeatils[7]["profile_path"])
        st.text(actorsDeatils[7]["name"])
    with actor9:
        st.image(actorsDeatils[8]["profile_path"])
        st.text(actorsDeatils[8]["name"])
    with actor10:
        st.image(actorsDeatils[9]["profile_path"])
        st.text(actorsDeatils[9]["name"])

    st.header("Top Recommendation")

    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    col11, col12, col13, col14, col15 = st.columns(5)
    col16, col17, col18, col19, col20 = st.columns(5)

    with col1:
        # st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        st.caption(recommended_movie_names[0])
    with col2:
        # st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        st.caption(recommended_movie_names[1])

    with col3:
        # st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        st.caption(recommended_movie_names[2])
    with col4:
        # st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        st.caption(recommended_movie_names[3])
    with col5:
        # st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        st.caption(recommended_movie_names[4])

    with col6:
        # st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
        st.caption(recommended_movie_names[5])
    with col7:
        # st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
        st.caption(recommended_movie_names[6])

    with col8:
        # st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
        st.caption(recommended_movie_names[7])
    with col9:
        # st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
        st.caption(recommended_movie_names[8])
    with col10:
        # st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
        st.caption(recommended_movie_names[9])


    with col11:
        # st.text(recommended_movie_names[10])
        st.image(recommended_movie_posters[10])
        st.caption(recommended_movie_names[10])
    with col12:
        # st.text(recommended_movie_names[11])
        st.image(recommended_movie_posters[11])
        st.caption(recommended_movie_names[11])

    with col13:
        # st.text(recommended_movie_names[12])
        st.image(recommended_movie_posters[12])
        st.caption(recommended_movie_names[12])
    with col14:
        # st.text(recommended_movie_names[13])
        st.image(recommended_movie_posters[13])
        st.caption(recommended_movie_names[13])
    with col15:
        st.text(recommended_movie_names[14])
        st.image(recommended_movie_posters[14])
        st.caption(recommended_movie_names[14])

    with col16:
        # st.text(recommended_movie_names[15])
        st.image(recommended_movie_posters[15])
        st.caption(recommended_movie_names[15])
    with col17:
        # st.text(recommended_movie_names[16])
        st.image(recommended_movie_posters[16])
        st.caption(recommended_movie_names[16])

    with col18:
        # st.text(recommended_movie_names[17])
        st.image(recommended_movie_posters[17])
        st.caption(recommended_movie_names[17])
    with col19:
        # st.text(recommended_movie_names[18])
        st.image(recommended_movie_posters[18])
        st.caption(recommended_movie_names[18])
    with col20:
        # st.text(recommended_movie_names[19])
        st.image(recommended_movie_posters[19])
        st.caption(recommended_movie_names[19])

###############################################################









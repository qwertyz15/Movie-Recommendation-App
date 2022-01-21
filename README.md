# Movie Recommendation App

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![API](https://img.shields.io/badge/API-TMDB-fcba03)


## How to get the API key?

Create an account in https://www.themoviedb.org/, click on the `API` link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your `API` sidebar once your request is approved.

## How to run the project?
1. Clone or download this repository to your local machine.
2. Create two empty folders named `/models` and `/datasets` in the same directory.
3. After that download the datasets from [here!](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv). and save the datasets in the `/datasets` direcotry.
4. Open your terminal/command prompt from your project directory and run the file `recommend.py` by executing the command `python3 recommend.py`.
5. Install all the libraries mentioned in the [requirements.txt](https://github.com/qwertyz15/Movie-Recommendation-App/blob/main/requirements.txt) file with the command `pip install -r requirements.txt`
6. Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key)
7. Then run the file `app.py` by executing the command `python3 app.py`.
8. After that run streamlit run app.py
9. Go to your browser and type `http://localhost:8501` in the address bar.
10. Hurray! That's it.


## Architecture

![IMG-20210306-WA0012](https://user-images.githubusercontent.com/36665975/110212434-597bb700-7ec1-11eb-9ffa-7ac319e33123.jpg)

## Similarity Score : 

   How does it decide which item is most similar to the item user likes? Here we use the similarity scores.
   
   It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.
   
## How Cosine Similarity works?
  Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
  
  ![image](https://user-images.githubusercontent.com/36665975/70401457-a7530680-1a55-11ea-9158-97d4e8515ca4.png)

  
More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)

### Sources of the datasets 

[IMDB 5000 Movie Dataset](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)


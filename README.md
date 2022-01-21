# Movie Recommendation App

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![API](https://img.shields.io/badge/API-TMDB-fcba03)


## How to get the API key?

Create an account in https://www.themoviedb.org/, click on the `API` link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your `API` sidebar once your request is approved.

## How to run the project?

1. Clone or download this repository to your local machine.
2. Install all the libraries mentioned in the [requirements.txt](https://github.com/qwertyz15/Movie-Recommendation-App/blob/main/requirements.txt) file with the command `pip install -r requirements.txt`
3. Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key)
3. Replace YOUR_API_KEY in **both** the places (line no. 15 and 29) of `static/recommend.js` file and hit save.
4. Open your terminal/command prompt from your project directory and run the file `app.py` by executing the command `python3 app.py`.
5. After that run streamlit run app.py
6. Go to your browser and type `http://localhost:8501` in the address bar.
7. Hurray! That's it.


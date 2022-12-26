# FLC-Movie-Review-Website


<p align="center"> 
 <img src="https://i.ibb.co/BPBGNG7/logo.png" alt="Bit-Movies-logo" border="0" width=300 height=300/>&nbsp; </a></p>


<p class="text-center mb-3" align="center">
<a href="#"><img src="https://forthebadge.com/images/badges/made-with-python.svg" border="0" title="Made with Python" /></a>
</p>

<p class="text-center mb-3" align="center">
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>
</p>

A Hackfest Project for Movie Reviews. Using this platform ‘Bit Movies’ user can get the information about any movie. User can search for a movie and also give reviews and rating. It allows people who are new to sign up and create a new account whereas people who already have existing accounts can sign in to get the information about a movie. Ratings from various other review websites like IMDB, Rotten Tomatoes and Metacritic are also available. Hence, the user can easily decide whether a movie is good or bad. User can also add the movies and web series to watchlist and watched categories. This will allow the user to search for a good movie.

1. Backend Framework: **Django**
2. Frontend Technologies: **HTML**, **CSS**, **Javascript**, **Bootstrap**


## Installation 

1. Fork and Clone
    <ol>
    <li>Fork the Repo</li>
    <li>Clone the repo to your computer.</li>
    </ol>

2. Create a Virtual Environment for the Project

    In Windows
    ```bash
    python -m venv env
    
    env\Scripts\activate
    ```

    In Ubuntu/MacOS
    ```bash
    python -m virtualenv env
    
    source env/bin/activate
    ```
   If you are giving a different name then `venv`, then please mention it in `.gitignore` file first

3. Install all the requirements

    ```bash
    pip install -r requirements.txt
    ```
4. Checkout to develop branch
     ```git
    git status
    git pull
    git branch
    git checkout develop
    
    ```

5. Make migrations/ Create db.sqlite3

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Create a super user.
    In django if you want to access admin page, you need to create an account first.
    ```djangotemplate
    python manage.py createsuperuser
    ```
   Then select your username and password.
7. Run server
    ```bash
    python manage.py runserver
    ```

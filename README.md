## [FLC-Movie-Review-Website](https://bit-movies-flc.up.railway.app/)


<p align="center"> 
 <img src="https://i.ibb.co/BPBGNG7/logo.png" alt="Bit-Movies-logo" border="0" width=300 height=300/>&nbsp; </a></p>


<p class="text-center mb-3" align="center">
<a href="https://ganeshpaih24.pythonanywhere.com/"><img src="https://forthebadge.com/images/badges/made-with-python.svg" border="0" title="Made with Python" /></a>
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
    
## Screenshots

- Landing Page
<img src="https://i.postimg.cc/BQWWSLH3/Screenshot-20221229-223010.png" alt="Landing Page">

- Login Page
<img src="https://i.ibb.co/R2TbP3q/Screenshot-20221229-203726.png" alt="Login Page">

- Register Page
<img src="https://i.postimg.cc/JzkCM7Dv/Screenshot-20221229-203753.png" alt="Register Page">

- Profile Page
<img src="https://i.postimg.cc/FHc8wPwQ/Screenshot-20221229-213527.png" alt="Profile Page">

- Edit Profile Page
<img src="https://i.postimg.cc/8P3g2f5L/Screenshot-20221229-213151.png" alt="Edit Profile Page">

- Search Results Page
<img src="https://i.postimg.cc/158LrRHX/Screenshot-20221229-213906.png" alt="Search Results Page">

- Movie Info Page
<img src="https://i.postimg.cc/8CgQ58L5/Screenshot-20221229-215119.png" alt="Movie Info Page">

- Ratings Page
<img src="https://i.postimg.cc/c46NkBss/Screenshot-20221229-215538.png" alt="Ratings Page">

- Display Review Page
<img src="https://i.postimg.cc/N0Rt7GQm/Screenshot-20221229-215158.png" alt="Review Page">

- Genre Page
<img src="https://i.postimg.cc/T1wBSTvk/Screenshot-20221229-215702.png" alt="Genre Page">

## Contributors
| <img src = "https://avatars.githubusercontent.com/u/91747440?v=4" width="50px"> | <img src = "https://avatars.githubusercontent.com/u/107351775?v=4" width="50px"> | <img src = "https://avatars.githubusercontent.com/u/109450989?v=4" width="50px"> | <img src = "https://avatars.githubusercontent.com/u/119883604?v=4" width="50px"> | <img src = "https://avatars.githubusercontent.com/u/119871841?v=4" width="50px"> | <img src = "https://avatars.githubusercontent.com/u/91683726?v=4" width="50px"> | <img src = "https://avatars.githubusercontent.com/u/106546916?v=4" width="50px"> | <img src = "https://avatars.githubusercontent.com/u/116286550?v=4" width="50px"> | <img src = "https://avatars.githubusercontent.com/u/119872202?v=4" width="50px"> | 
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | 
| [Ganesh](https://github.com/ganeshpaih24/) |  [Sharan](https://github.com/SharanShetty11/)   |  [Vandana](https://github.com/Vandanaprabhu7/)   |  [Saachi](https://github.com/SaachiSuvarna/)   |  [Sanjey](https://github.com/sanjeeey/)   |  [Deeksha](https://github.com/pai23deeksha/)   |  [Deepika](https://github.com/deepika-vk/)   |  [Pratham](https://github.com/12345prath/)   |  [Pavithra](https://github.com/pav-thra/)   |

## License
[Apache License 2.0](https://github.com/ganeshpaih24/flc-movie-review-website/blob/main/LICENSE)

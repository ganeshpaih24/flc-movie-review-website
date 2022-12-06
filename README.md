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

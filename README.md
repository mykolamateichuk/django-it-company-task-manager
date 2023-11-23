# IT Team Task Manager

## How to install


1) Clone repository into a desirable folder:

    ```
    git clone https://github.com/mykolamateichuk/django-it-company-task-manager.git
    ```

2) If you don't have **pip** installed  [install it here](https://pip.pypa.io/en/stable/installation/#).

3) Create and activate **Virtual environment**:
   
   **Windows**
   ```
   python -m venv venv
   
   source venv/Scripts/activate
   ```
   
   **MacOS**
   ```
   python3 -m venv venv
   
   source venv/bin/activate
   ```

4) Open cloned folder and install needed requirements using:

    ```
    pip install -r requirements.txt
    ```

5) Make migrations and migrate:

   ```
   python manage.py makemigrations
   
   python manage.py migrate
   ```

6) Install database fixture:

   ```
   python manage.py loaddata db_fixture.json
   ```

7) Run server:
   
   ```
   python manage.py runserver
   ```

8) Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


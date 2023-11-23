# IT Team Task Manager

## How to install

1) Open Terminal and open folder to clone project in.

2) Clone repository into a desirable folder:

    ```
    git clone https://github.com/mykolamateichuk/django-it-company-task-manager.git
    ```

3) If you don't have **pip** installed  [install it here](https://pip.pypa.io/en/stable/installation/#).

4) Create and activate **Virtual environment**:
   
   **Windows**
   ```
   python -m venv venv
   ```
   
   ```
   venv\Scripts\activate
   ```
   
   **MacOS**
   ```
   python3 -m venv venv
   ```
   
   ```
   source venv/bin/activate
   ```
   
5) Open cloned folder and install needed requirements using:

    ```
    pip install -r requirements.txt
    ```

6) Make migrations and migrate:

   ```
   python manage.py makemigrations
   ```
   ```
   python manage.py migrate
   ```

7) Install database fixture:

   ```
   python manage.py loaddata db_fixture.json
   ```

8) Run server:
   
   ```
   python manage.py runserver
   ```

9) Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


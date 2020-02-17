# Backend
## How to run
The main way to run the backend app is by by running the script `backend.py`.
The full list of necessary commands on win32. On other systems it should be similar:
```shell script
py -m venv venv
venv\Scripts\activate
pip install -r backend\requirements.txt
...
{ Set environment variables CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET }
...
py backend\backend.py
```

To run all the unit tests in one go you can set the environment variable `FLASK_APP=backend.py` and call
```shell script
flask test
```
## Configuration
The backend application can be started in test or development mode. You can specify the required mode by setting environment variable **FLASK_CONFIG** to `'development'` or `'testing'`. By default the application starts in development mode.

Running the application in development mode requires the following environment variables to be set:
* **CONSUMER_KEY** - Twitter application key
* **CONSUMER_SECRET** - Twitter application secret
* **ACCESS_TOKEN** - Twitter access token
* **ACCESS_TOKEN_SECRET** - Twitter access token secret
# Frontend
## How to run
```shell script
npm start
```
The application would be available on `http://localhost:3000/`

To run frontend unit tests call
```shell script
npm test
```
Though, at the moment, frontend has only one basic test.

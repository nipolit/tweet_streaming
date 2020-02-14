# Backend
## How to run
The main way to run the backend app is to set the environment variable `FLASK_APP=backend.py` and call
```shell script
flask run
```
To run all the unit tests you can use the command `test`:
```shell script
flask test
```
To debug some application error in an IDE you can start the application by running the script `backend.py`
## Configuration
The backend application can be started in test or development mode. You can specify the required mode by setting environment variable **FLASK_CONFIG** to `'development'` or `'testing'`. By default the application starts in development mode.

Running the application in development mode requires the following environment variables to be set:
* **CONSUMER_KEY** - Twitter application key
* **CONSUMER_SECRET** - Twitter application secret
* **ACCESS_TOKEN** - Twitter access token
* **ACCESS_TOKEN_SECRET** - Twitter access token secret

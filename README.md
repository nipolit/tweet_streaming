The backend application can be started in test or development mode. You can specify the required mode by setting environment variable **FLASK_CONFIG** to `'development'` or `'testing'`. By default the application starts in development mode.

Running the application in development mode requires the following environment variables to be set:
* **CONSUMER_KEY** - Twitter application key
* **CONSUMER_SECRET** - Twitter application secret
* **ACCESS_TOKEN** - Twitter access token
* **ACCESS_TOKEN_SECRET** - Twitter access token secret

# restAPI
type in terminal:
##### uvicorn main:app --reload
to run the server


# Authentication service
## auth.py
Handeling the authentication service as a whole. First we chose the encryption of a the password with the **pwd_context** variable. Next we are hashing the password of the user, when entered. For that we're using the JWT library. Also we've implemented a timeframe which checks if the given token is expired or not. If the token is expired the user is prompted with 401 error and a message indicating that the token is expired or in other case if the token is invalid, same status 401 code is raised but with the message indicating that the token is invalid.

## main.py
The register domain chechs wether the username is already in the database(in this case the list variable **users**) if not the user is added to the list of users. Login domain is handeling the initial login with the checking of the token. If the entered credentials are incorrect the status code 401 is raised with a message indicating that the given credential are incorrect.


## models.py
Models serves as a blueprint for the users and the roles that can be asigned.
We use a **User** class for the base information for the API and the class **Role** for the individual asigned role.
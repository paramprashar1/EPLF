import pyrebase
from getpass import getpass

firebaseConfig={

    "apiKey": "AIzaSyAkaasJWZxzFEDVsFJ45FLlb3LnReSSrew",
    "authDomain": "loadforecasttiet.firebaseapp.com",
    "databaseURL": "https://loadforecasttiet.firebaseio.com",
    "projectId": "loadforecasttiet",
    "storageBucket": "loadforecasttiet.appspot.com",
    "messagingSenderId": "736359693726",
    "appId": "1:736359693726:web:554d663d1eca05bbfaea8f",
    "measurementId": "G-6K0LG0DE8Y"
}







firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
#
email = input("Please enter your email address: \n")
password = getpass("Please enter your password: \n")
#
# user = auth.create_user_with_email_and_password(email, password)
# auth.send_email_verification(user['idToken'])
login = auth.sign_in_with_email_and_password(email, password)
print(login)

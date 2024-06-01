import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import firestore

# load environment variables
load_dotenv()

# initialise firebase app
cred = firebase_admin.credentials.Certificate(os.getenv("FIREBASE_CRED"))
firebase_admin.initialize_app(cred)

# intialise firestore
db = firestore.client()
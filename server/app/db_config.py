import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore, storage

load_dotenv()

# initialise firebase with cloud storage
cred = credentials.Certificate(os.getenv("FIREBASE_CRED"))
firebase_admin.initialize_app(cred, {'storageBucket':os.getenv('FIREBASE_STORAGE')})

db = firestore.client()
bucket = storage.bucket()

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate("talaley-2de4c-firebase-adminsdk-ux0s6-8d8f0c7058.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://talaley-2de4c.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('')

hopper_ref = ref.child('users/-M3eeHUTYiRqzkb6V_CC')
hopper_ref.delete()

print(ref.get())
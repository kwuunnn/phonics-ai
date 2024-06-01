from fastapi import APIRouter, Request
from firebase_db import db

router = APIRouter()

@router.get("/user_exists/{email}")
async def user_exists(email):
    doc_ref = db.collection("users").document(email)
    doc = doc_ref.get()
    if doc.exists:
        doc_json = doc.to_dict()
        print(doc_json)
        return doc_json
    else:
        return {"message":"no such user"}
    
@router.post("/user_create/")
async def user_create(request: Request):
    """
    data = {
            'username':...,
            'email':...,
            'password':...,
            'pin':...
            }
    """
    data = await request.json()
    username = data['username']
    email = data['email']
    password = data['password']
    pin = data['pin']
    to_add= {
            "username":username,
            "email":email,
            "password":password,
            "pin":pin
            }
    doc_ref = db.collection("users").document(email)
    doc = doc_ref.get()
    if doc.exists:
        return {"message":"user already exists"}
    else:
        db.collection("users").document(email).set(to_add)
        # set placeholder document for kids collection
        db.collection("users").document(email).collection("kids").document("placeholder").set({})
        return {"message":"user created"}

@router.get("/user_getkids/{email}")
async def user_getkids(email):
    all_kids = db.collection("users").document(email).collection("kids").stream()
    kids_list = []
    for kid in all_kids:
        if kid.id != "placeholder":
            kids_list.append(kid.to_dict())
    if len(kids_list)==0:
        return {"message":"no kids"}
    else:
        return {'kids':kids_list}
    
@router.post("/user_addkid/")
async def user_addkid(request: Request):
    """
    {
    'email':...,
    'name':...,
    'age':...,
    'school':...
    }
    """
    data = await request.json()
    email = data['email']
    name = data['name']
    age = data['age']
    school = data['school']
    to_add= {
            'name':name,
            'age':age,
            'school':school   
            }
    db.collection("users").document(email).collection("kids").document(name).set(to_add)
    # set placeholder for learning progress (?)
    return {"message":"kid added"}
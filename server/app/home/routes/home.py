from fastapi import APIRouter, Request
from db_config import db

router = APIRouter()

@router.get("/auth")
async def user_auth(request: Request):
    """
    data = {
            'email':...,
            'password':...
            }
    """
    data = await request.json()
    email = data['email']
    password = data['password']
    doc_ref = db.collection("users").document(email)
    doc = doc_ref.get()
    if doc.exists:
        doc_json = doc.to_dict()
        if doc_json['password'] == password:
            doc_json['message'] = "user exists"
            return doc_json
        else:
            return {'message':'wrong password'}
    else:
        return {"message":"no such user"}
    
@router.post("/create_user")
async def user_create(request: Request):
    """
    data = {
            'username':...,
            'email':...,
            'password':...,
            }
    """
    data = await request.json()
    username = data['username']
    email = data['email']
    password = data['password']
    to_add= {
            "username":username,
            "email":email,
            "password":password,
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
        return {'message':'kids returned', 'kids':kids_list}
    
@router.post("/user_addkid")
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
    doc_ref = db.collection("users").document(email).collection("kids").document(name)
    doc = doc_ref.get()
    if doc.exists:
        return {'message':'kid already exists'}
    else:
        doc_ref.set(to_add)
        # set placeholder for learning progress (?)
        return {"message":"kid added"}
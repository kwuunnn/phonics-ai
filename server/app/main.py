from fastapi import FastAPI
import uvicorn
from routes.home import router as home_router

app = FastAPI()

##### include routers here #####
app.include_router(home_router, prefix='/home')

##############################

##### run main app with all routers #####
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
##############################

"""
uvicorn main:app --reload
"""
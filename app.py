from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

storedData = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"Message": "use '/docs' endpoint to find all the api related docs "}


@app.post("/post-data/{data}")
def postData(data):
    try:
        storedData.append(data)
        return {"inserted": "true"}

    except:
        return {"inserted": "false"}


@app.get("/get-all-data")
def getData():
    return storedData

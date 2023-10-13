import uvicorn
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/hello")
async def read_hello(authorization: str = Header(...), token: str = Depends(oauth2_scheme)):
    return {"tanh": "Hello World!", "authorization": authorization, "token": token}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=1957)

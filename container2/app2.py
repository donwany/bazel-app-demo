from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import uvicorn


app = FastAPI()

bearer_scheme = HTTPBearer()


@app.get("/goodbye")
async def read_goodbye(authorization: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    return {"tanh": "Goodbye World!", "authorization": authorization}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=1958)
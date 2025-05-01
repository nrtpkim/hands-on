from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    res = os.getenv("TEST_ENV", default="Hello, World!")
    return {"message": res}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
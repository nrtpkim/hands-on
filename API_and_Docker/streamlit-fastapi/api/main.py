from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "Hello World"}

# Define the expected request body structure
class Txt(BaseModel):
    bot_name : str = "SIRI"
    text_payload: str

@app.post("/cate")
def sum(txt:Txt):

    if txt.text_payload == "cat":
        voice = "Meaw Meaw Meaw"
    elif txt.text_payload == "dog":
        voice = "woof!"
    else:
        voice = "I dont't know"

    return {"msg": f"{txt.bot_name} said :{voice}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
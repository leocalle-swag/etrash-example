from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from tqdm import tqdm
from time import sleep

app = FastAPI()

@app.get("/api_get")
def api_get():
    print("API_GET")
    return JSONResponse(content={"value": 2})



@app.post("/api_post")
async def api_post(request: Request):
    print("API_POST")
    print("aziono il servomotore" )
    data=(await request.json())
    print("ho ricevuto::", data["ripartizione_del_cestino"])
    for i in tqdm(range(10)):
        sleep(0.5)

    return JSONResponse(content={"servo_appena_azionato": "OK"})
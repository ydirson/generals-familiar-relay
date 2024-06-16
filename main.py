import http.client

from fastapi import FastAPI, Response

app = FastAPI()

HOST = 'army-forge.onepagerules.com'
JSON = "application/json"

@app.get("/")
def get_root():
    return {"Version": "0.0.1"}

@app.get("/opr/api/rules/common/{id}")
def get_commonrules(id: str):
    conn = http.client.HTTPSConnection(HOST)
    conn.request("GET", f"/api/rules/common/{id}", headers={"Host": HOST})
    response = conn.getresponse()
    if response.status < 200 or response.status >= 300:
        return response

    data = response.read()
    response = None
    conn.close()

    my_response = Response(content=data, media_type=JSON)
    my_response.headers["Access-Control-Allow-Origin"] = "*"
    return my_response

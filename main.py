import http.client

from fastapi import FastAPI, Request, Response

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address, default_limits=["5/minute"])
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

HOST = 'army-forge.onepagerules.com'
JSON = "application/json"

@app.get("/")
@limiter.limit("2/minute")
def get_root(request: Request):
    return {"Version": "0.0.3"}

@app.get("/opr/api/rules/common/{id}")
def get_commonrules(request: Request, id: str):
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

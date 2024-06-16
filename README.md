## A web proxy for select web API

The [General's Familiar](https://github.com/ydirson/generals-familiar)
project needs to access some APIs of [OPR Army
Forge](https://army-forge.onepagerules.com/) which, despite being
accessible from the AF app's in-browser code, are blocked by said
browser because of some missing CORS headers.

This small web service relays request to those specific endpoints, to
make it possible to present the information in different ways.

It aims to be kept minimal.

## Technical details

It is written in python, using the
[FastAPI](https://fastapi.tiangolo.com/) framework.

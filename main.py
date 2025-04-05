from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response

app = FastAPI()

@app.api_route("/", methods=["GET", "HEAD"])
async def root(request: Request):
    if request.method == "HEAD":
        return Response(status_code=200)
    return JSONResponse(content={"mensagem": "API do Dashboard Paulo funcionando!"})

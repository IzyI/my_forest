from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fastapi.middleware.gzip import GZipMiddleware
from settings import VERSION

from app.views import router
from starlette.middleware.cors import CORSMiddleware


def get_application() -> FastAPI:
    node = FastAPI()
    node.add_middleware(GZipMiddleware, minimum_size=1000)
    node.add_middleware(
        CORSMiddleware,
        allow_origins=[],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @node.get("/ping", tags=["check"])
    def ping():
        return JSONResponse({"result": "pong"})

    @node.get("/version", tags=["version"])
    def version():
        return JSONResponse({"version": VERSION})

    node.include_router(router)
    return node


app = get_application()

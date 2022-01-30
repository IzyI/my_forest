from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.gzip import GZipMiddleware
from settings import VERSION
from app.views import router
from starlette.middleware.cors import CORSMiddleware
import secrets
from settings import USERNAME, PASSWORD
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.staticfiles import StaticFiles

def get_application() -> FastAPI:
    node = FastAPI()
    security = HTTPBasic()

    def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
        correct_username = secrets.compare_digest(credentials.username, USERNAME)
        correct_password = secrets.compare_digest(credentials.password, PASSWORD)
        if not (correct_username and correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return credentials.username

    node.add_middleware(GZipMiddleware, minimum_size=1000)
    node.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # @node.middleware("http")
    # async def add_process_time_header(request: Request, call_next):
    #     start_time = time.time()
    #     response = await call_next(request)
    #     process_time = time.time() - start_time
    #     response.headers["X-Process-Time"] = str(process_time)
    #     return response

    # @node.get("/", tags=["html"], )
    # def html():
    #     return JSONResponse({"result": "pong"})
    #
    #
    # node.mount("/css", StaticFiles(directory="front/dist/css"), name="static")


    @node.get("/ping", tags=["check"], )
    def ping():
        return JSONResponse({"result": "pong"})

    @node.get("/version", tags=["version"], )
    def version():
        return JSONResponse({"version": VERSION})

    node.include_router(router, dependencies=[Depends(get_current_username)])

    node.mount("/", StaticFiles(directory="/root/my_forest/front/dist", html=True), name="static")
    node.mount("/js", StaticFiles(directory="/root/my_forest/front/dist/js", html=True), name="js")
    node.mount("/css", StaticFiles(directory="/root/my_forest/front/dist/css", html=True), name="css")
    return node


app = get_application()

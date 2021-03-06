from fastapi import FastAPI
import uvicorn

import router


def app():
    app = FastAPI()

    app.include_router(router.router)

    return app


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8080, reload=True, debug=True)
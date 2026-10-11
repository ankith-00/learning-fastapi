from fastapi import FastAPI, status, Header, Cookie

app = FastAPI()


@app.get("/products", status_code=status.HTTP_200_OK)
def get_products():
    return {
        "message": "Products fetched successfully"
    }


# @app.get("/profile")
# def get_profile(user_name: str = Header()):
#     return { "browser_info": user_name}


@app.get("/profile")
def get_profile(session_id: str | None = Cookie(default=None)):
    return {
        "session_id": session_id
    }
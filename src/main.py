from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from src.routers.products_router import router as product_router
from src.routers.seller_router import router as seller_router
from src.routers.login_router import router as login_router

app = FastAPI(
    title="Products API",
    description="Get details for all the products",
    terms_of_service="http://www.google.com",
    contact={
        "Developer name": "Sohanur Rahman",
        "email": "sohanur.it@gmail.com",
    },
    license_info={
        "name": "xyz",
        "url":"http://www.google.com"

    }
)

origins = [
    "http://localhost:3000",
    # Add other allowed origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router, tags=['Product'])
app.include_router(seller_router, tags=['Seller'])
app.include_router(login_router, tags=['Login'])

@app.get("/")
def index():
    return {"message": "this is fastapi app"}

def start():
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()
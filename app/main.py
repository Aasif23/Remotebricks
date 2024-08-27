from fastapi import FastAPI
from routes import auth, id_linking, joins, chain_delete

# Initialize FastAPI app
app = FastAPI()

# Include routers from different modules
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(id_linking.router, prefix="/id", tags=["ID Linking"])
app.include_router(joins.router, prefix="/joins", tags=["Joins"])
app.include_router(chain_delete.router, prefix="/delete", tags=["Chain Delete"])

# Entry point to run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

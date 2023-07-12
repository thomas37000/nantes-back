from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.asgi import GraphQL
from listParc import Query as ParcQuery
from listPiscines import Query as PiscinesQuery

@strawberry.type
class Query(ParcQuery, PiscinesQuery):
    pass

schema = strawberry.Schema(query=Query)

# schema = strawberry.Schema(query=Query)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {
        "message": "Bienvenue à Nantes, venez vous ballader dans nos nombreux parcs"
    }


app.add_route("/graphql", GraphQL(schema, debug=True))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

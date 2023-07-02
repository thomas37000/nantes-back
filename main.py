from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from listParc import Query
# from listSkateparks import Query as SkateparkQuery

# @strawberry.type
# class Query(ParcQuery, SkateparkQuery):
#     pass

# schema = strawberry.Schema(query=Query)

schema = strawberry.Schema(query=Query)
app = FastAPI()


@app.get("/")
def index():
    return {
        "message": "Bienvenue à Nantes, venez vous ballader dans nos nombreux parcs"
    }


app.add_route("/graphql", GraphQL(schema, debug=True))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

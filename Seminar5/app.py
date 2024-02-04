from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str

movies = [
    Movie(id=1, title="Movie 1", description="Description 1", genre="Action"),
    Movie(id=2, title="Movie 2", description="Description 2", genre="Comedy"),
    # Добавьте еще фильмы по мере необходимости
]

@app.get("/movies/", response_model=List[Movie])
async def get_movies_by_genre(genre: str = Query(..., title="Жанр")):
    return [movie for movie in movies if movie.genre == genre]

@app.post("/movies/", response_model=Movie)
async def create_movie(movie: Movie):
    movies.append(movie)
    return movie

@app.put("/movies/{movie_id}/", response_model=Movie)
async def update_movie(movie_id: int, updated_movie: Movie):
    for i, movie in enumerate(movies):
        if movie.id == movie_id:
            movies[i] = updated_movie
            return updated_movie
    raise HTTPException(status_code=404, detail="Фильм не найден")

@app.delete("/movies/{movie_id}/", response_model=Movie)
async def delete_movie(movie_id: int):
    for i, movie in enumerate(movies):
        if movie.id == movie_id:
            deleted_movie = movies.pop(i)
            return deleted_movie
    raise HTTPException(status_code=404, detail="Фильм не найден")

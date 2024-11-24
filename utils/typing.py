from typing import List, Optional, TypedDict


class Movie(TypedDict):
    title: str
    description: str
    genres: str
    uuid: str


class MoviesResponse(TypedDict):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Movie]

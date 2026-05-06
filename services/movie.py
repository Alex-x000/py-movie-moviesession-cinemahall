from db.models import Movie
from django.db.models import QuerySet


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids is None and actors_ids is None:
        return queryset
    elif genres_ids and actors_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
        queryset = queryset.filter(actors__id__in=actors_ids)
        return queryset
    elif genres_ids and actors_ids is None:
        queryset = queryset.filter(genres__id__in=genres_ids)
        return queryset
    elif actors_ids and genres_ids is None:
        queryset = queryset.filter(actors__id__in=actors_ids)
        return queryset


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> Movie:
    created_movie = Movie.objects.create(title=movie_title,
                                         description=movie_description)

    if genres_ids:
        created_movie.genres.set(actors_ids)
    if actors_ids:
        created_movie.actors.set(actors_ids)
    return created_movie

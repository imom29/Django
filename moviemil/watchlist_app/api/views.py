from django.http import JsonResponse
from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)

    return JsonResponse(serializer.data, safe=False)


def get_movie_by_id(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    serializer = MovieSerializer(movie)

    return JsonResponse(serializer.data)

# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse


# def movie_list(request):
#     movies = Movie.objects.all()
#     return JsonResponse({
#         'data': list(movies.values()),
#     })


# def get_movie_by_id(request, movie_id):
#     movie = Movie.objects.get(pk=movie_id)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }

#     return JsonResponse({'data': data})

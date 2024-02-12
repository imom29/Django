from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.api.serializers import StreamPlatformSerializer, WatchlistSerializer, ReviewsSerializer
from watchlist_app.models import StreamPlatform as StreamPlatformModel
from watchlist_app.models import Watchlist as WatchlistModel
from watchlist_app.models import Reviews as ReviewsModel


@api_view(["GET", "POST"])
def Watchlist(request):
    if request.method == "GET":
        watchlist = WatchlistModel.objects.all()
        serializer = WatchlistSerializer(watchlist, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def get_watchlist_by_id(request, watch_id):
    try:
        watchlist = WatchlistModel.objects.get(pk=watch_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = WatchlistSerializer(watchlist)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = WatchlistSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def Platforms(request):
    if request.method == "GET":
        platforms = StreamPlatformModel.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def get_platform_by_id(request, watch_id):
    try:
        platform = StreamPlatformModel.objects.get(pk=watch_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def get_all_reviews(request):
    reviews = ReviewsModel.objects.all()
    serializer = ReviewsSerializer(reviews, many=True)
    count = ReviewsModel.objects.count()
    print(count)
    response_data = {
        'data': serializer.data,
        'count': count
    }
    return Response(data = response_data)

@api_view(['GET', 'POST'])
def get_reviews_for_watchlist(request, watch_id):
    if request.method == 'GET':
        reviews = ReviewsModel.objects.filter(watchlist = watch_id)
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        review_to_add = request.data
        review_to_add["watchlist"] = watch_id        
        serializer = ReviewsSerializer(data = review_to_add)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

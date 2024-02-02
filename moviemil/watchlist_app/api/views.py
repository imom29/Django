from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.api.serializers import StreamPlatformSerializer, WatchlistSerializer
from watchlist_app.models import StreamPlatform as StreamPlatformModel
from watchlist_app.models import Watchlist as WatchlistModel


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

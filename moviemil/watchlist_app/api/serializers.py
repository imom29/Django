from rest_framework import serializers
from watchlist_app.models import StreamPlatform, Watchlist, Reviews


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = "__all__"
        read_only_fields = ["id"]

        def validate(self, data):
            if data["title"] == data["storyline"]:
                raise serializers.ValidationError("Title and Storyline should be different")
            return data


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        read_only_fields = ["id"]

        def validate(self, data):
            if data["name"] == data["description"]:
                raise serializers.ValidationError("Name and description should be different")
            return data


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"
        read_only_fields = ["id"]

        def validate(self, data):
            if(data['rating'] < 0 or data['rating'] > 5):
                raise serializers.ValidationError("Rating should be between 0 and 5")
            
            return data

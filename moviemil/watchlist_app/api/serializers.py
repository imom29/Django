from rest_framework import serializers
from watchlist_app.models import StreamPlatform, Watchlist


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = "__all__"
        read_only_fields = ["id"]

        def validate(self, data):
            if data["title"] == data["storyline"]:
                raise serializers.ValidationError("Title and Storyline should be different")
            return data


# class WatchlistSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     storyline = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Watchlist.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.storyline = validated_data.get(
#             'storyline', instance.storyline)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        read_only_fields = ["id"]

        def validate(self, data):
            if data["name"] == data["description"]:
                raise serializers.ValidationError("Name and description should be different")
            return data


# def description_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError('Description is too short')


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[description_length])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def delete(self, instance):
#         instance.delete()

#     def validate(self, data):
#         # Object Level Validation
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 "Name and description should be different")
#         return data

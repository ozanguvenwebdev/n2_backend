from rest_framework import serializers
from api.models import *

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ['lat','lng']


class AddressSerializer(serializers.Serializer):

    street = serializers.CharField(max_length=255)
    suite = serializers.CharField(max_length=150)
    city = serializers.CharField(max_length=255)
    zipcode = serializers.CharField(max_length=255)
    geo = GeoSerializer()


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name',]



class UserSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    address = AddressSerializer()
    phone = serializers.CharField(max_length=20)
    website = serializers.URLField()
    company = CompanySerializer()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.website = validated_data.get('website', instance.website)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance




class PostSerializer(serializers.Serializer):

    userId = UserSerializer()
    title = serializers.CharField(max_length=150)
    body = serializers.CharField(min_length=0)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userId = validated_data.get('userId', instance.userId)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance



class CommentSerializer(serializers.Serializer):

    postId = PostSerializer()
    title = serializers.CharField(max_length=150)
    body = serializers.CharField(min_length=0)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.postId = validated_data.get('postId', instance.postId)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance




class AlbumSerializer(serializers.Serializer):

    userId = UserSerializer()
    title = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userId = validated_data.get('userId', instance.userId)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
        



class PhotoSerializer(serializers.Serializer):

    albumId = AlbumSerializer()
    title = serializers.CharField(max_length=150)
    url = serializers.URLField()
    thumbnailUrl = serializers.URLField()

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.albumId = validated_data.get('albumId', instance.albumId)
        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('url', instance.url)
        instance.thumbnailUrl = validated_data.get('thumbnailUrl', instance.thumbnailUrl)
        instance.save()
        return instance




class TodoSerializer(serializers.Serializer):

    userId = UserSerializer()
    title = serializers.CharField(max_length=150)
    completed = serializers.BooleanField()

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userId = validated_data.get('userId', instance.userId)
        instance.title = validated_data.get('title', instance.title)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance
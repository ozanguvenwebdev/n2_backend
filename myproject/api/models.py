from django.db import models

# Create your models here.

class Geo(models.Model):

    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return str(self.id)

class Company(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Address(models.Model):

    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    geo = models.ForeignKey(Geo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.street




class User(models.Model):

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    website = models.URLField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Post(models.Model):

    userId = models.ForeignKey('User', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title




class Album(models.Model):

    userId = models.ForeignKey('User', on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title




class Todo(models.Model):

    userId = models.ForeignKey('User', on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title




class Comment(models.Model):

    postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name




class Photo(models.Model):

    albumId = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='photos') 
    title = models.CharField(max_length=255)
    url = models.URLField() 
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title




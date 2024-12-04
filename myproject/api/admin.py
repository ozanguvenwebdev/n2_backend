from django.contrib import admin
from api.models import *
# Register your models here.

@admin.register(Geo)
class GeoAdmin(admin.ModelAdmin):
    list_display = ('lat','lng',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'phone', 'website')
    search_fields = ('name', 'username', 'email')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'zipcode')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('userId', 'title')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('postId','name','email')
    
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('albumId','title','url')
    
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('userId','title','completed')
    
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('userId','title',)
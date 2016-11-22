from django.contrib import admin


from api.models import Category, Piece, Artist, Collection,NewsFeed


# Register your models here.

admin.site.register(Category)
admin.site.register(Piece)
admin.site.register(Collection)
admin.site.register(Artist)
admin.site.register(NewsFeed)
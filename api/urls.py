from django.conf.urls import url

from api.resources.artist_resource import create_artist
from api.resources.awsS3_resource import getCredentials
from api.resources.category_resource import category_list
from api.resources.collection_resource import *
from api.resources.pieces_resource import *
from api.resources.user_resource import login_view, logout_view, is_logged

urlpatterns = [
    url(r'^createArtist/$', create_artist, name='create_artist'),
    url(r'^logout$', logout_view, name="logout"),
    url(r'^login/$', login_view, name="login"),
    url(r'^islogged$', is_logged, name="is_logged"),
    url(r'^category/$', category_list, name='category_list'),
    url(r'^credentials/$', getCredentials, name='getCredentials'),

    # pieces
    url(r'^pieces/$', pieces_list, name='pieces_list'),
    url(r'^pieces/(?P<piece_id>\d+)/$', piece_by_id, name='piece_by_id'),
    url(r'^pieces/update$', update_piece, name='update_piece'),
    url(r'^pieces/add_piece/$', add_piece, name='add_piece'),

    # collections
    url(r'^collections/create$', create_collection, name='create_collection'),
    url(r'^collections/$', collections_list, name='collections_list'),
    url(r'^collections/delete$', collections_delete, name='collections_delete'),
    url(r'^collections/add$', collections_add, name='collections_add'),
    url(r'^collections/(?P<collection_id>\d+)/pieces$', collections_pieces, name='collections_pieces'),
    url(r'^collections/(?P<collection_id>\d+)/delete$', collection_delete_by_id, name='collection_delete_by_id'),
    url(r'^collections/(?P<collection_id>\d+)/update$', update_collection, name='update_collection'),

    # likes
    url(r'^pieces/(?P<piece_id>\d+)/like$', like_piece, name='like_piece'),
    url(r'^pieces/(?P<piece_id>\d+)/unlike$', unlike_piece, name='unlike_piece'),
    url(r'^pieces/(?P<piece_id>\d+)/liked$', is_liked_piece_by_username, name='is_liked_piece_by_username'),
    url(r'^pieces/(?P<piece_id>\d+)/likes$', likes_by_piece, name='likes_by_piece'),
    url(r'^pieces/rank$', get_most_voted, name='get_most_voted'),
]
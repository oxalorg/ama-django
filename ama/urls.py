from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.ama_index, name='ama_index'),
    url(r'^(?P<ama_id>[0-9]+)/', include([
        url(r'^$', views.ama_post, name='ama_post'),
        url(r'^reply/$', views.CommentCreate.as_view(), name='ama_comment_add'),
        url(r'^reply/(?P<cmt_id>[0-9]+)/$', views.CommentCreate.as_view(), name='ama_comment_add'),
    ])),
]

"""myproject URL Configuration

"""
from django.contrib import admin
from django.urls import path, re_path, include

from accounts import views as accounts_views
from boards import views

urlpatterns = [
    re_path(r'^$', views.BoardListView.as_view(), name='home'),
    re_path(r'^signup/$', accounts_views.signup, name='signup'),
    re_path(r'^', include("django.contrib.auth.urls")),
    re_path(r'^boards/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
    re_path(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='edit_post'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    re_path(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    path('admin/', admin.site.urls)
]

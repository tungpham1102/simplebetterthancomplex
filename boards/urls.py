from django.conf.urls import url
from . import views

app_name = 'boards'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^boards/(?P<pk>\d+)/topic/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topic/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
]
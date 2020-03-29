from django.conf.urls import url
from . import views

app_name = 'boards'

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^$', views.BoardListView.as_view(), name='home'),
    # url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    # url(r'^boards/(?P<pk>\d+)/topic/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topic/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
]
urlpatterns +=[
    url(r'^new_post/$', views.NewPostView.as_view(), name='new_post'),
    url(r'^boards/(?P<pk>\d+)/topic/(?P<topic_pk>\d+)/post/(?P<post_pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='edit_post'),
    url(r'^boards/(?P<pk>\d+)/$',views.TopicListView.as_view(), name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/topic/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
]
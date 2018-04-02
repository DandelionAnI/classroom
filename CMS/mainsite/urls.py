from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.roomSearch, name="roomSearch"),
    url(r'^teacherSearch', views.teacherSearch, name="teacherSearch"),
    url(r'^courseSearch', views.courseSearch, name="courseSearch"),
    url(r'^emptyRoomSearch', views.emptyRoomSearch, name="emptyRoomSearch"),
    url(r'^roomBorrow', views.roomBorrow, name="roomBorrow"),
]

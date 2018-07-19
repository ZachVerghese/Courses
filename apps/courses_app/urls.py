from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),   
    url(r'^add$',views.add),
    url(r'^destroy/(?P<course_id>\d+)$', views.destroy),
    url(r'^delete/(?P<course_id>\d+)$',views.delete)
]                           

# 1. home page 
# 2. process that creaets new course
# 3. page that asks if can delete
# 4. process that deletes
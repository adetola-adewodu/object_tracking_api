from django.conf.urls import url
from object_locations import views

urlpatterns = [
    url(r'^blocks/$', views.block_list),
    url(r'^blocks/latest/$', views.latest_block_list),
    url(r'^blocks/updated/$', views.get_latest_block),
    url(r'^blocks/delete/$', views.delete_all_blocks),
]
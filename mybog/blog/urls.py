from django.urls import path ,re_path
# django最新版url  path默认不支持正则，如果需要使用正则，需要导入：re_path，
# re_path(r'^test-(\d+)-(\d+)/', views.test),
from . import views
urlpatterns = [
    path('',views.index),  # http://127.0.0.1:8000/
    path('index/',views.index ),  # http://127.0.0.1:8000/blog/index/  最后的 / 可加可不加
    path('blog/', views.index),

    # re_path(r'^$',views.index),   # 默认不输入
    re_path(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name = 'article_page' ),
    re_path(r'edit/(?P<article_id>[0-9]+)$',views.edit_page ,name = 'edit_page'),
    path('edit/action',views.action_page , name = 'edit_action'),
]
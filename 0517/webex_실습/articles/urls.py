from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    # 전체조회, 생성, 
    # 추가적인 article 정보가 필요하지 않다
    # api/v1/articles/
    path('', views.article_list_or_create),


    # 상세조회, 수정 , 삭제
    # 추가적인 article 정보 ("pk")가 필요하다
    # api/v1/articles/<int:article_pk>/
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),

    #좋아요
    # api/v1/articles/
    path('<int:article_pk>/likes/', views.like_article)
]
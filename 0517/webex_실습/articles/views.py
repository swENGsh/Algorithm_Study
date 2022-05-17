from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from django.db.models import Count
from .serializers.article import ArticleSerializer,ArticleListSerializer
from .models import Article,Comment
# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_list_or_create(request):

    def article_list():
        # articles = get_list_or_404(Article)
        articles = Article.objects.annotate(
            comment_count=Count('comments', distinct=True),
            like_count=Count('like_users', distinct=True)
        ).order_by('-pk')



        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    def article_create():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method =='GET':
        return article_list()
    elif request.method =='POST':
        return article_create()

@api_view(['GET','PUT','DELETE'])
def article_detail_or_update_or_delete(request,article_pk):
    
    def article_detail():
        pass

    def delete_article():
        pass
    
    if request.method =='GET':
        return article_detail()
    elif request.method =='PUT':
        pass
    elif request.method =='DELETE':
        return delete_article()

@api_view(['POST'])
def like_article(request,article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)

    #user가 article.like_users에 있는지 확인하기 (toggling) 혹은 article이 user.like_articles에 있는지 확인하기
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)
    
    serializer = ArticleSerializer(article)

    return Response(serializer.data)
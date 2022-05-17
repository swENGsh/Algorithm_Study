from rest_framework import serializers
from ..models import Article
from django.contrib.auth import get_user_model

# 전체 조회 ==> 어떤 내용을 응답으로 줄 것인가?
User = get_user_model()
class ArticleListSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk','username')
    user = UserSerializer(read_only=True)
    # comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count')
    # like_users = UserSerializer(read_only=True, many=True)


    class Meta:
        model = Article
        #역참조는 default로 나오지 않음(정의되어있더라도 all에 나오지 않습니다)
        # 그래서 fields에 따로 지정해주어야 합니다.
        fields = ('pk','title','comments','user','like_users')
        # 만약 read_only_fields 를 사용할 때, 위에 user처럼 재정의를 한 경우에는 read_only_fields에 사용하면 안된다! 안됨!



# 상세조회 => 응답으로 어떤 걸 줄 것인가?(필요 없는 건 뺄 것인가?) 생성, 수정(Foriegn key 등은 빼야겠지(나중에 추가해야 하는 것))
class ArticleSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk','username')

    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        #생성 할 때에는 pk와 user는 필요하지 않다. title하고 content만 있으면 된다 (validation 체크할 때)
        # fields = ('pk', 'title', 'content', 'user')
        fields = ('pk','title', 'content','like_users')
        # read_only_fields = ('user',)
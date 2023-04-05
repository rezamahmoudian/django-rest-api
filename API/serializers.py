from rest_framework import serializers
from .models import Course, Article
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class AuthorSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "first_name", "last_name", "email")


class CourseSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class ArticleSerializers(serializers.ModelSerializer):
    # همه ی اطلاعات کاربر انتخاب شده در سریالایزر را نمایش میدهد
    # author = AuthorSerializers()

    # این برای نمایش فیلد های چندتایی است و چون نویسنده هر مقاله یکنفر است نمیتوان از ان استفاده کرد
    # author = serializers.HyperlinkedRelatedField(many=True,
    #                                              read_only=True,
    #                                              lookup_field='pk',
    #                                              view_name='api:author-detail')
    # بعنوان کلید در url به اشتباه آیدی مقاله را میدهد نه آیدی نویسنده ی مقاله پس وارد پروفایل نویسنده نمیشود
    # author = serializers.HyperlinkedIdentityField(view_name='api:author-detail')

    # نمایش یوزر نیم نویسنده برای فیلد author
    author = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ("created", "updated")

    # custom validation with validate_<field_name>
    def validate_title(self, value):
        forbidden = ["fuck", "shit", "dog", "yes"]
        for i in forbidden:
            if i in value:
                raise serializers.ValidationError('be polite please')
        return value

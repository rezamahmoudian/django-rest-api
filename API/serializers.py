from rest_framework import serializers
from .models import Course, Article
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class CourseSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields =(
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "is_superuser",
        )


class ArticleSerializers(serializers.ModelSerializer):
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

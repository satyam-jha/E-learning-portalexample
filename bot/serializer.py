from rest_framework import serializers
from .models import Question


class Questiondata(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ['bot_id' , 'answer',]

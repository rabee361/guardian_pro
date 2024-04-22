from rest_framework import serializers
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from .models import * 


weekday_mapping = {
    'Monday': 'الاثنين',
    'Tuesday': 'الثلاثاء',
    'Wednesday': 'الأربعاء',
    'Thursday': 'الخميس',
    'Friday': 'الجمعة',
    'Saturday': 'السبت',
    'Sunday': 'الأحد'
}


class HijriSerializer(serializers.Serializer):
    day = serializers.CharField()
    month = serializers.CharField()
    year = serializers.CharField()
    weekday = serializers.CharField()


class GregorianSerializer(serializers.Serializer):
    day = serializers.CharField()
    month = serializers.CharField()
    year = serializers.CharField()




class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'



class SouraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soura
        fields = '__all__'



class ImageSerializer(serializers.ModelSerializer):
    soura = SouraSerializer(read_only=True,many=False)
    class Meta:
        model = Image
        fields = '__all__'

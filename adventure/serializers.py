from rest_framework import serializers
from .models import *



class AdventureSerializer(serializers.ModelSerializer):
    """
    Класс для перевода типов данных Python в json формат
    """

    class Meta:
        """
        Класс для передачи дополнительных данных
        """
        model = Adventure
        fields = "__all__"
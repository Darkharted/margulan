from rest_framework import serializers
from .models import Clas






class ClassSerializer(serializers.ModelSerializer):
    """
    Класс для перевода типов данных Python в json формат
    """


    class Meta:
        """
        Класс для передачи дополнительных данных
        """
        model = Clas
        fields = '__all__'


        
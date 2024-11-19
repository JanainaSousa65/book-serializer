from decimal import Decimal
from rest_framework import serializers
from rest_framework.exceptions import ValidationError #import de validação de erro
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    #conversão
    price_in_dollars = serializers.SerializerMethodField() #converte de reais em dólares

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date','price', 'pages', 'price_in_dollars']

    def get_price_in_dollars(self, obj):
        # Converte o preço de reais para dólares 
        conversion_rate = Decimal('5.0')  
        return obj.price / conversion_rate 

    def validate_pages(self,value):
        if value <= 0:
            raise serializers.ValidationError("Por favor insira um número positivo")
        
        return value
        
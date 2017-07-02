from rest_framework import serializers

from book.api.serializers import BookSerializer
from users.api.serializers import UserSerializer
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('book', 'user', 'price')

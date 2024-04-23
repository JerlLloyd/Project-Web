from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

from myapp.models import *

#GET user model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user
        


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =  "__all__"
    
    

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields =  "__all__"
        
    category = serializers.StringRelatedField()
        

class CartSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField(method_name="totals")
    class Meta:
        model = Cart
        fields = ['id', 'product', 'product_qty',  'user', 'created_at', 'total']
        
    def totals(self, cart:Cart):
        return cart.product_qty * cart.product.s_price
    

 
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id","order", "product", "price", "quantity" ]
        
        product = serializers.StringRelatedField()
        
 
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id","user", "Fname", "Lname", "Email" ,"Contact", "Address", "Baranggay", "City", "Pincode", "payment_mode", "status", "tracking_no", "items", "total_price"]


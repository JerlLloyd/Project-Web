
from django.http import JsonResponse
from rest_framework import serializers, status, viewsets, fields, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login

from rest_framework.pagination import PageNumberPagination


from myapp.models import *

from .serializers import *

#Serializer for user


class RegisterAPI(generics.GenericAPIView):
   
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = {AllowAny}
    
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)





class UserViewSet(viewsets.ModelViewSet):
    permission_classes = {AllowAny}
    queryset = User.objects.all()
   # serializer_class =  UserSerializer
    
class UserDetails(viewsets.ModelViewSet):
    permission_classes = {IsAdminUser, }
   # serializer_class = UserSerializer
    queryset = User.objects.all()
        
class collectionsView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    serializer = CategorySerializer(queryset, many = True)
    
    
class productView(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer
    serializer = productSerializer(queryset, many = True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    pagination_class = PageNumberPagination
    
class cartView(viewsets.ModelViewSet):
    permission_classes = {AllowAny}
    queryset = Cart.objects.all()
    serializer_class = CartSerializer   
    
class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = {IsAuthenticated}
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = {IsAuthenticated}
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    
    
    
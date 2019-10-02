from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import routers, serializers, viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from apps.users.serializers import UserSerializers

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwarsg):
        serializer = self.serializer_class(data=request.data,
                                            context = {'resquest':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
            'is_staff': user.is_staff,
        }
        )
class UsersList(APIView):
    def get(self, request, format=None):
        queryset = User.objects.all()
        serializer = UserSerializers(queryset, many=True)        
        return Response(serializer.data)

class UsersDetail(APIView):
    def get_object(self, id):
        try:            
            return User.objects.get(pk=id) 
        except User.DoesNotExist: 
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = UserSerializers(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
    
    def put(self, request, id, format=None):        
        rol = request.user.is_staff
        example = self.get_object(id)
        if rol == True:
            if example != False:
                serializer = UserSerializers(example, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    datas = serializer.data
                    return Response(datas)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response("No eres administrador")



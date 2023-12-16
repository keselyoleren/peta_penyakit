# myapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from manage_users.models import AccountUser, Puskeswan
from manage_users.serializer.login_serializer import RegisterSerialize, UserLoginSerializer
from manage_users.serializer.user_serialize import UserSerialize



class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)

        try:
            return Response({
                'token': token.key, 
                'user': UserSerialize(user).data,
                'role': user.role,
                'puskeswan': {
                    'id': user.puskeswan.id,
                    'name': user.puskeswan.name,
                }
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'token': token.key,
                'user': UserSerialize(user).data,
                'role': user.role,
                'puskeswan': {
                    'id': None,
                    'name': None,
                }
            }, status=status.HTTP_200_OK)


class UserRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerialize(data=request.data)
        if serializer.is_valid(raise_exception=True):
            puskeswan = Puskeswan.objects.filter(code=request.data.get('puskeswanCode')).first()
            email_exist = AccountUser.objects.filter(email=request.data.get('email')).first()
            if email_exist:
                return Response({'message': 'Email sudah terdaftar'}, status=status.HTTP_400_BAD_REQUEST)

            user = AccountUser.objects.create_user(
                    email=request.data.get('email'),
                    username=request.data.get('email'),
                    password=request.data.get('password'),
                    first_name=request.data.get('name'),
                    is_active=True,
                    puskeswan=puskeswan
                )
            token, created = Token.objects.get_or_create(user=user)
            try:
                return Response(
                    {
                        'token': token.key, 
                        'user': UserSerialize(user).data,
                        'role': user.role,
                        'puskeswan': {
                            'id': user.puskeswan.id,
                            'name': user.puskeswan.name,
                        }
                    }, 
                    status=status.HTTP_200_OK)
            except Exception:
                return Response({
                    'token': token.key,
                    'user': UserSerialize(user).data,
                    'role': user.role,
                    'puskeswan': {
                        'id': None,
                        'name': None,
                    }
                }, status=status.HTTP_200_OK)
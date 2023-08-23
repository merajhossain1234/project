from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token  # Import Token
from rest_framework.authentication import TokenAuthentication  # Import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import SignupSerializer,LoginSerializer
from django.contrib.auth import authenticate

class SignupAPIView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Create a token for the user
            token, created = Token.objects.get_or_create(user=user)

            res = {'status': status.HTTP_201_CREATED, 'token': token.key}  # Include the token in the response
            return Response(res, status=status.HTTP_201_CREATED)
        
        res = {'status': status.HTTP_400_BAD_REQUEST, 'data': serializer.errors}
        return Response(res, status=status.HTTP_400_BAD_REQUEST)






class LoginAPIView(APIView):
    authentication_classes = [TokenAuthentication]  # Apply TokenAuthentication
    permission_classes = [IsAuthenticated]
    """This api will handle login and return token for authenticate user."""
    def post(self,request):
            serializer = LoginSerializer(data = request.data)
            if serializer.is_valid():
                    username = serializer.validated_data["username"]
                    password = serializer.validated_data["password"]
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        """We are reterving the token for authenticated user."""
                        token = Token.objects.get(user=user)
                        response = {
                               "status": status.HTTP_200_OK,
                               "message": "success",
                               "data": {
                                       "Token" : token.key
                                       }
                               }
                        return Response(response, status = status.HTTP_200_OK)
                    else :
                        response = {
                               "status": status.HTTP_401_UNAUTHORIZED,
                               "message": "Invalid Email or Password",
                               }
                        return Response(response, status = status.HTTP_401_UNAUTHORIZED)
            response = {
                 "status": status.HTTP_400_BAD_REQUEST,
                 "message": "bad request",
                 "data": serializer.errors
                 }
            return Response(response, status = status.HTTP_400_BAD_REQUEST)
        
        
        
        
        
        
class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]  # Apply TokenAuthentication
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # Get the user's token and delete it
        token = Token.objects.get(user=request.user)
        token.delete()
        
        response = {
            "status": status.HTTP_200_OK,
            "message": "Successfully logged out."
        }
        return Response(response, status=status.HTTP_200_OK)
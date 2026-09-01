from http.client import responses

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics, request
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from cart.models import Cart

from .models import User
from products.models import Product

from .serializers import UserSerializer
from .serializers import UserLoginSerializer
from .serializers import UpdateUserSerializer
from products.serializers import ListProductSerializer


# Create your views here.

##Creates a new user api POST
##TEST FIELDS ['first_name', 'last_name', 'email', 'password' ]
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


##Allows a user to log in api GET
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        cart = Cart.objects.get(user=user)

        refresh = RefreshToken.for_user(user)

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'cart_id': cart.id,
        })


##Logout Endpoint
class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response(
                {'error': 'Refresh token is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {'message': 'Successfully logged out.'},
                status=status.HTTP_205_RESET_CONTENT
            )

        except Exception:
            return Response(
                {'error': 'Invalid refresh token.'},
                status=status.HTTP_400_BAD_REQUEST
            )



##Allows a user to update data PATCH
class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer

##Gets user information
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCurrentUser(request):
    return Response({
        'id': request.user.id,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    })


####ADMIN ENDPOINTS ONLY#####
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] ### For testing purposes only

class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny] ### For testing purposes only

    def delete(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        user.delete()

        return Response({
            'message': 'User successfully deleted.'
        })
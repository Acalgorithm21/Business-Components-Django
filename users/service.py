from users.models import User
from users.serializers import UserSerializer


def get_user(request):
    user = User.objects.all();
    data = user.get()

    return data

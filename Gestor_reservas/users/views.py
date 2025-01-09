from rest_framework import viewsets
from .serializers import UsersSerializer
from .models import Users

class UsersView(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()
    
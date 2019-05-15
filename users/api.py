from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from rest_framework.views import APIView
import json


class UsersAPI(APIView):

    def get(self, request):
        users = User.objects.all()
        user_list = []
        for user in users:
            user_list.append({
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name
            })
        users_json = json.dumps(user_list)
        return HttpResponse(users_json)

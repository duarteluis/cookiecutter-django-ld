from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import path


class PingView(APIView):
    def get(self, request):
        return Response({"message": "pong"})


urlpatterns = [
    path("ping/", PingView.as_view(), name="ping"),
]

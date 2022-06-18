from rest_framework.views import APIView
from .serializers import AdoptionSerialiazer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .email_service import send_confirmation_email
from .models import Adoption


class AdoptionList(APIView):
    def get(self, request, format=None):
        adoptions = Adoption.objects.all()
        serializer = AdoptionSerialiazer(adoptions, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, format=None):
        serializer = AdoptionSerialiazer(data=request.data)
        if serializer.is_valid():
            adoption = serializer.save()
            send_confirmation_email(adoption)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "message": "Houveram erros de validação",
                "errors": serializer.errors,
            },
            status=HTTP_400_BAD_REQUEST,
        )


from rest_framework.views import APIView
from core.models import Persona
from rest_framework.response import Response
from core.serializer import PersonaSerializer


class PersonListAPIView(APIView):

    def get(self, request, format=None):
        list_person = Persona.objects.all()
        serializer = PersonaSerializer(list_person, many=True)
        return Response(serializer.data)
        


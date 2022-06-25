# rest_framework
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status

# local DJango
from .serializers import PersonSerializer, SearchSerializer
from .models import Person
from .utilities import find_time_slots

class PersonViewset(viewsets.ModelViewSet):
    """Viewset for candidate"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class SearchViewset(views.APIView):

    def post(self, request, format=None):
        serializer = SearchSerializer(data=request.data)
        
        if serializer.is_valid():

            try:
                candidate = Person.objects.get(pk=serializer.data["candidate_id"])
                interviewer = Person.objects.get(pk=serializer.data["interviewer_id"])
            except Person.DoesNotExist as error:
                return Response(data={"detail": f"{error}"}, status=status.HTTP_404_NOT_FOUND)

            if candidate.available_on != interviewer.available_on:
                return Response({"detail": f"Not available on {interviewer.available_on}"})
            
            date = candidate.available_on
            candidate_timing = (candidate.available_from, candidate.available_to)
            interviewer_timing = (interviewer.available_from, interviewer.available_to)
            
            proper_timing = find_time_slots(date, candidate_timing, interviewer_timing)

            return Response(proper_timing, status=status.HTTP_200_OK)

        return Response({"detail": f"Not time slots available"}, status=status.HTTP_404_NOT_FOUND)
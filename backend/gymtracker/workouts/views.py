from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Workout
from .serializers import WorkoutSerializer

@api_view(['GET', 'POST'])
def workouts_api(request):

    if request.method == 'GET':
        data = Workout.objects.all().order_by('-date')
        serializer = WorkoutSerializer(data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

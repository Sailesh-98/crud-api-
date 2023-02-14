from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import studentserializer
from .models import student
from rest_framework import status

# Create your views here.


@api_view(['GET'])
def studentdetail(request):
    students = student.objects.all()
    serializer = studentserializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def studentdetails(request, pk):
    students = student.objects.get(id=pk)
    serializer = studentserializer(students, many=False)
    return Response(serializer.data)




@api_view(['POST'])
def studentupdate(request,pk):
    students = student.objects.get(id=pk)
    serializer = studentserializer( instance= students, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, )   



@api_view(['DELETE'])
def studentdelete(request,pk):
    students = student.objects.get(id=pk)
    students.delete()


    return Response(status=status.HTTP_204_NO_CONTENT)      



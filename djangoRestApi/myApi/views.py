# create restApi - section 5


from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def student_list(request):
	# get all the drinks 
	# serialize them 
	#return json 

	if request.method =='GET':
			# 1. et dall the data 
		student = Student.objects.all()
		# 2. serialize the data 
		serializer = StudentSerializer(student, many=True)
		# 3. return the data 
		# sometimes use safe=false 
		# return JsonResponse({"drinks":serializer.data}, safe=False)  

		return JsonResponse({"students":serializer.data})  
	if request.method =='POST':
		serializer = StudentSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def student_detail(request, id):

	try:
		student = Student.objects.get(pk=id)
	except Student.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method =='GET':
		serializer = StudentSerializer(student)
		return Response(serializer.data)

	elif request.method =='PUT':
		serializer = StudentSerializer(student, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# working 
	# http://localhost:8000/drinks/2/
	# must use / at the end, otherwise not working 
	elif request.method =='DELETE':
		Student.objects.filter(pk=id).delete()
		
		return Response(status=status.HTTP_204_NO_CONTENT)

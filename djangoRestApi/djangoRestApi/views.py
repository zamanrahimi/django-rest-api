from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
	# get all the drinks 
	# serialize them 
	#return json 

	if request.method =='GET':
			# 1. et dall the data 
		Drinks = Drink.objects.all()
		# 2. serialize the data 
		serializer = DrinkSerializer(Drinks, many=True)
		# 3. return the data 
		# sometimes use safe=false 
		# return JsonResponse({"drinks":serializer.data}, safe=False)  

		return JsonResponse({"drinks":serializer.data})  
	if request.method =='POST':
		serializer = DrinkSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):

	try:
		drink = Drink.objects.get(pk=id)
	except Drink.DoesNotExist:
		return response(status=status.HTTP_404_NOT_FOUND)

	if request.method =='GET':
		serializer = DrinkSerializer(drink)
		return Response(serializer.data)

	elif request.method =='PUT':
		serializer = DrinkSerializer(drink, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method =='DELETE':
		pass

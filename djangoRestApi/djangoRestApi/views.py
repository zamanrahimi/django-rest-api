from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer


def drink_list(request):
	# get all the drinks 
	# serialize them 
	#return json 

	# 1. et dall the data 
	Drinks = Drink.objects.all()
	# 2. serialize the data 
	serializer = DrinkSerializer(Drinks, many=True)
	# 3. return the data 
	return JsonResponse(serializer.data, safe=False) 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import FoodItem, Order
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FoodItemSerializer
from .models import FoodItem

@api_view(['GET'])
def food_list(request):
    foods = FoodItem.objects.all()
    serializer = FoodItemSerializer(foods, many=True)
    return Response(serializer.data)

def get_food(request):
    foods = FoodItem.objects.all()

    data = []
    for food in foods:
        data.append({
            "id": food.id,
            "name": food.name,
            "price": food.price,
            "description": food.description
        })

    return JsonResponse(data, safe=False)


@csrf_exempt
def create_order(request):
    if request.method == "POST":
        data = json.loads(request.body)

        food = FoodItem.objects.get(id=data['food_id'])

        order = Order.objects.create(
            food_item=food,
            quantity=data['quantity']
        )

        return JsonResponse({
            "message": "Order placed successfully",
            "order_id": order.id
        })

    return JsonResponse({"error": "Only POST method allowed"})

def get_orders(request):
    orders=Order.objects.all()

    data=[]
    for order in orders:
        data.append({
            "id":order.id,
            "food":order.food_item.name,
            "quantity":order.quantity,
            "created_at":order.created_at
        })

    return JsonResponse(data, safe=False)    
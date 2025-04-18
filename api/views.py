from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    # person = {'name' : 'myname', 'age' : 18}
    items = Item.objects.all()
    serialiser = ItemSerializer(items, many=True)
    return Response(serialiser.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
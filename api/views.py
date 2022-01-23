from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers  import *
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins, generics
# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to our web api')
class AgronomeView(APIView):
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    def get(self,request):
        agronomeData=Agronome.objects.all().order_by('-id')
        agSerializer=AgronomeSerializer(agronomeData, many=True)
        return JsonResponse(agSerializer.data, safe=False)
    def post(self, request):
        agdata = request.data
        agSerializer=AgronomeSerializer(data=agdata)
        if agSerializer.is_valid():
            agSerializer.save()
            return JsonResponse(agSerializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(agSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Mixins
class AgronomeViewMIxin(mixins.CreateModelMixin, 
mixins.ListModelMixin, mixins.RetrieveModelMixin,
mixins.UpdateModelMixin,mixins.DestroyModelMixin,
generics.GenericAPIView):
    queryset= Agronome.objects.all()
    serializer_class=AgronomeSerializer
    def post(self, request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    def get(self, request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    def get(self, request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    def put(self, request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    def delete(self, request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)

# Generics View
class Login(ObtainAuthToken):
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, 
        context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token,created=Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'email':user.email,
            'username':user.username,
            'first_name':user.first_name

        })
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@csrf_exempt
def farmers(request):
    if request.method =='GET':
        farmersData= Farmers.objects.all()
        serializer = FarmersSerializer(farmersData, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FarmersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def farmersUpdate(request, id):
    if request.method == 'GET':
        farmerData = Farmers.objects.get(id=id)
        serializer = FarmersSerializer(farmerData, many=False)
        return JsonResponse(serializer.data, status=200, safe=False)
    elif request.method =='PUT':
        data = JSONParser().parse(request)
        
        farmerData = Farmers.objects.get(id=id)
        farmerData.fullname = data['fullname']
        farmerData.email = data['email']
        farmerData.phone = data['phone']
        farmerData.save()
        serializer = FarmersSerializer(farmerData)
       
        return JsonResponse(serializer.data, status=201)
    elif request.method == 'DELETE':
        farmerData = Farmers.objects.get(id=id).delete()
        serializer = FarmersSerializer(farmerData, many=False)
        return JsonResponse('Data has been deleted', status=200, safe=False)
        
@csrf_exempt
def accountCreation(request):
    if request.method =='GET':
        users = User.objects.all().select_related('profile')
        serializer =UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        userData = JSONParser().parse(request)
        serializer= UserSerializer(data=userData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)


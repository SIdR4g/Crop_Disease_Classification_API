from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
import jwt
import datetime

import os

from keras.models import load_model
import tensorflow as tf
import pickle
import numpy as np

class ViewAPI(APIView):
    def post(self,request):
        token = request.data['jwt']

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token Expired! Log in again.')
        if payload['level'] != 'dev':
            return Response({
                'response' : 'ACCESS DENIED',
            })
        
        user = CropDiseaseAPI.objects.all()        
        serializer=CropDiseaseAPISerializers(user,many = True)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class ActionAPI(APIView):
    def post(self, request):
        token = request.data['jwt']

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token Expired! Log in again.')

        if payload['level'] != 'dev' and payload['level'] != 'farmer':
            return Response({
                'response' : 'INVALID USER',
            })


        new_leaf = CropDiseaseAPI(
            file = request.FILES['file']
        )
        serializer = CropDiseaseAPISerializers(new_leaf)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        new_leaf.save()

        crop = request.data['crop']
        leaf_image = request.FILES['file']

        from PIL import Image 

        def load_image(image_file):
            img = Image.open(image_file)
            return img 

        img = load_image(leaf_image)
        IMG_SIZE = (1,128, 128,3)
        img_array = np.resize(np.array(img),IMG_SIZE)
        dataset = tf.data.Dataset.from_tensor_slices(img_array)
        dataset = dataset.batch(1)
        print(os.getcwd())
        with open('Classes_crop/Classes/'+crop+'_class.pkl','rb') as clas:
            classes = pickle.load(clas)
        reconstructed_model = load_model('Models_crop/Models/'+crop+".h5")
        out = reconstructed_model.predict(dataset)
        response = "The dissease is "+str(classes[np.argmax(out)])+ " with a probability of "+ str(np.max(out)*100)
        print(response)
        return Response({
            'response': response,
            })

class UserActionAPI(APIView):
    def post(self, request):
        name = request.data['name']#used name and level for signup and login
        level = request.data['level']

        print(name,level)

        if level=='dev':#then created token for particular user
            # user = Farmers(request.data)
            serializer = FarmerSerializers(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user = Farmers.objects.filter(name = name).first()

        if level=='farmer':#then created token for particular user
            serializer = FarmerSerializers(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user = Farmers.objects.filter(name = name).first()

        payload = {
            'id': user.id,
            'level': user.level,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }

        #token includes user id and level
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        time = datetime.datetime.utcnow() + datetime.timedelta(seconds=120)
        response.data = {
            'jwt': token,
            'time': time
        }

        return response
from django.shortcuts import render
from .serializers import (EditUserSerializer,
                          RegisterSerializer,)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.http import Http404

# Create your views here.


class UserCreateView(APIView):
    """
    Creates the user.
    """
    def post(self, request, format='json'):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
           
            # print (serializer.validated_data)
            # send_otp()
            email = serializer.validated_data['email']
            mobile = serializer.validated_data['mobile']
            msg = "New User Register"
            check_email = User.objects.filter(email=email).first()
            check_mobile= User.objects.filter(mobile=mobile).first()
            if check_email:
                return Response({"message": "User Already Exists with  This Email! "}, status=status.HTTP_400_BAD_REQUEST)
            if check_mobile:
                return Response({"message": "User Already Exists with This Phone NO!"}, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()
            data = serializer.data
            if user:
                return Response({ 'data':data,
                                  "status":status.HTTP_201_CREATED,
                                  "msg" :  msg})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserCreateView(APIView):
#     # permission_classes = (AllowAny, )
#     def post(self, request, format='json'):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             import pdb;pdb.set_trace()
            
#             # print (serializer.validated_data)
#             # send_otp()
#             # user = serializer.save()
#             # data = serializer.data
#             # msg = "New User Register"
        
#             phone_number  = int(serializer.validated_data['mobile'])
            
#             if phone_number:
                
#                 phone  = str(phone_number)
#                 user = User.objects.filter(mobile__iexact = phone)
#                 print (phone_number)
#                 print("user",user)
#                 if user.exists():
#                     return Response({
#                         'status' : False,
#                         'detail' : 'Phone number already exists.'
#                         })
#                 else:
#                     key = send_otp(phone)

#                     if key:
#                         old = User.objects.filter(mobile__iexact = phone)
#                         if old.exists():
#                             old  = old.first()
#                             count = old.count()
#                             # if count > 20:
#                             #     return Response({
#                             #         'status': False,
#                             #         'detail' : 'Sending otp error. Limit Exceeded. Please contact customer support.'
#                             #         })
#                             old.count = count + 1
#                             old.save()
#                             print('Count Increase', count)
#                             return Response({
#                                 'status' : True,
#                                 'detail' : 'OTP sent successfully.'
#                                 })
#                         else:
#                             user = serializer.save()
#                             data = serializer.data
#                             msg = "New User Register"
                            
#                             if user:
#                                 return Response({ 
#                                                   "status":status.HTTP_201_CREATED,
#                                                   "msg" :  msg,
#                                                   'detail' : 'OTP sent successfully.'})
#                             else:
#                                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#                     else:
#                         return Response({
#                             'status' : False,
#                             'detail' : 'Sending OTP error.'
#                             })

#             else:
#                 return Response({
#                     'status' : False,
#                     'detail' : 'Phone number is not given in post request.'
#                     })


def send_otp(otp, phone):
    if phone:
        key = '12345'
        print(key)
        return key
    else:
        return False


class ValidateOTP(APIView):
    # permission_classes = (AllowAny, )
    def post(self, request, *args, **kwargs):
        
        phone  = request.data['mobile']
        otp_sent = request.data['otp']
        if phone and otp_sent:
            old = User.objects.filter(mobile__iexact = phone)
            if old.exists():
                old = old.first()
                otp = old.otp
                if str(otp_sent) == str(otp):
                    old.validated = True
                    old.save()
                    return Response({
                        'status' : True,
                        'detail' : 'OTP mactched. Please proceed for registration.'
                        })

                else: 
                    return Response({
                        'status' : False,
                        'detail' : 'OTP incorrect.'
                        })
            else:
                return Response({
                    'status' : False,
                    'detail' : 'First proceed via sending otp request.'
                    })
        else:
            return Response({
                'status' : False,
                'detail' : 'Please provide both phone and otp for validations'
                })


class UserEditDetail(APIView):
    """
    Retrieve, update or delete a Teacher instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = EditUserSerializer(teacher)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = EditUserSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




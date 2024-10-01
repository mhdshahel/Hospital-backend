from django.shortcuts import render
from django.http import JsonResponse
from .models import Register,Doctors,staffs,patients,booking
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from .serializer import Doctorss
from django.db.models import Q

@csrf_exempt
def Register_name(request):
    if request.method=='POST':

      name=request.POST.get('NAME')
      dob=request.POST.get('DOB')
      phone=request.POST.get('PHONE')
      age=request.POST.get('AGE')
      duty_time=request.POST.get('DUTY_time')
      catagory=request.POST.get('CATAGORYT')
      gender=request.POST.get('GENDER')
      email=request.POST.get('EMAIL')
      address=request.POST.get('ADDRESS')
      username=request.POST.get('USERNAME')
      
      if Register.objects.filter(Username=username).exists():
         return JsonResponse({'error':'This  user already taken'})
      else:
        if section=="Doctor":
          Doctors.objects.create(NAME=name,EMAIL=email,USERNAME=username,PHONE=phone,DUTY_TIME=duty_tim,AGE=age,GENDER=gender,ADDRESS=address,DOB=dob,CATAGORY=catagory)
          user=Register.objects.create(Name=name,Email=email,Username=username,Password=make_password(Password),Section=section,Phone=phone)
          return JsonResponse({'success':'your registertion  completed'})

        if section=="staffs":

          staffs.objects.create(DOB=dob,EMAIL=email,GENDER=gender,NAME=name,USERNAME=username)
          Register.objects.create(NAME=name,EMAIL=email,USERNAME=username,Password=make_password(password),section=section,phone=phone)

        if  section=="patients":

            patients.objects.create(NAME=name,EMAIL=email,USERNAME=username,PHONE=phone)
            Register.objects.create(Name=name,Email=email,Username=username,Password=make_password(Password),section=section,Phone=phone)

        return JsonResponse({'success':'you Registration Completed'})
          
    else:
        return JsonResponse({'method is wrong'})

          
@csrf_exempt
def login(request):
   if request.method=='POST':

       username=request.POST.get('USERNAME')
       password=request.POSt.get('PASSWORD')
       
       try:
        user=Register.objects.get(Username=username,password=Password)
       except Register.DoesNotExist:
         return JsonResponse({'error':'invalidcredentials'})

         if check_password(password,user.password):
             response =JsonResponse({'message':'login successfull'})
             response.set_cookie('login_cookie','cookie_value',max_age=3600)

             request.session['username']=user.Username
             request.seccion['user_id']=user.id

             csrf_token=get_token(request)
             response.set_cookie('csrftoken')

             return response

             
         else:
           return JsonResponse({'error':'errorrrrrrr'})

def logout(request):
     logout(request)
     response=JsonResponse({'massage':'logout successfully'})
     response.delete_cookie('login_cookie')
     response.delete_cookie('csrftoken')

     return response

@csrf_exempt
def add_Doctors(request):
  if request.method=='POST':
    
    name=request.POST.get('NAME')
    dob=request.POST.get('DOB')
    phone=request.POST.get('PHONE')
    age=request.POST.get('AGE')
    duty_time=request.POST.get('DUTY_time')
    catagory=request.POST.get('CATAGORYT')
    gender=request.POST.get('GENDER')
    email=request.POST.get('EMAIL')
    address=request.POST.get('ADDRESS')
    username=request.POST.get('USERNAME')

    if Doctors.objects.filter(USERNAME=username).exists():
       data=Doctors.objects.get(USERNAME=username)
       data.NAME=name
       data.PHONE=phone
       data.DOB=dob
       data.GENDER=gender
       data.AGE=age
       data.EMAIL=email
       data.DUTY_time=duty_time
       data.ADDRESS=address
       data.CATAGORY=catagory
       data.save()

       return JsonResponse ({'success':'good'})


    else:
      return JsonResponse({'erorr':'not found'})


@csrf_exempt
def add_staffs(request):
      if request.method=='POST':

       name=request.POST.get('NAME')
       username=request.POST.get('USERNAME')
       address=request.POST.get('ADDRESS')
       age=request.POST.get('AGE')
       phone=request.POST.get('PHONE')
       email=request.POST.get('EMAIL')
       gender=request.POST.get('GENDER')
       dob=request.POST.get('DOB')
       qualifition=request.POST('QUALIFITION')
       password=request.POST.get('PASSWORD')


       if staffs.objects.filter(USERNAME=username).exists():
        data=staffs.objects.get(USERNAME=username)
        data.NAME=name
        data.USERNAME=username
        data.AGE=age
        data.DOB=dob
        data.PASSWORD=password
        data.GENDER=gender
        data.PHONE=phone
        data.QUALIFITION=qualifition
        data.EMAIL=email
        data.ADDRESS=address
        data .save()


        return JsonResponse({'success':'sheriyan'})

      else:

        return JsonResponse({'eroor':'tettan'})

      
@csrf_exempt
def add_patients (request):
        if request.method=='POST':

          name=request.POST.get('NAME')
          age=request.POST.get('AGE')
          address=request.POST.get('ADDRESS')
          phone=request.POST.get('PHONE')
          gender=request.POST.get('GENDER')
          dob=request.POST.get('DOB')
          boold_group=request.POST.get('BOOLD_GROUP')
        
        if patients.objects.filter(USERNAME=username).exists():
          data=patients.objects.get(USERNAME=username)
          data.NAME=name
          data.AGE=age
          data.ADDRESS=address
          data.PHONE=phone
          data.GENDER=gender
          data.DOB=dob
          data.BOOLD_GROUP=bools_group
          data.save()

          return JsonResponse({'success':'sheriyan'})

        else:

                return JsonResponse({'eroor':'tettan'})




@csrf_exempt
def add_booking(request):
         if request.method=='POST':

          name=request.POST.get('NAME')
          age=request.POST.get('AGE')
          address=request.POST.get('ADDRESS')
          phone=request.POST.get('PHONE')
          gender=request.POST.get('GENDER')

          if booking.objects.filter(PHONE=phone).exists():
             return JsonResponse({'eroor':'NIGAL ITHINAGAM  BOOK CHEYITHITTUND'})

         else:


            try:
               last_token=booking.objects.all().order_by('TOKENNUMBER').last()
               new_token=last_token.TOKENNUMBER+1
               booking.objects.create(NAME=name,AGE=age,ADDRESS=address,PHONE=phone,GENDER=gender,TOKENNUMBER=new_token)

               return JsonResponse({'success':'NINGALUDE BOOKING VIJAYAKARAMAYI','your token is':new_token})


            except:
                    booking.objects.create(NAME=name,AGE=age,ADDRESS=addres,PHONE=phone,GENDER=gender)


                    return JsonResponse({'SUCCESS':'your token number is 1'})

     


@csrf_exempt
def delete_multiple_data(request):
        if request.method=='POST':

           Register.objects.get(USERNAME=username).delete()
           Doctors.objects.get(USERNAME=username).delete()
           staffs.objects.get(USERNAME=username).delete()
           patients.objects.get(USERNAME=username).delete()
               
           return JsonRespons({'success':'DELETE AYITTUND'})


        else:

                return JsonResponse({'ERORR':'DELETE AYITTILA'})
      
@csrf_exempt
def display_Doctors(request):
            name= request.POST.get('name')

            if Doctors.objects.filter(NAME=name).exists():
                 data=Doctors.objects.filter(NAME=name, CATAGORY='doctor')

                 serializer=Doctorss(data,many=True)
                 
                 return JsonResponse({'status':'success','data':serializer.data})




@csrf_exempt
def display_staffs(request):
            name= request.POST.get('name')

            if staffs.objects.filter(NAME=name).exists():
                 data=staffs.objects.filter(NAME=name, CATAGORY='staffs')

                 serializer=stafss(data,many=True)
                 
                 return JsonResponse({'status':'success','data':serializer.data})





@csrf_exempt
def display_patients(request):
            name= request.POST.get('name')

            if patients.objects.filter(NAME=name).exists():
                 data=patients.objects.filter(NAME=name, CATAGORY='staffs')

                 serializer=patients(data,many=True)
                 
                 return JsonResponse({'status':'success','data':serializer.data})


def search_for_doctor(request,name):

      if name:
             
 
          data=Doctors.objects.filter(Name__icontains=name)  | Doctors.objects.filter(phone__icontains=name) | Doctors.objects.filter(Email__icontains=name) | Doctors.objects.filter(Address__icontains=name) 
            
          serializer=Doctors(data,many=True)

          return JsonResponse({'status':'success','data':serializer.data})

      else:
         return JsonResponse({'erorr':"no user found"})   



def search_for_staffs(request,name):

      if name:
             
 
          data=staffs.objects.filter(Name__icontains=name)  | staffs.objects.filter(phone__icontains=name) | staffs.objects.filter(Email__icontains=name) | staffs.objects.filter(Address__icontains=name) 
            
          serializer=staffs(data,many=True)

          return JsonResponse({'status':'success','data':serializer.data})

      else:
         return JsonResponse({'erorr':"no user found"})   



def search_for_patients(request,name):

      if name:
             
 
          data=patients.objects.filter(Name__icontains=name)  | patients.objects.filter(phone__icontains=name) | patients.objects.filter(Email__icontains=name) | patients.objects.filter(Address__icontains=name) 
            
          serializer=patients(data,many=True)

          return JsonResponse({'status':'success','data':serializer.data})

      else:
         return JsonResponse({'erorr':"no user found"})  


      
      




      
          

           

      
from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .iteganya import *
# Create your views here.
def  welcome(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='turabayoimmacule@gmail.com'
api_key ='8e70d9b7b66a13836369cbd2a7813b4b7fe036a9cc99df1f7464a89d960cd2c9'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):

    if request.method == 'POST':

        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST['text']
        # 1*1*1 
        level = text.split('*')
        category = text[:3]
        response =""
        #  main menu for our application
        if text == '':
            response =  "CON Murakaza neza kuri Hunikapp \n"
            response += "1. Ikinyarwanda \n"
            response += "2. English \n"
        elif text == '1':
            # SELECT * FROM PRODUCTMODEL where title="" ORDER BY ID DESC LIMIT 5
            #fetchProducts = HunikaappUserobjects.all()
            response = "CON mwiyandikishe \n"
            response += "1.Ukoresheje irangamuntu\n"
            response += "2.Udakoresheje irangamuntu\n"
            #for  hunikappAdmin in  hunikappAdmin:
                #response += ""+str(products.id)+"."+str(products.title)+ "\n"

        elif text == '1*1':
            product=""
            response = "CON shyiramo nimero y irangamuntu "+str(product)+"\n"
        elif category =='1*1' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "CON ubwoko bw ibihingwa \n"
            response += "1. ibinyameke \n"
            response += "2. ibinyamafufu \n"
            response += "3. imboga n imbuto"
        elif category =='1*1' and int(len(level)) == 4 and str(level[3]) in  str(level):
            response = "CON Shyiramo igihe bizahunikwa \n"
            response += "1. ukwezi \n"
            response += "2.umwaka"
        elif category =='1*1' and int(len(level)) == 5 and str(level[4]) in  str(level):
            # save the data into the database
            #names= level[3]
            #idnumber = level[4]
            #insert = Hunikappuser(sessiondId=session_id,
            #serviceCode = service_code,
            #phoneNumber=phone_number,
            #names=names,
            #idnumber=idnumber,
            #)
            #insert.save()
            response = "END Murakoze kwiyandikisha kuri hunikapp\n"


    #     # elif text == '1*2':
    #     #     product ="Indimu"
    #     #     response ="CON shyiramo ubuso bw'ubutaka bwawe bw' "+str(product)+"\n"
    #     # elif category =='1*2' and int(len(level)) == 3 and str(level[2]) in  str(level):
    #     #     response = "CON Uwo mubufatanyije \n"
    #     # elif category =='1*2' and int(len(level)) == 4 and str(level[3]) in  str(level):
    #     #     response = "CON Shyiramo nimero y'irangamuntu yuwo mufatanyije \n"
    #     # elif category =='1*2' and int(len(level)) == 5 and str(level[4]) in  str(level):
    #     #     category='Indimu'
    #     #     sizeOfland=level[2]
    #     #     names= level[3]
    #     #     idnumber = level[4]
    #     #     insert = Idafarmuser(sessiondId=session_id,
    #     #     serviceCode = service_code,
    #     #     phoneNumber=phone_number,
    #     #     level=level,
    #     #     category=category,
    #     #     sizeOfland=sizeOfland,
    #     #     names=names,
    #     #     idnumber=idnumber,
    #     #     )
    #     #     insert.save()
    #         # response = "END Murakoze kwiyandikisha kuri Ida farm \n"
         
    #     #  ======================== INGENGABIHE==================
    #     elif text == '2':
    #         response = "CON REGISTER HERE \n "
    #         response += "1.With ID\n"
    #         response += "2.Without ID\n"
    #         elif text == '2*1':
    #         insertData(
    #             category='Kabiri',
    #             sessionID=session_id,
    #             phoneNumber=phone_number
    #         )
        
    #         response = "CON Enter your Id number "+str(product)+"\n"
    #     elif category =='2*2' and int(len(level)) == 3 and str(level[2]) in  str(level):
    #         response = "CON Types Of Your Products \n"
    #         response += "1. Graineaters \n"
    #         response += "2. ibinyamafufu \n"
    #         response += "3. Vegetables&Fruits"
    #     elif category =='2*3' and int(len(level)) == 4 and str(level[3]) in  str(level):
    #         response = "CON Period \n"
    #         response += "1. Months \n"
    #         response += "2.Year"

    #     # elif text == '2*1':
    #     #      save the data
    #     #     insertData(
    #     #         category='Rimwe',
    #     #         sessionID=session_id,
    #     #         phoneNumber=phone_number
    #     #     )
    #     #     response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe rimwe mukwezi"
    #     #     response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe kabiri mukwezi"
    #     # elif text == '2*3':
    #     #     insertData(
    #     #         category='Burigihe',
    #     #         sessionID=session_id,
    #     #         phoneNumber=phone_number
    #     #     )
    #         response ="END THANKS FOR REACHING TO US"

    #     else:
    #         response = "END INVALID OPTION, TRY LATER"
    #     return HttpResponse(response)
    # else:
    #     return HttpResponse('we are on ussd app')

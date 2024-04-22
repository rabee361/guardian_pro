from django.shortcuts import render , get_object_or_404
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework.generics import RetrieveAPIView , ListAPIView




# @login_required
# def join_group(request, uuid):
# 	u = request.user
# 	gp = Group.objects.get(uuid=uuid)

# 	gp.members.add(u)
# 	gp.save()
# 	return redirect('home')

# @login_required
# def leave_group(request, uuid):
# 	u = request.user
# 	gp = Group.objects.get(uuid=uuid)
# 	gp.members.remove(u)
# 	gp.save()
# 	return redirect('home')


# @login_required
# def open_chat(request, uuid):
# 	group = Group.objects.get(uuid=uuid)
# 	if request.user not in group.members.all():
# 		return HttpResponseForbidden('Not a member. Try another group.')
# 	messages = group.message_set.all()
# 	sorted_messages = sorted(messages, key=lambda x: x.timestamp)
# 	return render(request, 'chat.html', context={'messages':sorted_messages, 'uuid': uuid})










Url = 'http://api.aladhan.com/v1/timings/'
# 17-07-2007?latitude=51.508515&longitude=-0.1254872&method=2

def get_response(longitude,latitude,day,month,year):
    formatted_date = ''
    if day and month and year:
        date = datetime(int(year), int(month), int(day))
        formatted_date = date.strftime("%d-%m-%Y")
        print(Url+formatted_date)
    else:
        return Response({"error":"wrong data"})
    
    p = {
        'longitude' : longitude,
        'latitude' : latitude
    }
    response = requests.get(Url+formatted_date,params=p)
    return response.json()


class CalenderView(APIView):
    def post(self,request):
        longitude = request.data.get('longitude')
        latitude = request.data.get('latitude')
        day = request.data.get('day')
        month = request.data.get('month')
        year = request.data.get('year')

        response = get_response(longitude,latitude,day,month,year)
        gregorian_date = {
            'day': response['data']['date']['gregorian']['day'],
            'month': response['data']['date']['gregorian']['month']['en'],
            'year': response['data']['date']['gregorian']['year'],
        }

        hijri_date = {
                'day': response['data']['date']['hijri']['day'],
                'month': response['data']['date']['hijri']['month']['ar'],
                'year': response['data']['date']['hijri']['year'],
                'weekday': response['data']['date']['hijri']['weekday']['ar'],
            }

        gregorian = GregorianSerializer(gregorian_date)
        hijri = HijriSerializer(hijri_date)
        arabic_gregorian_date = gregorian.data
        arabic_hijri_date = hijri.data

        return Response({
            'timings': response['data']['timings'],
            'hijri' : arabic_hijri_date,
            'gregorian': arabic_gregorian_date,
            'city': response['data']['meta']['timezone']
        })
    

    



from fcm_django.models import FCMDevice

def send_notification(title, body, device_id):
    device = FCMDevice.objects.get(id=device_id)
    device.send_message(title=title, body=body)









class Chats(APIView):
    def get(self,request):
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats,many=True)
        return Response(serializer.data)
    


# class Chat(RetrieveAPIView):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer


class ChatMessages(APIView):
    def get(self,request,chat_id):
        chat = Chat.objects.get(id=chat_id)
        messages = Message.objects.filter(chat=chat)
        serializer = MessageSerializer(messages,many=True)
        return Response(serializer.data)
    



def send_notification(request):
    user = User.objects.get(username='username')
    devices = FCMDevice.objects.filter(user=user)
    devices.send_message(title="Notification Title", body="Notification Body")
    return Response('Notification sent.')



class GetSoura(RetrieveAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is not None:
            soura = get_object_or_404(Soura, id=pk)
            return Image.objects.filter(soura=soura)
        else:
            return Image.objects.none()
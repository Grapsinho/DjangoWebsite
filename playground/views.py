from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic, Messages, User
from .forms import RoomForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    #if q != None:
        #q = request.GET.get('q')
    #else:
       # q = ''

    rooms = Room.objects.filter(
        
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    
    ) # აქ კი ვაგზავნით მოთხოვნას იმ მონაცემებზე რომლების ასოებიც ემთხვევა ამათუ იმ ტოპიკს მაგალითად თუ ჩავწერეთ py ეს დაემთხვევა python და ასშ...
    
    topic = Topic.objects.all()
    room_count = rooms.count()
    
    # ესეიგი ამით შეგვიძლია გავფილტროთ და გამოვიტანოთ მხოლოდ ის მესჯიები რომლებიც რომელიმე კონკრეტულ რუმს ეკუთვნის
    room_massages = Messages.objects.filter(Q(room__topic__name__icontains=q)).order_by('-created')[0:3]

    context = {"rooms": rooms, "topics": topic, 'room_count': room_count, "room_massages": room_massages, "q": q}
    return render(request, 'playground/home.html', context)

def room(request, room_id):
    room = Room.objects.get(id=room_id)
    room_massages = room.messages_set.all()[0:20] # ეს გვაძლევს ყველა ამ რუმთან დაკავშირებულ მესიჯებს
    participants = room.participants.all()

    if request.method == 'POST':
        room.participants.add(request.user)

    context = {"room": room, 'room_massages': room_massages, 'participants': participants, 'room_id': room_id,}

    for message in room_massages:
        context['message1'] = message

    return render(request, 'playground/room.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    topic = Topic.objects.all()
    room_massages = user.messages_set.all()
    context = {'user':user, "rooms": rooms, 'topics': topic, "room_massages": room_massages}
    return render(request, 'playground/profile.html', context)

@login_required(login_url='login')
def roomPage(request):
    fields = RoomForm()
    all_topics = Topic.objects.all()

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    context = {"fields": fields, 'all_topics': all_topics}
    return render(request, 'playground/room_page.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) # ანუ ეს ფორმ შეივსება წინასწარ ამ როომით
    topics = Topic.objects.all()

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        form = RoomForm(request.POST, instance=room) # ეს ინსტენსი იმიტომ რომ ვიცოდეთ რომელ რუმს ვააბდეითებთ და ახალი რუმი კიარ შექმნას ის დააბდეითოს

        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'fields': form, 'topics': topics, "room": room}

    return render(request, 'playground/room_page.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id = pk)

    if request.method == 'POST':
        room.delete()    # და ნუ მოკლედ უბრალოდ წავშალეთ ის რუმი
        return redirect('home')

    return render(request, 'playground/delete_room.html', {'obj': room})

@login_required(login_url='login')
def deleteMessages(request, pk):

    message = Messages.objects.get(id = pk)

    if request.method == 'POST':
        message.delete() # და ნუ მოკლედ უბრალოდ წავშალეთ ის მესიჯი
        return redirect('home')

    return render(request, 'playground/delete_messages.html', {'obj': message})
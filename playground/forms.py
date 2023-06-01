from django.forms import ModelForm 
from .models import Room, User

class RoomForm(ModelForm):
    class Meta:
        model = Room #ის ცხრილი რომლისთვისაც გვინდა რომ შევქმნათ ფორმი
        fields = '__all__'
        exclude = ['host', 'participants'] # ანუ შექმნის ყველა ჩამოწერილი ქოლუმნისთვის ფორმის ელემენტებს
        # ხოლო შეგვიძლია შევქმნათ ლისტი და ამ ლისტში ჩავწეროთ ის რაღაცეები რისთვისაც გვინდა რომ შეიქმნას იმ ქოლუმნის სახელები
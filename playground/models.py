from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, unique=True)

    avatar = models.ImageField(null=True, default='avatar.svg')

    #ანუ იუზერნეიმ ფიელდ იქნება ემაილი ეხლა
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model): #ჩავთვალოთ ეს არის ქოლუმნის სახელი
    # ესენი უკვე არიან როუები
                              #ანუ როცა ამეებს ვაწერთ ჩვენ ვეუბნებით დატაბეისს თუ რამოუვა ამ Room და ასშ...
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
                      #ანუ შეიძლება რომ null იყოს
                      #ბლანკ არის ფორმისთვის form ხოლო null დატაბეისისთვის
    description = models.TextField(null=True, blank=True) # ეს უბრალოდ იქნება უფრო დიდი ტექსტ ფიელდი
    # related_name გვჭირდება იმიტომ რომ იუზერი უკვე გვაქ დაკავშირებული სხვა ქოლუმნებთან
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) # ანუ როდესაც დავაწვებით ბათონს ეს დააყენებს დროს
    created = models.DateTimeField(auto_now_add=True) # ანუ თუ ბათონს დავაწვებით რამოდენიმეჯერ ეს არ შეიცვლება ის მაღლითა კი

    class Meta:
        ordering = ['-updated', '-created'] # ანუ ახალ შექმნილ რუმებს ვალაგებთ desc ორდერით იმიტომ რომ ბოლოს შექმნილი რუმი მოხვდეს თავში და ასშ...

    def __str__(self):
        return self.name

class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
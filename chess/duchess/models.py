from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    victories = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    STATUS = (
        ('Done','Done'),
        ('Playing','Playing'),
        ('Aborted','Aborted'),
        )
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    player1 = models.ForeignKey(Player,null=True,on_delete=models.SET_NULL,related_name='player1')
    player2 = models.ForeignKey(Player,null=True,on_delete=models.SET_NULL,related_name='player2')
    winner = models.ForeignKey(Player,null=True,on_delete=models.SET_NULL,related_name='winner')
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    
    def __str__(self):
        return str(self.player1)+" vs "+str(self.player2)+" time:  "+str(self.date_created)+" winner: "+str(self.winner)

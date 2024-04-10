from django.db import models
from games.models import Game


class Weapon(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    image = models.URLField()
    description = models.TextField()
    category = models.CharField(max_length=100)
    weight = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='weapons', default='Elden Ring')

    def __str__(self):
        return self.name


class AttackAttribute(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='attack_attributes')
    name = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.weapon.name} - Attack: {self.name}: {self.amount}"


class DefenseAttribute(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='defense_attributes')
    name = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.weapon.name} - Defense: {self.name}: {self.amount}"


class Scaling(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='scalings')
    name = models.CharField(max_length=50)
    scaling = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.weapon.name} - Scaling: {self.name}: {self.scaling}"


class RequiredAttribute(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='required_attributes')
    name = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.weapon.name} - Required: {self.name}: {self.amount}"

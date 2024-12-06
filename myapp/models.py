from django.db import models

from common_app.models import BaseModel


class HouseChoices(models.Choices):
    GRYFFINDOR = "GRYFFINDOR"
    RAVENCLAW = "RAVENCLAW"
    HUFFLEPUFF = "HUFFLEPUFF"
    SLYTHERIN = "SLYTHERIN"


class GenderChoices(models.Choices):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHERS = "OTHERS"



class Wizard(BaseModel):
    name = models.CharField(max_length=64, null=False, blank=False)
    house = models.CharField(
        max_length=20, choices=HouseChoices.choices, default=HouseChoices.SLYTHERIN
    )
    gender = models.CharField(
        max_length=20, choices=GenderChoices.choices, default=GenderChoices.MALE
    )
    image = models.ImageField(null=True, upload_to="wizard_images/")


    def __str__(self):
        return self.name

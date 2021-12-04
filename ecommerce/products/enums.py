from django.db import models
from django.utils.translation import gettext_lazy as _


class Colors(models.TextChoices):
    RED = "red", _("Red")
    BLUE = "blue", _("Blue")
    WHITE = "white", _("White")
    YELLOW = "yellow", _("Yellow")

class Categories(models.TextChoices):
    TECHNOLOGY = "technology", _("Technology")
    FASHION = "fashion", _("Fashion")
    HOME = "home", _("home")
    COSMETICS =  "cosmetics", _("Cosmetics")
    KIDS = "kids", _("Kids")
    PETS = "pets", _("Pets")
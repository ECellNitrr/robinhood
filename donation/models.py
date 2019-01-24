from django.db import models
from appprofile.models import Profile

# Create your models here.
class Item(models.Model):
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False, default="RobinHood")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return str(self.name)

class Donation(models.Model):
    ITEM_CONDITION = (
        ('REP', 'Repairable'),
        ('WOR', 'Working'),
    )
    class Meta:
        verbose_name = "Donation"
        verbose_name_plural = "Donations"
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False, default="Donation Description")
    quantity = models.IntegerField(default=1, blank=False, null=False)
    status = models.BooleanField(default=True)
    item_condition = models.CharField(
        max_length = 3,
        choices=ITEM_CONDITION,
        default='WOR',
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return str(self.profile.user.first_name + " " + self.profile.user.last_name + " => " + self.item.name)
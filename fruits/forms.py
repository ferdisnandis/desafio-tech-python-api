from django.forms import ModelForm
from fruits.models import Fruits, Region

# Create the form class.
class FruitsForm(ModelForm):
    class Meta:
        model = Fruits
        fields = ['name', 'region']

class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = ['name']
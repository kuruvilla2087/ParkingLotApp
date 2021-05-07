from django import forms
from car.models import car
import datetime

class NewCarForm(forms.ModelForm):
    class Meta:
        model = car
        fields = ('regno', 'color','Time_in')

    def clean(self):
	    """ 
	    Override the default clean method to check whether this course has
	    been already inputted.
	    """    
	    cleaned_data = self.cleaned_data
	    name = cleaned_data.get('regno')

	    matching_names = car.objects.filter(regno=name,status='in')
	    if self.instance:
	        matching_names = matching_names.exclude(pk=self.instance.pk)
	    if matching_names.exists():
	        msg = u"Car number: %s already exist in Parking " % name
	        raise forms.ValidationError(msg)
	    else:
	        return self.cleaned_data

class Meta:
    model = car


class RemoveCarForm(forms.ModelForm):
    class Meta:
        model = car
        fields =('regno',)

class SearchCarForm(forms.Form):
          searchfield = forms.CharField(max_length=100)


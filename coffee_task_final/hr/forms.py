from django import forms
from .models import Category , Machine 

class PersonForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('machine', 'Type', 'coffeePod', 'flavour', 'wl', 'packsize')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['option'].queryset = Category.objects.none()

    #     if 'machine' in self.data:
    #         # print('if')
    #         try:
    #             machine_id = int(self.data.get('machine'))
    #             self.fields['option'].queryset = Category.objects.filter(machine=machine_id).order_by('option')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty category queryset
    #     elif self.instance.pk:
    #         self.fields['option'].queryset = self.instance.machine.category_set.order_by('option')

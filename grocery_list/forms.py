from django.forms import ModelForm, Select, DateInput, SelectDateWidget, TextInput, Form

from grocery_list.models import GroceryList


class DateTypeInput(DateInput):
    input_type = 'date'


class GroceryListForm(ModelForm):
    class Meta:
        model = GroceryList
        fields = "__all__"
        exclude = ['user']
        widgets = {
            "item_status": Select(attrs={'class': 'form-control'}),
            "date": DateTypeInput(attrs={'class': 'form-control'}),
            "item_quantity": TextInput(attrs={'class': 'form-control'}),
            "item_name": TextInput(attrs={'class': 'form-control'})
        }

    def save(self, user=None):
        user_profile = super(GroceryListForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile

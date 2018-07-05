from django.forms import ModelForm, FileField, ClearableFileInput, CharField, TextInput, ImageField
from gallery.models import Image


class ImageForm(ModelForm):
    image = FileField(widget=ClearableFileInput(attrs={'multiple': True}))
    file_name = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Photo Title'}))

    class Meta:
        model = Image
        fields = ['file_name', 'image']

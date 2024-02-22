from django import forms
from .models import File

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewFileForm(forms.ModelForm):
    """
    Form class for creating a new item.

    Inherits from Django's ModelForm class.
    Sets the Meta class to specify the File model and fields to include.
    Defines custom widgets for certain fields.
    """
    class Meta:
        model = File
        fields = ('category', 'title', 'author', 'publication_year', 'language', 'price', 'rating', 'image', 'file_type', 'file')
        widgets = {
            'category': forms.Select(attrs={'class': INPUT_CLASSES}),
            'title': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'author': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'publication_year': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'language': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'rating': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
            'file_type': forms.Select(attrs={'class': INPUT_CLASSES}),
            'file': forms.FileInput(attrs={'class': INPUT_CLASSES})
        }

class EditFileForm(forms.ModelForm):
    """
    Form class for editing an existing item.

    Inherits from Django's ModelForm class.
    Sets the Meta class to specify the Item model and fields to include.
    Defines custom widgets for certain fields.
    """
    class Meta:
        model = File
        fields = ('author', 'category', 'title', 'price', 'image', 'file', 'available', )
        widgets = {
            'author': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'title': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'category': forms.Select(attrs={'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
            'file': forms.FileInput(attrs={'class': INPUT_CLASSES}),
            'available': forms.CheckboxInput(attrs={'class': INPUT_CLASSES})
        }

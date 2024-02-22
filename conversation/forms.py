from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    """
    Represents a form for creating or updating a conversation message.
    """
    class Meta:
        # Specifies the ConversationMessage model to use for the form
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }
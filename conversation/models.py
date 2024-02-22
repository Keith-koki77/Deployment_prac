from django.contrib.auth.models import User
from django.db import models

from file.models import File

class Conversation(models.Model):
    """
    Represents a conversation between users.
    """
      # A foreign key relationship to the Item model, representing the item associated with the conversation.
    file = models.ForeignKey(File, related_name='conversations', on_delete=models.CASCADE)

    # A many-to-many relationship to the User model, representing the members of the conversation.
    members = models.ManyToManyField(User, related_name='conversations')

    # A DateTimeField that automatically sets the value to the current datetime when a new conversation is created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A DateTimeField that automatically updates the value to the current datetime whenever the conversation is modified.
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Defines the default ordering for conversations, based on the modified_at field in descending order.
        ordering = ('-modified_at',)

class ConversationMessage(models.Model):
    """
    Represents a message within a conversation.
    """

    # A foreign key relationship to the Conversation model, representing the conversation the message belongs to.
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)

    # A TextField to store the content of the message.
    content = models.TextField()

    # A DateTimeField that automatically sets the value to the current datetime when a new message is created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A foreign key relationship to the User model, representing the user who created the message.
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)

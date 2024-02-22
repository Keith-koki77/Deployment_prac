from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from file.models import File

from .forms import ConversationMessageForm
from .models import Conversation

@login_required
def new_conversation(request, file_pk):
    """
    Create a new conversation with the given item.
    Parameters:
        - request: The HTTP request object.
        - item_pk: The primary key of the item.
    Returns:
        - If the user is the creator of the item, redirects to the index page.
        - If a conversation with the item already exists for the user, redirects
        to the conversation detail page.
        - If the request method is POST and the form is valid, creates a new
        conversation, adds the necessary members, saves the conversation
        message, and redirects to the item detail page.
        - If the request method is not POST, renders the new conversation form.
    Raises:
        - None.
    """
    file = get_object_or_404(File, pk=file_pk)

    if file.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(file=file).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(file=file)
            conversation.members.add(request.user)
            conversation.members.add(file.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('file:detail', pk=file_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form
    })

@login_required
def inbox(request):
    """
    Renders the inbox view for a logged-in user.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered inbox.html template with the conversations data.
    """
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required
def detail(request, pk):
    """
     Renders the detail view for a conversation.
    Parameters:
        - request: The HTTP request object.
        - pk: The primary key of the conversation.
    Returns:
        - If the request method is POST and the form is valid, redirects to the conversation detail page.
        - If the request method is not POST, renders the conversation detail page with the conversation and form context variables.
    """
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form
    })

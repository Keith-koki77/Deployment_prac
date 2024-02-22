from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from file.models import File

@login_required
def index(request):
    """
    Renders the 'dashboard/index.html' template with a context containing the items created by the logged-in user.
    Parameters:
        request (HttpRequest): The HTTP request object sent by the client.
    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    files = File.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'files': files,
    })

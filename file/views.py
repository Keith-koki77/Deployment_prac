from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewFileForm, EditFileForm
from .models import Category, File, Payment


def files(request):
    """
    Renders the files page with a list of files based on the request parameters.
    Parameters:
        - request: The HTTP request object.
    Returns:
        - The rendered items.html template with the items, query, categories,
        and category_id context variables.
    """
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    files = File.objects.all()

    if category_id:
        files = files.filter(category_id=category_id)

    if query:
        files = files.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'file/files.html', {
        'files': files,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })


def detail(request, pk):
    """
     Renders the detail page for a specific item.
    Parameters:
        - request: The HTTP request object.
        - pk: The primary key of the item.
    Returns:
        - The rendered detail.html template with the item and related_items context variables.
    """
    file = get_object_or_404(File, pk=pk)
    related_files = File.objects.filter(category=file.category, available=True).exclude(pk=pk)[0:3]

    return render(request, 'file/detail.html', {
        'file': file,
        'related_files': related_files
    })

@login_required
def new(request):
    """
    Renders the new item form page and handles form submission to create a new item.
    Parameters:
        - request: The HTTP request object.
    Returns:
        - If the request method is POST and the form is valid,
        redirects to the item detail page for the new item.
        - If the request method is not POST, renders the form.html
        template with the new item form and title context variables.
    """
    if request.method == 'POST':
        form = NewFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.save(commit=False)
            file.created_by = request.user
            file.save()

            return redirect('file:detail', pk=file.id)
    else:
        form = NewFileForm()

    return render(request, 'file/form.html', {
        'form': form,
        'title': 'New file',
    })


@login_required
def edit(request, pk):
    """
     Renders the edit item form page and handles form submission to edit an existing item.
    Parameters:
        - request: The HTTP request object.
        - pk: The primary key of the item.
    Returns:
        - If the request method is POST and the form is valid, redirects to
        the item detail page for the edited item.
        - If the request method is not POST, renders the form.html template with
        the edit item form and title context variables.
    """
    file = get_object_or_404(File, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditFileForm(request.POST, request.FILES, instance=file)

        if form.is_valid():
            form.save()

            return redirect('file:detail', pk=file.id)
    else:
        form = EditFileForm(instance=file)

    return render(request, 'file/form.html', {
        'form': form,
        'title': 'Edit file',
    })

@login_required
def delete(request, pk):
    """
     Deletes an item specified by its primary key and the authenticated user.
    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the item to be deleted.
    Returns:
        HttpResponseRedirect: A redirect response to the index page of the dashboard.
    """
    file = get_object_or_404(File, pk=pk, created_by=request.user)
    file.delete()

    return redirect('dashboard:index')


@login_required
def process_payment(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    # Process payment using your payment gateway here
    # Assuming payment is successful
    payment = Payment.objects.create(user=request.user, file=file, paid=True)
    return redirect('file:download', file_id=file_id)  # Corrected redirect URL

@login_required
def download(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    # Check if the user has made a payment for the file
    if not Payment.objects.filter(user=request.user, file=file, paid=True).exists():
        # Redirect the user to the payment page or form
        return redirect('file:payment', file_id=file_id)  # Use correct URL name
    else:
        # User has made a payment, allow file download
        # You can implement file download logic here
        # For example, return a response with the file content
        return render(request, 'file/download.html', {'file': file})

@login_required
def payment(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    # Render the payment page or form
    return render(request, 'file/payment.html', {'file': file})

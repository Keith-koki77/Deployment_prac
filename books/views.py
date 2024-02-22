# Create your views here.
from django.shortcuts import render, redirect

from file.models import Category, File

from .forms import SignupForm

from django.contrib.auth import logout




def index(request):
    # Fetch all featured books
    files = File.objects.all()

    # Fetch files by category for display
    files_by_category = {}
    categories = Category.objects.all()
    for category in categories:
        files_by_category[category] = File.objects.filter(category=category)

    context = {
        'files': files,
        'files_by_category': files_by_category,
    }

    return render(request, 'books/index.html', context)


def landing(request):
    """
    This function handles the landing page.
    
    :param request: The HTTP request object.
    :return: The rendered landing page.
    """
    # Retrieve all categories
    categories = Category.objects.all()

    # Create a dictionary to store files grouped by category
    files_by_category = {}

    # Iterate over each category
    for category in categories:
        # Retrieve files for the current category
        files = File.objects.filter(category=category)
        # Store files in the dictionary with category as key
        files_by_category[category] = files


    # Pass grouped data to template
    return render(request, 'books/landing.html', {'files_by_category': files_by_category})



def contact(request):
    """
     This function handles the review page.
    
    :param request: The HTTP request object.
    :return: The rendered review page.
    """
    return render(request, 'books/contact.html')


def faqs(request):
    """
     This function handles the FAQS page.
    
    :param request: The HTTP request object.
    :return: The rendered review page.
    """
    return render(request, 'books/faqs.html')


def privacy(request):
    """
     This function handles the Pricacy & Policy page.
    
    :param request: The HTTP request object.
    :return: The rendered review page.
    """
    return render(request, 'books/privacy.html')


def about(request):
    """
    This function handles the about page.
    
    :param request: The HTTP request object.
    :return: The rendered about page.
    """
    return render(request, 'books/about.html')



def pricing(request):
    """
    This function handles the pricing page.
    
    :param request: The HTTP request object.
    :return: The rendered pricing page.
    """
    return render(request, 'books/pricing.html')



def reviews(request):
    """
     This function handles the review page.
    
    :param request: The HTTP request object.
    :return: The rendered review page.
    """
    return render(request, 'books/reviews.html')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')

    else:
        form = SignupForm()

    return render(request, 'books/signup.html', {
        'form': form
    })



def logout(request):
    """
    This function handles the logout page.
    
    :param request: The HTTP request object.
    :return: The rendered logout page.
    """
    return render(request, 'books/logout.html')
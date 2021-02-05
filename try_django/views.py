from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost



def home_page(request):
    my_title = "Hello there ..."
    qs = BlogPost.objects.all()[:5]
    context = {"my_title" : "Welcom to Try Django", "blog_list":qs}
    return render(request, "home.html" , context)



def about_page(request):
    return render(request, "about.html" , {"my_title" : "about "})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "my_title" : "contact us",
        "form": form
    }
    return render(request, "form.html" , context)



def example_page(request):
    context         = {"my_title":"Example"}
    template_name   = "hello_world.html"
    template_obj    = get_template(template_name)
    render_item     = template_obj.render(context)

    return HttpResponse(template_obj.render(context))  #render(request, "hello_world.html" , {"my_title" : "contact us"})

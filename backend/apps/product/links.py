from .models import MyLinks

def get_my_links(request):
    links = MyLinks.objects.latest()
    context = {'links': links}
    return context
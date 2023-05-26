from .models import *
from .views import *

def list_categories(request):
    categories = Category.objects.all()
    data = {'categories': categories}
    return data
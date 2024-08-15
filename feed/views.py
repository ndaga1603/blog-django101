from typing import Any
from django.views.generic import ListView
from .models import Feed

# function based view
# class based view

class HomePage(ListView):
    model = Feed
    template_name = "index.html"

  
from django.shortcuts import render, get_object_or_404
from .models import *


def package_detail(request, id, slug):
    package = get_object_or_404(Package, id=id, slug=slug, available=True)
    return render(request, 'margulan/package/detail.html', {'product': package})



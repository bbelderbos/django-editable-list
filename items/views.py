from urllib.parse import parse_qs

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.middleware.csrf import get_token

from .models import ListItem
from .forms import ListItemBaseForm, ListItemUpdateForm


def index(request):
    items = ListItem.objects.all()
    add_form = ListItemBaseForm()
    return render(
        request,
        "index.html",
        {"items": items,
         "add_form": add_form,
         "csrf_token": get_token(request)},
    )


def update_item(request, pk):
    item = get_object_or_404(ListItem, pk=pk)
    if request.method == "PUT":
        body_data = parse_qs(request.body.decode())
        data = {key: value[0] for key, value in body_data.items()}
        form = ListItemUpdateForm(data, instance=item)
        if form.is_valid():
            item = form.save()
            return render(request, "item.html", {"item": item})
    else:
        form = ListItemUpdateForm(instance=item)
    return render(
        request,
        "item_edit.html",
        {"form": form, "item": item, "csrf_token": get_token(request)},
    )


def add_item(request):
    form = ListItemBaseForm(request.POST)
    if form.is_valid():
        item = form.save()
        return render(request, "item.html", {"item": item})
    return JsonResponse({"success": False})

from .forms import ItemForm
from django.shortcuts import render
from .scripts.downloads_pdf import pdf
from django.http import HttpResponse
import re


def get_property_id(request):
    form = ItemForm()
    context = {"form": form}
    return render(request, "get_property_id.html", context)


def get_pdf(request):
    try:
        property_id = request.POST["property_id"]
        url = (
            "https://whats-that.s3.eu-central-1.amazonaws.com/energy-data/"
            + property_id
            + ".pdf"
        )
    except Exception as error:
        print(error)
    text = pdf(url)
    if text is not None:
        klasifikacija_stavbe = re.search(r"\d{7,8}", text)
        potrebna_teplota = re.search(r"Razred\s\w{1,2}\s{1,3}\d{1,4}", text)
        klasifikacija_stavbe = (
            klasifikacija_stavbe.group(0)
            if klasifikacija_stavbe is not None
            else "Not found"
        )
        potrebna_teplota = (
            f"{potrebna_teplota.group(0)} kWh/m2a"
            if potrebna_teplota is not None
            else "Not found"
        )
        context = {
            "potrebna_teplota": potrebna_teplota,
            "klasifikacija_stavbe": klasifikacija_stavbe,
        }
        return render(request, "result.html", context)
    else:
        return HttpResponse("Page does not exist")

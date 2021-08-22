from django.forms.widgets import Input
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


# Create your views here.
@login_required(login_url="/accounts/login/")
def homepage(request):
    buses = Article.objects.all().order_by('date')
    return render(request, 'main/homepage.html', {'articles': buses})


@login_required(login_url="/accounts/login/")
def bus_details(request, slug):
    # return HttpResponse(slug)
    buses = Article.objects.get(slug=slug)
    return render(request, 'main/bus_details.html', {'article': buses})


@login_required(login_url="/accounts/login/")
def about(request):
    # return HttpResponse("About")
    return render(request, 'main/about.html')


@login_required(login_url="/account/login/")
def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message = request.POST['message-message']
        return render(request, 'main/contact.html', {'message_name': message_name})

    else:
        return render(request, 'main/contact.html')


@login_required(login_url="/account/login/")
def bolaka(request):
    return render(request, 'main/bolaka.html')


@login_required(login_url="/account/login/")
def ticket_page(request):
    return render(request, 'main/ticket_page.html')


@login_required(login_url="/account/login/")
def ticket_page(request):
    message_name = request.POST.get('message-name')
    message_email = request.POST.get('message-email')
    message_phone = request.POST.get('message-phone')

    print(message_name, message_email, message_phone)

    return render(request, 'main/ticket_page.html')


@login_required(login_url="/account/login/")
def ticket(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    print()
    lines = [
        "Line1",
        "Line2",
        "Line3",
        "Line4",
        "Line5",
    ]

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="ticket.pdf")

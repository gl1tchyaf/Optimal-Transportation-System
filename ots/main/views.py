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
from django.core.mail import send_mail


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

        #send email
        send_mail(
            message_name +' '+ message_phone, # subject
            'Sent from '+message_email+ ' \n' + message, #message
            message_email, #from mail
            ['2018-3-60-088@std.ewubd.edu'], #tomail
        )
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
    ticket_page.message_name = request.POST.get('message-name')
    ticket_page.message_email = request.POST.get('message-email')
    ticket_page.message_phone = request.POST.get('message-phone')
    ticket_page.message_start = request.POST.get('message-start')
    ticket_page.message_end = request.POST.get('message-end')
    ticket_page.message_date = request.POST.get('message-date')

    return render(request, 'main/ticket_page.html', {'message_name': ticket_page.message_name})


@login_required(login_url="/account/login/")
def ticket(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    name=ticket_page.message_name
    mail=ticket_page.message_email
    phone=ticket_page.message_phone
    start= ticket_page.message_start
    end = ticket_page.message_end

    lines = [
        name,
        mail,
        phone,
        start,
        end,
        ticket_page.message_date

    ]

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="ticket.pdf")

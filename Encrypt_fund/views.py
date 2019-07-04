from django.core.mail import EmailMessage
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string

from Encrypt_fund.models import Subscribe


def index(request):
    if request.method == "POST":
        if request.POST.get('email'):
            sub = Subscribe()
            sub.email = request.POST.get('email')
            sub.save()
            mail_subject = 'Thank you For Subscribing'
            message = render_to_string('sub_email.html')
            to_email = request.POST.get('email')
            email = EmailMessage(
                mail_subject, message, to= [to_email]
            )
            email.send()
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')


def roadmap(request):
    return render(request, 'Roadmap.html')


def demo_piechart(request):
    """
    pieChart page
    """
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]

    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return render_to_response('piechart.html', data)

from django.shortcuts import render
from .models import Parcel
import random
from urllib.parse import quote

def add_parcel(request):
    if request.method == 'POST':
        tracking_id = "TRK" + str(random.randint(1000,9999))

        parcel = Parcel.objects.create(
            tracking_id=tracking_id,
            sender_name=request.POST['sender_name'],
            receiver_name=request.POST['receiver_name'],
            pickup_location=request.POST['pickup_location'],
            delivery_location=request.POST['delivery_location'],
            weight=request.POST['weight'],
        )

        # 📱 WhatsApp logic
        phone = request.POST.get('phone')

        message = f"Hello, your parcel is booked.\nTracking ID: {tracking_id}\nTrack here: http://127.0.0.1:8012/parcel/track/"
        encoded_msg = quote(message)

        # ✅ BEST LINK (mobile + web both)
        whatsapp_url = f"https://api.whatsapp.com/send?phone=91{phone}&text={encoded_msg}"

        return render(request, 'success.html', {
            'tracking_id': tracking_id,
            'whatsapp_url': whatsapp_url
        })

    return render(request, 'add_parcel.html')
def parcel_list(request):
    parcels = Parcel.objects.all()
    return render(request, 'parcel_list.html', {'parcels': parcels})

def track_parcel(request):
    data = None
    if request.method == 'POST':
        tracking_id = request.POST['tracking_id']
        try:
            data = Parcel.objects.get(tracking_id=tracking_id)
        except:
            data = None

    return render(request, 'track.html', {'data': data})

from django.shortcuts import render
from .models import Parcel

def dashboard(request):
    total = Parcel.objects.count()
    delivered = Parcel.objects.filter(status='Delivered').count()
    pending = Parcel.objects.filter(status='Pending').count()
    transit = Parcel.objects.filter(status='In Transit').count()

    context = {
        'total': total,
        'delivered': delivered,
        'pending': pending,
        'transit': transit,
    }

    return render(request, 'dashboard.html', context)

from urllib.parse import quote

def update_status(request, id):
    parcel = Parcel.objects.get(id=id)

    if request.method == 'POST':
        new_status = request.POST['status']
        parcel.status = new_status
        parcel.save()

        # 📱 WhatsApp message
        phone = request.POST.get('phone')

        message = f"Update: Your parcel ({parcel.tracking_id}) is now {new_status}."
        encoded_msg = quote(message)

        whatsapp_url = f"https://wa.me/91{phone}?text={encoded_msg}"

        return render(request, 'update_success.html', {
            'parcel': parcel,
            'whatsapp_url': whatsapp_url
        })

    return render(request, 'update_status.html', {'parcel': parcel})


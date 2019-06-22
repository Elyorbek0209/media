from django.shortcuts import render

#Here importing Destination From models
from .models import Destination



# Create your views here.
def index(request):


# Here we'll create an Object for Destionation
    dest1 = Destination()

    dest1.name = 'Tashkent'

    dest1.desc = 'The City is very Delicious Food'

    dest1.price = 300

    dest1.img = 'destination_1.jpg'

    dest1.offer = False



    dest2 = Destination()

    dest2.name = 'Andijan'

    dest2.desc = 'The City is the king Babur born'

    dest2.price = 400

    dest2.img = 'destination_3.jpg'

    dest2.offer = True



    dest3 = Destination()

    dest3.name = 'Fergana'

    dest3.desc = 'The City is full of beauty'

    dest3.price = 400

    dest3.img = 'destination_6.jpg'

    dest3.offer = False


    # Here we are creating a List from that above 3 Data
    dests = [dest1, dest2, dest3]

   # dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})


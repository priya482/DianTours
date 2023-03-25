from django.contrib import admin
from .models import Packages
from .models import Address
from .models import Admin
#from .models import Customer
from .models import Agent
from .models import Hotel
from .models import Booking
from .models import Payment
from .models import Cancellation
from .models import Enquiry
from .models import Feedback
#from .models import 

# Register your models here.
admin.site.register(Packages)
admin.site.register(Address)
admin.site.register(Admin)
admin.site.register(Agent)
admin.site.register(Hotel)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Cancellation)
admin.site.register(Enquiry)
admin.site.register(Feedback)

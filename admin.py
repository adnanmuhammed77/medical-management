from django.contrib import admin
from . models import Departments, product,Doctors,Booking

# Register your models here.
class productadmin(admin.ModelAdmin):
    list_display=('name','price','image')

admin.site.register(product,productadmin)



admin.site.register(Departments)
admin.site.register(Doctors)

class BookAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','P_email','doc_name','booking_date','booked_on')
admin.site.register(Booking,BookAdmin)

admin.site.site_header="APOLLO HOSPITAL"

admin.site.index_title="welcome admin"
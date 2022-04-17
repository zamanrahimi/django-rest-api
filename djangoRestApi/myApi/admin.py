from django.contrib import admin

# Register your models here.

## create restApi - section 1


from .models import Student

admin.site.register(Student) 


#follow the bellow steps 

# 1. admin
# 2. model
# 3. serializer
# 4. url
# 5.view
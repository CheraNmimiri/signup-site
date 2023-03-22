# signup-site
Lesson project for making a site for sign up and login

				make projecet and app and make front

1-& django-admin startproject [projectname] #for make project and file of that
2-& manage.py runserver [port:optional] #baray run kardan server va ereftan link
3-ba dastor manage.py startapp [appname] ye app misazim va be setting ham add mikonim.
4-make folder [templates] and import html file to that.
5-make static file and within that make 3 folder for javascript and css and img files.
6-next going to setting and find [TEMPLATES] section 
7- next find 'DIRS' : [BASE_DIR , 'templates']
8- next copy this on the setting but end of that
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
9-varded views toy dir app mishim ba tavabe ro ba html page ha tarif mikonim.
copy that is code on that:
from django.shortcuts import render

def home(request):
    return render(request,"htmllogin.html")
 
11-vared urls.py project mishim va onja aval directory views.py ro ke toy directory app ma hast beheshe mishnasonim.
from appname.views import defs
    
12- and write in urlpattersns that

	path('',defname),

TIP= BARAY KAR BA CSS DASTOR MANAGE.PY COLLECTSTATIC YADET NARE.


					create admin page and access to users
1-uese command manage.py migrate # az in baray sakht ye database estefade mishe
2-use command manage.py createsuperuser
3-next going to urls and import that
from django.contrib import admin

4-make a path seems that:
path("admin/", admin.site.urls),

5-next you have access to admin page



                                sakht sign in page
1-vared views.py shode va in ha ro import mikonim ta az on baray method sakht sign in estefade konim.
	from django.contrib.auth.forms import UserCreationForm
2-bad dastorat zir ro vared mikonim.dastorat zir ye class ro farakhani mikonan ke ma ono toy file html sing in estefade mikonim va bara ma ye ghaleb amade dorost mikone va be on marhale ham miresim.

	def signup(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}

3- hala vared file html marbot be sign in mishim va bad az sakht base har html toy body ye form dorost mikonim be skhakl zir va bad class form ro fara mikhonim ta ghaleb ro baramon besaze. be alave ye input baray vorodi ham estefade mikoin ke bahash dade haro taeed konim.
	 <form method="POST" action="">
       # code hay html ma injan va ma bayad zir har lable ye {{form.username}} ya ... gharar bedim be onvan field
# darbare shenasondan ina sohbat mikonim
    
  </form>
4- hala runserver mikonim va bad ye sign up mikonim va mitonim az bakhsh admin ham ezafe shodan on ro bbinim.

					

							ejad directory forms baray gereftan dade bishtar
1-ye directory be esm forms.py besaz.
2- hame script hay zir ro tosh copy kon,
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

3-ba ina behesh migi man in dade haro mikham va django mishnase




					bazgasht be safhe login bad az signup

1-baray ejad url va html o css ravand moshabe signup hast.
2-hala vared views mishim [redirect] ro import mikonm vaghal render.
3-be tabe signup va zir form.save() in ebarat ro ezaf mikonim.
            return redirect(login)
ba in kar belafasele bad az sinup shakhs vared login page mishe.

				
					ejad pegham khata zir har field
1-in ro import mikonim
from django.contrib import messages





						make log in and log out

1- aval be view mirim va in ro import mikonim.
from django.contrib.auth import authenticate,login , logout
2- tabe login ma ine 
def login(request):
    def loginpage(request):   # khod tabe
    if request.method == 'POST': # agar az method post dade gerefti
        username=request.POST.get("username")  #dade toy field user name ro begir(niaz be taghir dar input html username)
        password=request.POST.get("password")  #dade toy field password ro begir (niaz be taghir dar input html password)
        user = authenticate(request , username=username , password=password) #taeen moteghayer baray dade hay ersali
        if user is not None: # agar dade ha khali nabodan
            login(request , user ) #amal login ro anjam bede
            return redirect(home) # agar dorost bod bargard be page home
	  else:
        messages.info(request,"User name or password incorrect") #halat ghalt bodan info
        return render(request,"login.html" , context)
    
    
    context={}
    return render(request,"login.html" , context)


3- baray in ke matn error namayesh dade beshe be akhar file html login ino ezafe mikonim.
{% for message in messages%}
    <p id ="messages" > {{message}}<p>
     {% endfor %} 
						
	

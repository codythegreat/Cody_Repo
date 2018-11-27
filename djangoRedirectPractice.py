#views.py
from django.shortcuts import redirect

def redirect_view(request):
	response = redirect('/redirect_success/')
	return response

##########################################

# urls.py
from django.urls import path

from .views import redirect_view

urlpatterns = [
	path('/redirect/', redirect_view)
]

##########################################

from django import forms
from django.http import HttpResponseReirect
from django.shortcuts import redirect, render

def send_message(name, message):
	# this is where code for actually sending the message would go

class ContactForm(forms.form):
	name = forms.CharField()
	message = forms.CharField(widget=forms.TextArea)

def contact_view(request):
	# the request method POST will indicate that the form was submitted
	if request.method == 'POST':
		# create a form instance with the submitted data:
		form = ContactForm(request.POST)
		# validate the form:
		if form.is_valid():
			# if the form is valid we will send the message (or do 
			# something else with it.)
			send_message(
				form.cleaned_data['name'],
				form.cleaned_data['message']
			)
			# after the operation is successful we will need to 
			# redirect the user to another page:
			return redirect('/thank-you/')
	else:
		# Create an empty instance:
		form = ContactForm()

	return render(request, 'contact_form.html', {'form': form})

##########################################

def hand_crafted_redirect_view(request):
	response = HttpResponse(status=302)
	response['Location'] = '/redirect/success/'
	return response

##########################################

def redirect_view(request):
	return HttpResponseReirect('/redirect/success')

##########################################

from django.shortcuts import redirect

def model_redirect_view(request):
	product = Product.objects.filter(featured=True).first()
	return redirect(product)

##########################################

from django.shortcuts import redirect

def fixed_featured_product_view(request):
	...
	product_id = settings.FEATURES_PRODUCT_ID
	return redirect('product_detail', product_id=product_id)

##########################################

from django.shortcuts import redirect

def features_product_view(request):
	return redirect('/products/42/')

##########################################

# urls.py
from django.urls import path
from .views import SearchRedirectView

urlpatterns = [
	path('/search/<term>/', SearchRedirectView.as_view())
]

# views.py
from django.views.generic.base import RedirectView

class SearchRedirectView(RedirectView):
	url = 'https://google.com/?q=%(term)s'

##########################################

from django.views.generic.base import RedirectView

urlpatterns = [
	path('/search/term/',
		 RedirectView.as_view(url='https://www.google.com/?q=%(term)s'))
]

##########################################

from random import choice
from django.views.generic.base import RedirectView

class RandomAnimalView(RedirectView):

	animal_urls = ['/dog/', '/cat/', '/parrot/']
	is_permanent = True

	def get_redirect_url(*args, **kwargs):
		return choice(self.animal_urls)

##########################################

from random import choice
from dfango.shortcuts import redirect

def random_animal_view(request):
	animal_urls = ['/dog/', '/cat/', '/parrot/']
	return redirect(random(animal_urls))

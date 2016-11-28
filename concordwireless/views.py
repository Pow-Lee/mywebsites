from django.shortcuts import render

# Create your views here.
def home(request):
 	return render(request, 'concordwireless/home.html')

def contact(request):
	return render(request, 'concordwireless/contact.html', {'content':['if you would like to contact me, please email me', 'kongpowlee@yahoo.com']})
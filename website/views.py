from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


# def wiki_context_processor(request):
#     return {
#         'Business_Name': 'Dental World',
# 			'Business_Address': 'Hous#01 Road#12 Sector#22 Uttara, Dhaka 1230, Bangladesh.',
# 			'Business_Email': 'info@dentalworld.com',
# 			'Facebook_Link': 'https://www.facebook.com/Sochetonota/',
# 			'Twitter_Link': '#',
# 			'Google_Plus_Link': '#',
# 			'LinkedIn_Link': '#',
#     }


# def getWikiContext(self, view, request):
#         context = {
#             'Business_Name': 'Dental World',
# 			'Business_Address': 'Hous#01 Road#12 Sector#22 Uttara, Dhaka 1230, Bangladesh',
# 			'Business_Email': 'info@dentalworld.com',
# 			'Facebook_Link': 'https://www.facebook.com/Sochetonota/',
# 			'Twitter_Link': '#',
# 			'Google_Plus_Link': '#',
# 			'LinkedIn_Link': '#',
#         }

#         return context


def home(request):
	# context = wiki_context_processor(request)
	return render(request, 'home.html', {})

def contact(request):

	if request.method == 'POST':
		message_name = request.POST['message-name'] 
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send and email
		send_mail(
			'message from ' + message_name, # subject
			message, # message
			message_email, # from email
			['rabbanii@gmail.com'], # to email
		)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})

def gallery(request):
	return render(request, 'gallery.html', {})

def about(request):
	return render(request, 'about.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def service(request):
	return render(request, 'service.html', {})

def appointment(request):

	if request.method == 'POST':
		your_name = request.POST['your-name'] 
		your_phone = request.POST['your-phone'] 
		your_email = request.POST['your-email'] 
		your_address = request.POST['your-address'] 

		# your_schedule = request.POST['your-schedule'] 
		your_day = request.POST['your-day']

		your_time = request.POST['your-time'] 
		your_message = request.POST['your-message'] 

		# message_name = request.POST['message-name'] 
		# message_email = request.POST['message-email']
		# message = request.POST['message']

		# send and email

		appointment = "Name: "+ your_name + "\nPhone: "+ your_phone +	"\nEmail: "+ your_email +	"\nAddress: "+ your_address +	"\nDay: "+ your_day +	"\nTime: "+ your_time +"\nMessage: "+ your_message

		send_mail(
			'Appointment Request from '+ your_name, # subject
			appointment, # message
			your_email, # from email
			['rabbanii@gmail.com'], # to email
		)

		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_day': your_day,
			'your_time': your_time,
			'your_message': your_message
		})

	else:
		return render(request, 'home.html', {})


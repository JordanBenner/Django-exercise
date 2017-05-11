from django.template.response import TemplateResponse
from django import forms, http
from .forms import ContactForm
from django.core.mail import send_mail


def homepage(request):
  context = {
    'page_title': 'Home Page',
    'name': 'John Madden',
    'numbers': [1, 2, 3, 4]
  }
  return TemplateResponse(request, 'base.html', context, {})


def thanks(request):
  return TemplateResponse(request, 'thanks.html', {})


def hello(request):
  form = NameForm(request.POST or None)

 if request.method == 'POST':
    if form.is_valid():
      send_email()
      return http.HttpResponseRedirect('/thanks/')

 context= {
    'form':form
  }
  return TemplateResponse(request, 'hello.html', context, {})

def contact_me(request):
  form  = ContactForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      send_mail(
        form.cleaned_data['your_name'],
        form.cleaned_data['your_question'],
        form.cleaned_data['your_email'],
        ['benner281@gmail.com'],
        fail_silently=False,
      )
      return http.HttpResponseRedirect('/thanks/')


 context = {
    'form':form
    }
  return TemplateResponse(request, 'contact_me.html', context)



# from django.template.response import TemplateResponse
# from django import forms, http
# from django.core.mail import EmailMessage
# from django.shortcuts import redirect
# from django.template import Context
# from django.template.loader import get_template
# #
# #
# # class ContactForm(forms.Form):
#     contact_name = forms.CharField(required=True)
#     contact_email = forms.EmailField(required=True)
#     content = forms.CharField(
#         required=False,
#         widget=forms.Textarea
#     )
#
#
# def __init__(self, *args, **kwargs):
#     super(ContactForm, self).__init__(*args, **kwargs)
#     self.fields['contact_name'].label = "Your name:"
#     self.fields['contact_email'].label = "Your email:"
#     self.fields['content'].label = "What do you want to say?"
#
#
# def index(request):
#     context = {
#         'page_title': 'HOME PAGE'
#
#     }
#     return TemplateResponse(request, 'index.html', {})
#
#
# def contact(request):
#     form_class = ContactForm
#
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#     #         return http.HttpResponseRedirect('/thanks/')
#     # context = {
#     #     'form': form
#     # }
#
#     if request.method == 'POST':
#         form = form_class(data=request.POST)
#
#         if form.is_valid():
#             contact_name = request.POST.get(
#                 'contact_name', '')
#             contact_email = request.POST.get(
#                 'contact_email', '')
#             form_content = request.POST.get('content', '')
#
#             template = get_template('contact_template.txt')
#             context = Context({
#                 'contact_name': contact_name,
#                 'contact_email': contact_email,
#                 'form_content': form_content,
#             })
#             content = template.render(context)
#
#             email = EmailMessage(
#                 "New contact form submission",
#                 content,
#                 "Your website" + '',
#                 ['benner281@gmail.com'],
#                 headers={'Reply-To': contact_email}
#             )
#             email.send()
#             return redirect('contact')
#
#     return TemplateResponse(request, 'contact.html',  context)
#           'form': form_class,
#      })

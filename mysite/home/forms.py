from django import forms

class MessageForm(forms.Form):
	name = forms.CharField(label='name', max_length=32)
	email = forms.EmailField(label='email', max_length=32)
	subject = forms.CharField(label='subject', max_length=64)
	
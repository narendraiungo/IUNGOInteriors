from django.contrib.auth.forms import UserCreationForm
from django.forms import Select
from .models import IungoUser
from django import forms
from django.apps import apps


class RegistrationForm(UserCreationForm):
	# client_category = forms.ChoiceField(widget=forms.Select)
	class Meta:
		model = IungoUser
		fields= ['username','email','first_name','last_name','ClientType','client_category','ProfileImage']
		widgets = {
			'client_category': Select(attrs={'class': 'select'}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['client_category'].queryset = None

		if 'ClientType' in self.data:
			try:
				client_type = self.data.get('ClientType')
				model = apps.get_model('LIstings', self.data.get('ClientType'))
				print(self.data.get('client_category'))
				# import pdb;pdb.set_trace()
				self.fields['client_category'].queryset = model.objects.get(name=self.data.get('client_category'))
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty  queryset

from django import forms
from rango.models import Tapa, Bar, UserProfile
from django.contrib.auth.models import User

class BarForm(forms.ModelForm):
    nombre = forms.CharField(max_length=30, help_text="Nombre:")
    direccion = forms.CharField(max_length=50, help_text="Dirección:")
    num_visitas = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Bar
        fields = ('nombre','direccion',)
        exclude = ('num_visitas','slug',)


class TapaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=30, help_text="Introduce el nombre de la tapa.")
    votos = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tapa

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('bar','votos',)
        #or specify the fields to include (i.e. not include the category field)
        fields = ('nombre',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

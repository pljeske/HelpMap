from django import forms
from django.contrib.auth.forms import UserCreationForm
from registration.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text="Pflichtfeld. Bitte geben Sie eine gültige Mailadresse an!")
    first_name = forms.CharField(max_length=100, required=True, label="Vorname")
    last_name = forms.CharField(max_length=100, required=True, label="Nachname")

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for label in ['username']:
            self.fields[label].label = 'Username'
            self.fields[label].help_text = 'Pflichtfeld. 150 Zeichen oder weniger. Buchstaben, Zahlen und @/./+/-/_ ' \
                                           'sind erlaubt.'

        for label in ['password1']:
            self.fields[label].label = 'Passwort'
            self.fields[label].help_text = '<ul><li>Bitte wählen Sie kein rein numerisches Passwort</li><li>mit ' \
                                           'mindestens 8 Zeichen.</li>' \
                                           '<li>ohne einen Bezug auf Ihre persönlichen Daten.</li>' \
                                           '<li>Bitte vermeiden Sie die Nutzung eines zu einfachen Passwortes.</li>'

        for label in ['password2']:
            self.fields[label].label = 'Passwort bestätigen'
            self.fields[label].help_text = 'Bitte bestätigen Sie die Eingabe Ihres Passwortes erneut.'


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Passwort")


class ProfileForm(forms.Form):
    picture = forms.ImageField(required=True, label="Neues Profilbild hochladen")

from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, label="username")
    password = forms.CharField(
        label="password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )



  
  
    # name = forms.CharField(max_length=30, label='Name')
    # firstname = forms.CharField(max_length=30, label='Firstame')
    # email = forms.EmailField(max_length=254, label='Email')
    # picture = forms.ImageField(label='Profile Picture', required=False)
    # password1 = forms.CharField(
    #     label="Password",
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    # )
    # password2 = forms.CharField(
    #     label="Password confirmation",
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    #     strip=False,
    # )
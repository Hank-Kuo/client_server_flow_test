from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User,Token
from django.contrib  import auth


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','token')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class LoginForm(forms.Form):
    username = forms.CharField(label='USERNAME' ,
                                widget = forms.TextInput(attrs={'class':'au-input au-input--full','placeholder' : "Username"}),
                                )
    password = forms.CharField(label='PASSWORD',
                                widget = forms.PasswordInput(attrs={'class':'au-input au-input--full','placeholder' : "Password"}))
    def clean(self):
        username = self.cleaned_data['username'] #process valid 
        password  = self.cleaned_data['password']
        user = auth.authenticate(username=username,password=password)
        if user is None :
            raise forms.ValidationError('user wrong or password wrong')
        else:
            self.cleaned_data['user']=user
        return  self.cleaned_data

class RegForm(forms.Form):
    username = forms.CharField(label='USER' ,
                                max_length=30,
                                min_length=3,
                                widget = forms.TextInput(attrs={'class':'au-input au-input--full','placeholder' : "username"}),
                                )
    
    password = forms.CharField(label='PASSWORD',
                                min_length= 6,
                                widget = forms.PasswordInput(attrs={'class':'au-input au-input--full','placeholder' : "password"}),
                                )
    password_again = forms.CharField(label='PASSWORD AGAIN',
                                    min_length = 6,
                                    widget = forms.PasswordInput(attrs={'class':'au-input au-input--full','placeholder' : "password again"}),
                                    )
    token = forms.CharField(label='TOKEN',
                                    min_length = 6,
                                    widget = forms.TextInput(attrs={'class':'au-input au-input--full','placeholder' : "token"}),
                                    )  
    class Meta:
        model = User
        fields = ['username','password', 'password_again', 'token'] 
    
    def clean_username(self):
        username=self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("the user exist")
        return username

    def clean_password_again(self):
        password = self.cleaned_data["password"]
        password_again = self.cleaned_data["password_again"]
        if password != password_again:
            raise forms.ValidationError("password wrong")
        return password_again

    def clean_token(self):
        token = self.cleaned_data['token']
        if(Token.objects.filter(token = token).exists()):
            if(Token.objects.filter(token = token).values("is_valid")[0]["is_valid"]==False):
                raise forms.ValidationError("token already used")
        else :
            raise forms.ValidationError("token is wrong")
        return token
        
    def save(self, commit=True):
        db = User.objects.create_user(username=self.cleaned_data['username'],token=self.cleaned_data['token'],password = self.cleaned_data['password'],is_staff=True)
        Token.objects.filter(token = self.cleaned_data['token']).update(username=self.cleaned_data['username'])
        Token.objects.filter(token = self.cleaned_data['token']).update(is_valid=False)
        db.save()
        return db

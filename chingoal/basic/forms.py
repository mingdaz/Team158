from django import forms

from django.contrib.auth.models import User

from message_models, post_models, question_models, user_models import *

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length = 30)
    password1 = forms.CharField(max_length = 200, label = 'Password',
        widget = forms.PasswordInput())
    password2 = forms.CharField(max_length = 200, label = 'Confirm Password',
        widget = forms.PasswordInput())
    email = forms.EmailField()
    identity = forms.IntegerField() # 0 For student 1 For teacher


    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact = username):
            raise forms.ValidationError('Username is already taken!')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__exact = email):
            raise forms.ValidationError('Email address is registered!')
        return email

    def clean_identity(self):
        identity = self.cleaned_data.get('identity')
        if identity != 0 && identity != 1:
            raise forms.ValidationError('Identity can only be teacher or student!')



class EditProfileForm(forms.Form):
    username = forms.CharField(max_length = 30)
    
    def clean(self):
        cleaned_data = super(EditProfileForm, self).clean()
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact = username):
            raise forms.ValidationError('Username is already taken!')
        return username


class EditScheduleForm(forms.Form):
    progress_level = forms.IntegerField()
    progress_lesson = forms.IntegerField()

    def clean(self):
        cleaned_data = super(EditScheduleForm, self).clean()

    ## TODO clean_process_level clean_process_lesson


class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(max_length = 200, label = 'Password',
        widget = forms.PasswordInput())
    password2 = forms.CharField(max_length = 200, label = 'Confirm Password',
        widget = forms.PasswordInput())

    def clean(self):
        # Get dictionary of cleaned data
        cleaned_data = super(ResetPasswordForm, self).clean()
        # Check two passwords match
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")
        # return cleaned data
        return cleaned_data



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('author', 'post_time', )


class WTForm(forms.ModelForm):
    class Meta:
        model = Word_Translation


class MCForm(forms.ModelForm):
    class Meta:
        model = Multiple_Choice


class TestForm(forms.ModelForm):
    class Meta:
        model = Test


class LearnForm(forms.ModelForm):
    class Meta:
        model = Learn

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'post_time', )


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        exclude = ('author', 'post_time', 'reply_to')



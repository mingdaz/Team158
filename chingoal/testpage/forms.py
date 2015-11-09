from django import forms

class MCQFrom(forms.Form):
    question = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Choice Text'}))
    a = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Choice Text'}))
    b = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Choice Text'}))
    c = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Choice Text'}))
    d = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Choice Text'}))
    explanation = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Explanation'}))
    def clean(self):
        cleaned_data = super(MCQFrom, self).clean()
        return cleaned_data

class TRQFrom(forms.Form):
    question = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Question'}))
    explanation = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Answer'}))
    def clean(self):
        cleaned_data = super(TRQFrom, self).clean()
        return cleaned_data


# class TestFrom(forms.ModelForm):
#     # shortbio = forms.CharField( widget=forms.Textarea, required = False)
#     class Meta:
#         model = MyUser
#         exclude  = ( 'user','follow' )
#         widgets = {'myimg' : forms.FileInput(),'shortbio':forms.Textarea()}
#     def clean(self):
#         # Checks the validity of the form data
#         cleaned_data = super(ProfileForm, self).clean()
#         return cleaned_data

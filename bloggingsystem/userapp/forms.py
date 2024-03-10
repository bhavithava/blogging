from django import forms
from .models import *

class OpenBlogForm(forms.ModelForm):
    class Meta:
        model = OpenBlog
        fields = ['name', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super(OpenBlogForm, self).__init__(*args, **kwargs)


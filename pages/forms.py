from django import forms 
from posts.models import Post 
  
class CreatePost(forms.ModelForm): 
    class Meta: 
        model = Post 
        fields = [ "context", "image",] 
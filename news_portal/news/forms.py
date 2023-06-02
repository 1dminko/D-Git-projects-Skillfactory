
from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
            'id_author',
            'id_cat',
            'state_news',
            'article',
            'text',
        ]

class CategoryForm(forms.ModelForm):
   class Meta:
       model = Category
       fields = [
            'name_cat',
       ]
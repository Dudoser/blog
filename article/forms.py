#-*- coding: utf-8 -*-
from django.forms import ModelForm, fields
from models import Comments

class CommentForm(ModelForm):
    class Meta():
        model = Comments
        fields = ['comments_text']
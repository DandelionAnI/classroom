# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100, widget=forms.TextInput(attrs={
        'class': 'username', 'placeholder': '用户名', 'autocomplete': 'off'
    }))
    password = forms.CharField(label='密__码', widget=forms.PasswordInput(attrs={
        'class': 'password',
        'placeholder': '密码',
        'oncontextmenu': 'return false',
        'onpaste': 'return false',
    }))
    college = forms.IntegerField(widget=forms.Select(attrs={
        'style': 'appearance: none; -moz-appearance: none; -webkit-appearance: none; width: 100%;',
        'class': 'btn btn-default dropdown-toggle',
        'data-toggle': 'dropdown',
        'aria-haspopup': 'true',
        'aria-expanded': 'false',
    }))
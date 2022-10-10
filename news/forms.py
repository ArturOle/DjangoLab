from django import forms

class NewsForm(forms.Form):

    topic = forms.CharField(label = 'topic', max_length = 100)
    text = forms.CharField(label = 'text', max_length = 200)
    author = forms.CharField(label = 'author', max_length = 100)


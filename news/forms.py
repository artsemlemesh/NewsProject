from django import forms
from django.core.exceptions import ValidationError

from .models import News

class NewsForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = News
        fields = [
            'name',
            'description',
            'category',
        ]


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')



        if name == description:
            raise ValidationError(
                'description cannot be identical to the name'
            )

        return cleaned_data
# from news.forms import NewsForm
# f = NewsForm({'name': 'hello', 'description': 'hello', 'category': 'Sport'})
# f.is_valid()
# f.errors
from django import forms
from tinymce.widgets import TinyMCE
from django.utils.translation import ugettext_lazy as _
from .models import Article


#
# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False



class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        # kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)


class ArticleForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(
            attrs={'required': False, 'cols': 10, 'rows': 30}
        ))
    short_description = forms.CharField(
        widget=TinyMCE(
            attrs={'required': False, 'cols': 10, 'rows': 10}
        )
    )
    # date_published = forms.DateTimeField(
    #         input_formats=['%d/%m/%Y %H:%M'],
    #         widget=forms.DateTimeInput(attrs={
    #             'class': 'form-control datetimepicker-input',
    #             'data-target': '#datetimepicker1'
    #         })
    #     )
    # def clean_article(self):
    #     data = self.cleaned_data['tag']
    #     data = self.cleaned_data['category']
    #     data = self.cleaned_data['title']
    #     data = self.cleaned_data['author']
    #     data = self.cleaned_data['short_description']
    #     data = self.cleaned_data['content']
    #     data = self.cleaned_data['published_status']
    #     data = self.cleaned_data['visibility']
    #     data = self.cleaned_data['date_published']
    #     data = self.cleaned_data['is_featured']

    class Meta:
        model = Article
        fields = ['title','author',
                  'short_description','content','published_status','tag','category',
                  'visibility','date_published','is_featured']
        help_texts = {'short_description': _('Intro description only shown on blogs main page.')}
        labels = {
                "tag": _("Tag"),
                "category": _("Category"),
                "title": _("Title"),
            }
        widgets = {
            'date_published': DateInput(format=["%Y-%m-%d"])
        }

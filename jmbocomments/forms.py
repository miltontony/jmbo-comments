from django.contrib.comments.forms import CommentForm
from django import forms

from jmbocomments.models import UserComment, REPORT_CATEGORY_CHOICES
from jmbocomments.forms import UserCommentForm


class UserCommentForm(UserCommentForm):
    email = forms.EmailField(required=False)
    category = forms.IntegerField(required=True,\
                widget=forms.RadioSelect(choices=REPORT_CATEGORY_CHOICES))


    def get_comment_model(self):
        # this is not really needed anymore, as was used by function below.
        return UserComment

    def get_comment_object(self):
        # removed check for duplicates code.
        return UserComment(**self.get_comment_create_data())

    def get_comment_create_data(self):
        data = super(UserCommentForm, self).get_comment_create_data()
        del data['user_name']
        del data['user_email']
        del data['user_url']
        data['like_count'] = 0
        return data

    def clean_timestamp(self):
        # allows you to cache page that includes comments for longer than 2 hours.
        return self.cleaned_data['timestamp']

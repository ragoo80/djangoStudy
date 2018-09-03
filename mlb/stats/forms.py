# -*- coding: utf-8 -*-

# 1. manage.py makemigrations
# 2. manage.py migrate

# ----------------------------------------------------------------------------------------------------
# 아래 주소 내용 테스트 해볼것 validator추가, messages 모듈 사용
# https://lhy.kr/lecture/django/instagram/06.message-framework

#https://blog.hannal.com/2015/05/start_with_django_webframework_07/

# apply css to form field
# https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html
# ----------------------------------------------------------------------------------------------------


from django import forms
from sql.model.testModel import Post

class PostForm(forms.ModelForm) :
    class Meta:
        model = Post
        fields = ('title', 'text')

# ----------------------------------------------------------------------------------------------------
# class Post(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#         default=timezone.now)
#     published_date = models.DateTimeField(
#         blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title
# ----------------------------------------------------------------------------------------------------


# forms.Form, forms.ModelForm -> 2가지 경우 있음
# 일반 폼으로 PostForm을 구성하는 경우의 코드
class testForm(forms.Form) :
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    # emailInput = forms.EmailInput(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='write here your message!'
    )
    # A hidden input for internal use
    # tell from which page the user sent the message
    source = forms.CharField(
        max_length=50,
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(testForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        # emailInput = cleaned_data.get('emailInput')
        message = cleaned_data.get('message')

        if not name and not email and not message :
            raise forms.ValidationError('you have to write something')


# ----------------------------------------------------------------------------------------------------

class CommentForm(forms.Form):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'content',
                'placeholder': '댓글 달기...',
            }
        )
    )
    def clean_content(self):
        data = self.cleaned_data['content']
        errors = []
        if data == '':
            errors.append(forms.ValidationError('댓글 내용을 입력해주세요'))
        elif len(data) > 50:
            errors.append(forms.ValidationError('댓글 내용은 50자 이하로 입력해주세요'))
        if errors:
            raise forms.ValidationError(errors)
        return data


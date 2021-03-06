from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=140, 
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목을 입력바랍니다.',
            }
        )
    )
    content = forms.CharField(
    # label 내용 수정
        label='내용',
        # Django form에서 HTML 속성 지정 -> widget을 통해서
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': '내용을 입력바랍니다.',
                'rows': 5,
                'cols': 60
            }
        )        
    )
    class Meta:
        model = Article
        fields = '__all__'
        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'placeholder': '제목을 입력바랍니다.'
        #         }
        #     )
        # }
        # fields = ('title',)



 
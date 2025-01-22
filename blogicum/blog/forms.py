from django import forms
from blog.models import Comment, Post, User, Location, Category


class PostForm(forms.ModelForm):
    """
    Форма для создания или редактирования публикации (Post).
    """

    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateTimeInput(format='%Y-%m-%dT%H:%M',
                                            attrs={'type': 'datetime-local'})
        }


class CommentForm(forms.ModelForm):
    """
    Форма для создания или редактирования комментария (Comment).
    """

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'cols': 10, 'rows': 10})
        }


class UserForm(forms.ModelForm):
    """
    Форма для создания или редактирования пользователя (User).
    """
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

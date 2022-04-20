from tkinter import Widget
from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):

    title = forms.CharField(
        max_length=50,
        label = "Title",
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control'
            }
        )
    )

    issue_a = forms.CharField(
        max_length=20,
        label = "Issue a",
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control'
            }
        )
    )


    issue_b = forms.CharField(
        max_length=20,
        label = "Issue b",
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control'
            }
        )
    )


    class Meta:
        model = Question
        fields = '__all__'



class CommentForm(forms.ModelForm):

    pick_A = "Blue"
    pick_B = "Red"
    pick_choice = [
        (pick_A, 'Blue'),
        (pick_B, 'Red'),
    ]

    pick = forms.ChoiceField(
        label = "pick",
        choices = pick_choice,
        widget=forms.Select(
            attrs={
                'class' : 'form-select'
            }
        )
    )

    content = forms.CharField(
        max_length=100,
        label = "content",
        widget=forms.TextInput(
            attrs = {
                'class' : 'form-control'
            }
        )
    )

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('que',)
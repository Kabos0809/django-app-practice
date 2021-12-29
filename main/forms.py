from django import forms
from django.forms import fields, widgets
from .models import CustomUser, article_form
from datetime import datetime
from django.contrib.auth.forms import ReadOnlyPasswordHashField
class categorie_form(forms.Form):

    

    title = forms.CharField(max_length=30)
    comments = forms.CharField(widget=forms.Textarea(attrs={'cols':'80', 'rows':'10'}))

    rank = (
    ('ブロンズ4', 'ブロンズ4'), ('ブロンズ3', 'ブロンズ3'), ('ブロンズ2', 'ブロンズ2'), ('ブロンズ1', 'ブロンズ1'),
    ('シルバー4', 'シルバー4'), ('シルバー3', 'シルバー3'), ('シルバー2', 'シルバー2'), ('シルバー1', 'シルバー1'),
    ('ゴールド4', 'ゴールド4'), ('ゴールド3', 'ゴールド3'), ('ゴールド2', 'ゴールド2'), ('ゴールド1', 'ゴールド1'),
    ('プラチナ4', 'プラチナ4'), ('プラチナ3', 'プラチナ3'), ('プラチナ2', 'プラチナ2'), ('プラチナ1', 'プラチナ1'),
    ('ダイヤ4', 'ダイヤ4'), ('ダイヤ3', 'ダイヤ3'), ('ダイヤ2', 'ダイヤ2'), ('ダイヤ1', 'ダイヤ1'), ('マスター', 'マスター'), ('プレデター', 'プレデター')
    )

    rnk_min = forms.fields.MultipleChoiceField(
        choices = rank,
        required=True,
        label='希望ランク',
        widget=forms.widgets.Select
    )

    rnk_max= forms.fields.MultipleChoiceField(
        choices = rank,
        required=True,
        label='希望ランク',
        widget=forms.widgets.Select
    )

    nums = (('1人', '1人'), ('2人', '2人'), ('大会参加者募集', '大会参加者募集'))

    num = forms.fields.MultipleChoiceField(
        choices = nums,
        required = True,
        label = '希望人数',
        widget=forms.widgets.Select
    )

    pers = (('ランク', 'ランク'), ('Duoカジュアル', 'Duoカジュアル'), ('Trioカジュアル', 'Trioカジュアル'), ('アリーナ', 'アリーナ'), ('アリーナランク', 'アリーナランク'),
      ('大会', '大会')
      )

    per = forms.fields.MultipleChoiceField(
        choices = pers,
        required=True,
        label = '目的',
        widget=forms.widgets.Select
    )

    hards = (('Switch', 'Switch'), ('PS4', 'PS4'), ('PS5', 'PS5'), ('PC', 'PC'), ('Xbox', 'Xbox'))

    hard = forms.fields.MultipleChoiceField(
        choices = hards,
        required=True,
        label = '使用機器',
        widget=forms.RadioSelect
    )

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput
    )
    class Meta:
        model = CustomUser
        fields = ('username', 'user_id', 'email')

        def clean_password2(self):
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Oops!! Passwords don't match.")
            return password2
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_passoword(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_id')

        def clean_password(self):
            return self.initial["password"]


class p_r_select(forms.Form):
    rnk = (
    ('ブロンズ4', 'ブロンズ4'), ('ブロンズ3', 'ブロンズ3'), ('ブロンズ2', 'ブロンズ2'), ('ブロンズ1', 'ブロンズ1'),
    ('シルバー4', 'シルバー4'), ('シルバー3', 'シルバー3'), ('シルバー2', 'シルバー2'), ('シルバー1', 'シルバー1'),
    ('ゴールド4', 'ゴールド4'), ('ゴールド3', 'ゴールド3'), ('ゴールド2', 'ゴールド2'), ('ゴールド1', 'ゴールド1'),
    ('プラチナ4', 'プラチナ4'), ('プラチナ3', 'プラチナ3'), ('プラチナ2', 'プラチナ2'), ('プラチナ1', 'プラチナ1'),
    ('ダイヤ4', 'ダイヤ4'), ('ダイヤ3', 'ダイヤ3'), ('ダイヤ2', 'ダイヤ2'), ('ダイヤ1', 'ダイヤ1'), ('マスター', 'マスター'), ('プレデター', 'プレデター')
    )

    rank = forms.ChoiceField(
        choices=rnk,
        required=True,
        label='rank',
        widget=forms.widgets.Select
    )

    p_field = (('Switch', 'Switch'), ('PS4', 'PS4'), ('PS5', 'PS5'), ('PC', 'PC'), ('Xbox', 'Xbox'))

    ply_f = forms.ChoiceField(
        choices=p_field,
        required=True,
        label='play field',
        widget=forms.SelectMultiple()
    )

from django import forms
from django.forms import fields, widgets
from .models import CustomUser, article_form
from datetime import datetime
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import forms as auth_forms

#投稿作成フォーム

class categorie_form(forms.Form):

    

    title = forms.CharField(max_length=30)
    comments = forms.CharField(widget=forms.Textarea(attrs={'cols':'80', 'rows':'10'}))

    #ランク選択
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

    #人数
    nums = (('1人', '1人'), ('2人', '2人'), ('大会参加者募集', '大会参加者募集'))

    num = forms.fields.MultipleChoiceField(
        choices = nums,
        required = True,
        label = '希望人数',
        widget=forms.widgets.Select
    )

    #ゲームモード
    pers = (('ランク', 'ランク'), ('Duoカジュアル', 'Duoカジュアル'), ('Trioカジュアル', 'Trioカジュアル'), ('アリーナ', 'アリーナ'), ('アリーナランク', 'アリーナランク'),
      ('大会', '大会')
      )

    per = forms.fields.MultipleChoiceField(
        choices = pers,
        required=True,
        label = '目的',
        widget=forms.widgets.Select
    )

    #プレイ環境
    hards = (('Switch', 'Switch'), ('PS4', 'PS4'), ('PS5', 'PS5'), ('PC', 'PC'), ('Xbox', 'Xbox'))

    hard = forms.fields.MultipleChoiceField(
        choices = hards,
        required=True,
        label = '使用機器',
        widget=forms.RadioSelect()
    )

    class Meta:
        model = article_form
        fields = ('title', 'comments', 'rnk_min', 'rnk_max', 'num', 'per', 'hard')

#ユーザー作成フォーム

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput
    )

    comments = forms.CharField(widget=forms.Textarea(attrs={'cols':'80', 'rows':'10'}))

    rnk = (
    ('設定なし', '設定なし'), ('ブロンズ4', 'ブロンズ4'), ('ブロンズ3', 'ブロンズ3'), ('ブロンズ2', 'ブロンズ2'), ('ブロンズ1', 'ブロンズ1'),
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

    p_field = (('設定なし', '設定なし'), ('Switch', 'Switch'), ('PS4', 'PS4'), ('PS5', 'PS5'), ('PC', 'PC'), ('Xbox', 'Xbox'))

    playfield = forms.MultipleChoiceField(
        choices=p_field,
        required=True,
        label='playfield',
        widget=forms.CheckboxSelectMultiple
    )

    characters = (('ブラッドハウンド', 'ブラッドハウンド'), ('ジブラルタル', 'ジブラルタル'), ('ライフライン', 'ライフライン'), ('パスファインダー', 'パスファインダー'), ('レイス', 'レイス'),
                ('バンガロール', 'バンガロール'), ('コースティック', 'コースティック'), ('ミラージュ', 'ミラージュ'), ('オクタン', 'オクタン'), ('ワットソン', 'ワットソン'), ('クリプト', 'クリプト'),
                ('レヴナント', 'レヴナント'), ('ローバ', 'ローバ'), ('ランパート', 'ランパート'), ('ホライゾン', 'ホライゾン'), ('ヒューズ', 'ヒューズ'), ('シア', 'シア'), ('アッシュ', 'アッシュ'))

    character = forms.fields.MultipleChoiceField(
        choices = characters,
        required=True,
        label = 'よく使うキャラクター',
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'user_id', 'email', 'playfield', 'rank', 'twitter_id', 'Youtube_url', 'discord_id', 'password1', 'password2', 'comments', 'character')

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

#ユーザー情報修正フォーム

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_id', 'playfield', 'rank', 'twitter_id', 'Youtube_url')

        def clean_password(self):
            return self.initial["password"]

class LoginForm(auth_forms.AuthenticationForm):
    #ログインフォーム
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
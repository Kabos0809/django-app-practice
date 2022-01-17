import encodings
from django import forms
from .models import CustomUser, article_form, reportModel
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import forms as auth_forms

characters = (('ブラッドハウンド', 'ブラッドハウンド'), ('ジブラルタル', 'ジブラルタル'), ('ライフライン', 'ライフライン'), ('パスファインダー', 'パスファインダー'), ('レイス', 'レイス'),
                ('バンガロール', 'バンガロール'), ('コースティック', 'コースティック'), ('ミラージュ', 'ミラージュ'), ('オクタン', 'オクタン'), ('ワットソン', 'ワットソン'), ('クリプト', 'クリプト'),
                ('レヴナント', 'レヴナント'), ('ローバ', 'ローバ'), ('ランパート', 'ランパート'), ('ホライゾン', 'ホライゾン'), ('ヒューズ', 'ヒューズ'), ('シア', 'シア'), ('アッシュ', 'アッシュ'))

ranks = (
    ('ブロンズ4', 'ブロンズ4'), ('ブロンズ3', 'ブロンズ3'), ('ブロンズ2', 'ブロンズ2'), ('ブロンズ1', 'ブロンズ1'),
    ('シルバー4', 'シルバー4'), ('シルバー3', 'シルバー3'), ('シルバー2', 'シルバー2'), ('シルバー1', 'シルバー1'),
    ('ゴールド4', 'ゴールド4'), ('ゴールド3', 'ゴールド3'), ('ゴールド2', 'ゴールド2'), ('ゴールド1', 'ゴールド1'),
    ('プラチナ4', 'プラチナ4'), ('プラチナ3', 'プラチナ3'), ('プラチナ2', 'プラチナ2'), ('プラチナ1', 'プラチナ1'),
    ('ダイヤ4', 'ダイヤ4'), ('ダイヤ3', 'ダイヤ3'), ('ダイヤ2', 'ダイヤ2'), ('ダイヤ1', 'ダイヤ1'), ('マスター', 'マスター'), ('プレデター', 'プレデター')
    )

nums = (('1人', '1人'), ('2人', '2人'), ('大会参加者募集', '大会参加者募集'))

pers = (('ランク', 'ランク'), ('Duoカジュアル', 'Duoカジュアル'), ('Trioカジュアル', 'Trioカジュアル'), ('アリーナ', 'アリーナ'), ('アリーナランク', 'アリーナランク'),
      ('大会', '大会'))

p_field = (('Switch', 'Switch'), ('PS4', 'PS4'), ('PS5', 'PS5'), ('PC', 'PC'), ('Xbox', 'Xbox'))



#投稿作成フォーム

class categorie_form(forms.ModelForm):

    title = forms.CharField(max_length=30)
    comments = forms.CharField(widget=forms.Textarea(attrs={'cols':'80', 'rows':'10'}))

    #ランク選択

    rnk_min = forms.fields.ChoiceField(
        choices = ranks,
        required=True,
        label='希望ランク',
        widget=forms.widgets.Select
    )

    rnk_max= forms.fields.ChoiceField(
        choices = ranks,
        required=True,
        label='希望ランク',
        widget=forms.widgets.Select
    )

    #人数

    num = forms.fields.ChoiceField(
        choices = nums,
        required = True,
        label = '希望人数',
        widget=forms.widgets.Select
    )

    #ゲームモード

    per = forms.fields.ChoiceField(
        choices = pers,
        required=True,
        label = '目的',
        widget=forms.widgets.Select
    )

    #プレイ環境

    hard = forms.fields.ChoiceField(
        choices = p_field,
        required=True,
        label = '使用機器',
        widget=forms.RadioSelect()
    )

    class Meta:
        model = article_form
        fields = ('title', 'comments', 'rnk_min', 'rnk_max', 'num', 'per', 'hard')

#投稿修正フォーム

class PostUpdateForm(forms.ModelForm):

    comments = forms.CharField(widget=forms.Textarea(attrs={'cols':'80', 'rows':'10'}))

    #ランク選択

    rnk_min = forms.fields.ChoiceField(
        choices = ranks,
        required=True,
        label='希望ランク',
        widget=forms.widgets.Select
    )

    rnk_max= forms.fields.ChoiceField(
        choices = ranks,
        required=True,
        label='希望ランク',
        widget=forms.widgets.Select
    )

    #人数

    num = forms.fields.ChoiceField(
        choices = nums,
        required = True,
        label = '希望人数',
        widget=forms.widgets.Select
    )

    #ゲームモード

    per = forms.fields.ChoiceField(
        choices = pers,
        required=True,
        label = '目的',
        widget=forms.widgets.Select
    )

    #プレイ環境

    hard = forms.fields.ChoiceField(
        choices = p_field,
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

    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols':'80', 'rows':'10'}))

    rank = forms.ChoiceField(
        choices=ranks,
        required=True,
        label='rank',
        widget=forms.widgets.Select
    )

    playfield = forms.MultipleChoiceField(
        choices=p_field,
        required=False,
        label='playfield',
        widget=forms.CheckboxSelectMultiple
    )

    character = forms.fields.MultipleChoiceField(
        choices = characters,
        required=False,
        label = 'よく使うキャラクター',
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'player_name', 'email', 'playfield', 'rank', 'twitter_id', 'Youtube_url', 'discord_id', 'password1', 'password2', 'comments', 'character')

        def clean_password(self):
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("パスワードが間違っています")
            return password1
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_passoword(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user

#ユーザー情報修正フォーム

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols':'80', 'rows':'10'}))

    rank = forms.ChoiceField(
        choices=ranks,
        required=True,
        label='rank',
        widget=forms.widgets.Select
    )

    playfield = forms.MultipleChoiceField(
        choices=p_field,
        required=True,
        label='playfield',
        widget=forms.CheckboxSelectMultiple
    )

    character = forms.fields.MultipleChoiceField(
        choices = characters,
        required=True,
        label = 'よく使うキャラクター',
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'player_name', 'playfield', 'rank', 'twitter_id', 'Youtube_url', 'comments', 'character', 'discord_id')

        def clean_password(self):
            return self.initial["password"]

#ログインフォーム

class LoginForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

#違反報告フォーム

class ReportForm(forms.ModelForm):

    article_id = forms.CharField(required=True)

    categories = (('スパム', 'スパム'), ('出会いなどを誘うような内容', '出会いなどを誘うような内容'), ('公序良俗に反する内容', '公序良俗に反する内容'), ('暴言・脅迫・誹謗中傷', '暴言・脅迫・誹謗中傷'), ('その他', 'その他'))

    category = forms.ChoiceField(
        choices=categories,
        label='違反事項',
        required=True,
        widget=forms.widgets.Select
    )

    matters = forms.CharField(required=True, widget=forms.Textarea(attrs={'cols':'80', 'rows':'10'}))

    class Meta:
        model = reportModel
        fields = ('article_id', 'category', 'matters', 'not_mischief')
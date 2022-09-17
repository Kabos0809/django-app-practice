from django import forms
from .models import CustomUser, ThreadComments, article_comment, apex_recruit, reportModel, ThreadModel
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.password_validation import validate_password

characters = (('設定なし', '設定なし'), ('ブラッドハウンド', 'ブラッドハウンド'), ('ジブラルタル', 'ジブラルタル'), ('ライフライン', 'ライフライン'), ('パスファインダー', 'パスファインダー'), ('レイス', 'レイス'),
                ('バンガロール', 'バンガロール'), ('コースティック', 'コースティック'), ('ミラージュ', 'ミラージュ'), ('オクタン', 'オクタン'), ('ワットソン', 'ワットソン'), ('クリプト', 'クリプト'),
                ('レヴナント', 'レヴナント'), ('ローバ', 'ローバ'), ('ランパート', 'ランパート'), ('ホライゾン', 'ホライゾン'), ('ヒューズ', 'ヒューズ'), ('シア', 'シア'), ('アッシュ', 'アッシュ'), ('マッドマギー', 'マッドマギー'))

ranks = (
    ('ブロンズ4', 'ブロンズ4'), ('ブロンズ3', 'ブロンズ3'), ('ブロンズ2', 'ブロンズ2'), ('ブロンズ1', 'ブロンズ1'),
    ('シルバー4', 'シルバー4'), ('シルバー3', 'シルバー3'), ('シルバー2', 'シルバー2'), ('シルバー1', 'シルバー1'),
    ('ゴールド4', 'ゴールド4'), ('ゴールド3', 'ゴールド3'), ('ゴールド2', 'ゴールド2'), ('ゴールド1', 'ゴールド1'),
    ('プラチナ4', 'プラチナ4'), ('プラチナ3', 'プラチナ3'), ('プラチナ2', 'プラチナ2'), ('プラチナ1', 'プラチナ1'),
    ('ダイヤ4', 'ダイヤ4'), ('ダイヤ3', 'ダイヤ3'), ('ダイヤ2', 'ダイヤ2'), ('ダイヤ1', 'ダイヤ1'), ('マスター', 'マスター'), ('プレデター', 'プレデター')
    )

nums = (('1人', '1人'), ('2人', '2人'), ('大会参加者募集', '大会参加者募集'))

pers = (('ランク', 'ランク'), ('Duoカジュアル', 'Duoカジュアル'), ('Trioカジュアル', 'Trioカジュアル'), ('アリーナ', 'アリーナ'), ('アリーナランク', 'アリーナランク'),
        ('タイマン', 'タイマン'), ('大会', '大会'))

p_field = (('設定なし', '設定なし'), ('Switch', 'Switch'), ('PS4', 'PS4'), ('PS5', 'PS5'), ('PC', 'PC'), ('Xbox', 'Xbox'))

vcs = (('なし', 'なし'), ('discord', 'discord'), ('ゲーム内VC', 'ゲーム内VC'), ('その他VC', 'その他VC'))

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

    #ボイチャ

    vc = forms.ChoiceField(
        choices=vcs,
        label='ボイチャ',
        required=False,
        widget=forms.RadioSelect
    )

    class Meta:
        model = apex_recruit
        fields = ('title', 'comments', 'rnk_min', 'rnk_max', 'num', 'per', 'hard', 'vc')

#募集へのコメント

class CommentForm(forms.ModelForm):
    class Meta:
        model = article_comment
        fields = ('comment',)


#ユーザー作成フォーム

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)

    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput)

    username = forms.CharField(label="username")

    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols':'80', 'rows':'10'}))

    icon = forms.ImageField(required=False)

    steam_url = forms.CharField(required=False)

    origin_id = forms.CharField(required=False)

    psn_id = forms.CharField(required=False)

    switch_id = forms.CharField(required=False)

    other_id = forms.CharField(required=False)

    discord_id = forms.CharField(required=False)

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
        fields = ('icon', 'username', 'player_name', 'steam_url', 'origin_id', 'psn_id', 'switch_id', 'other_id', 'is_show_steam', 'is_show_origin', 'is_show_psn', 'is_show_switch', 'is_show_other', 'is_show_discord', 'email', 'playfield', 'rank', 'discord_id', 'password1', 'comments', 'character')

        def save(self, commit=True):
            user = super().save(commit=False)
            icon = self.cleaned_data['icon']
            validate_password(self.cleaned_data['password1'], user)
            user.set_passoword(self.cleaned_data["password1"])
            user.icon = icon
            if commit:
                user.save()
            return user

    def clean_username(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if len(username) < 8:
            raise forms.ValidationError('ユーザーネームが短すぎます')

    def clean_rank(self):
        cleaned_data = super().clean()
        rank = cleaned_data.get('rank')
        if not rank:
            raise forms.ValidationError('ランクを選択してください')
    
    def clean_playfield(self):
        cleaned_data = super().clean()
        playfield = cleaned_data.get('playfield')
        if not playfield:
            raise forms.ValidationError('プレイ環境を設定してください')
    
    def clean_character(self):
        cleaned_data = super().clean()
        character = cleaned_data.get('character')
        if not character:
            raise forms.ValidationError('レジェンドを選択してください')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('パスワードが一致しません') 

#ユーザー情報修正フォーム

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    username = forms.CharField(required=False)

    player_name = forms.CharField(required=False)

    icon = forms.ImageField(required=False)

    steam_url = forms.CharField(required=False)

    origin_id = forms.CharField(required=False)

    psn_id = forms.CharField(required=False)

    switch_id = forms.CharField(required=False)

    other_id = forms.CharField(required=False)

    discord_id = forms.CharField(required=False)

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
        fields = ('icon', 'username', 'player_name', 'email', 'steam_url', 'origin_id', 'psn_id', 'switch_id', 'other_id', 'playfield', 'rank', 'comments', 'character', 'discord_id')

        def clean_password(self):
            return self.initial["password"]
    
    def clean_username(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if len(username) < 8:
            raise forms.ValidationError('ユーザーネームが短すぎます')

#プライバシー設定    

#class PrivacySettingForm(forms.ModelForm):
    

#ログインフォーム

class LoginForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

#違反報告フォーム

class ReportForm(forms.ModelForm):

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
        fields = ('category', 'matters', 'not_mischief')

#情報交換

class NewsForm(forms.ModelForm):

    about = forms.CharField(required=True, widget=forms.Textarea(attrs={'cols':'80', 'rows':'10'}))

    class Meta:
        model = ThreadModel
        fields = ('title',)

#情報交換コメント

class NewsCommentForm(forms.ModelForm):

    comment = forms.CharField(required=True, widget=forms.Textarea(attrs={'cols':'80', 'rows':'10'}))

    class Meta:
        model = ThreadComments
        fields = ('comment',)
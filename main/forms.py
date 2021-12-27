from django import forms
from .models import article_form
from datetime import datetime

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
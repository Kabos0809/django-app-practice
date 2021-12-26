from django import forms
from .models import article_form
from datetime import datetime

class categorie_form(forms.Form):

    title = forms.CharField(max_length=30)
    comments = forms.CharField(max_length=500)

    rank = (
    ('b4', 'ブロンズ4'), ('b3', 'ブロンズ3'), ('b2', 'ブロンズ2'), ('b1', 'ブロンズ1'),
    ('s4', 'シルバー4'), ('s3', 'シルバー3'), ('s2', 'シルバー2'), ('s1', 'シルバー1'),
    ('g4', 'ゴールド4'), ('g3', 'ゴールド3'), ('g2', 'ゴールド2'), ('g1', 'ゴールド1'),
    ('p4', 'プラチナ4'), ('p3', 'プラチナ3'), ('p2', 'プラチナ2'), ('p1', 'プラチナ1'),
    ('d4', 'ダイヤ4'), ('d3', 'ダイヤ3'), ('d2', 'ダイヤ2'), ('d1', 'ダイヤ1'), ('mas', 'マスター'), ('pre', 'プレデター')
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

    nums = (('0', '1人'), ('1', '2人'), ('2', '大会参加者募集'))

    num = forms.fields.MultipleChoiceField(
        choices = nums,
        required = True,
        label = '希望人数',
        widget=forms.widgets.Select
    )

    pers = (('rnk', 'ランク'), ('casd', 'Duoカジュアル'), ('cast', 'Trioカジュアル'), ('aln', 'アリーナ'), ('aln_rnk', 'アリーナランク'),
      ('comp', '大会')
      )

    per = forms.fields.MultipleChoiceField(
        choices = pers,
        required=True,
        label = '目的',
        widget=forms.widgets.Select
    )

from django import forms
from .models import article_form
from django.db import models

class articleform(forms.ModelForm):
    class Meta():
        model = article_form
        fields = ('title', 'comments')


class rank(models.TextChoices):
    bronze4 = 'b4', 'ブロンズ4'
    bronze3 = 'b3', 'ブロンズ3'
    bronze2 = 'b2', 'ブロンズ2'
    bronze1 = 'b1', 'ブロンズ1'
    silver4 = 's4', 'シルバー4'
    silver3 = 's3', 'シルバー3'
    silver2 = 's2', 'シルバー2'
    silver1 = 's1', 'シルバー1'
    gold4 = 'g4', 'ゴールド4'
    gold3 = 'g3', 'ゴールド3'
    gold2 = 'g2', 'ゴールド2'
    gold1 = 'g1', 'ゴールド1'
    platinum4 = 'p4', 'プラチナ4'
    platinum3 = 'p3', 'プラチナ3'
    platinum2 = 'p2', 'プラチナ2'
    platinum1 = 'p1', 'プラチナ1'
    diamond4 = 'd4', 'ダイヤ4'
    diamond3 = 'd3', 'ダイヤ3'
    diamond2 = 'd2', 'ダイヤ2'
    diamond1 = 'd1', 'ダイヤ1'
    master = 'mas', 'マスター'
    predator = 'pre', 'プレデター'
 
class rankform(forms.Form):
    ranks = forms.fields.MultipleChoiceField(
        choices = rank.choices,
        required=True,
        label='希望ランク',
        widget=forms.CheckboxSelectMultiple()
    )

    def __str__(self):
        return self.ranks

class number(models.TextChoices):
    one = '0', '1人'
    two = '1', '2人'
    competition = '2', '大会参加者募集'

class numberform(forms.Form):
    number = forms.fields.MultipleChoiceField(
        choices = number,
        required = True,
        label = '希望人数',
        widget=forms.widgets.Select
    )

    def __str__(self):
        return self.number

class perposes(models.TextChoices):
    rnk = 'rnk', 'ランク'
    casd = 'casd', 'Duoカジュアル'
    cast = 'cast', 'Trioカジュアル'
    aln = 'aln', 'アリーナ'
    aln_rnk = 'aln_rnk', 'アリーナランク'
    competition = 'comp', '大会'

class perposeform(forms.Form):
    perpose = forms.fields.MultipleChoiceField(
        choices = perposes,
        required=True,
        label = '目的',
        widget=forms.CheckboxSelectMultiple()
    )

    def __str__(self):
        return self.perpose
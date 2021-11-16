from django.forms import Form
from django.forms import ChoiceField, RadioSelect

class VotingForm(Form):
    CHOICES = []
    choice = ChoiceField(widget=RadioSelect, choices=CHOICES)

    def __init__(self,question,*args,**kwargs):
        super().__init__(*args,**kwargs)
        added_choice = []
        self.question = question
        for i, option in enumerate(question.choice_set.all()):
            added_choice.append((str(i), option.choice_text))
        field = ChoiceField(widget=RadioSelect, choices=added_choice)
        self.fields['choice'] = field
        self.CHOICES = added_choice
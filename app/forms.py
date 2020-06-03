from django import forms
from .models import Person
from django.core.exceptions import ValidationError

def validate_credit(value):
    print(value)
    if value < 0:
        raise ValidationError("Enter some positive amount")

class getid:
    def __init__(self,id):
        self.id=id
    

def gett(*argv):
    try:
        det=Person.objects.all().values()
        k=0
        for i in argv:
            k=i
        options = []
        for (index,item) in enumerate(det):
            if(item['id']==int(k)):
                pass
            else:
                options.append((item['id'],item['name']))
    except Exception as e:
        print(e)

    print(options)
    return options

class formname(forms.Form):

    cred=forms.IntegerField(validators=[validate_credit])
    Transfer_to=forms.ChoiceField(choices=())

    def getform(self,id):
        print(id)
        self.fields["Transfer_to"]=forms.ChoiceField(choices=(gett(id)))
        
    # cred=forms.IntegerField(validators=[validate_credit])
    # Transfer_to=forms.ChoiceField(choices=(gett(0)
    # ))

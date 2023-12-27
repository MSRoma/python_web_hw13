from django.forms import ModelForm, CharField, TextInput, DateField,ModelMultipleChoiceField,ModelChoiceField,SelectMultiple,Select
from .models import Tag, Note, Author


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']

class AuthorForm(ModelForm):

    fullname = CharField(min_length=10, max_length=250, required=True, widget=TextInput())
    born_date = CharField(min_length=10, max_length=250, required=True, widget=TextInput())
    born_location = CharField(min_length=10, max_length=250, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=500, required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname','born_location','born_location','description']



class NoteForm(ModelForm):

    #name = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=500, required=True, widget=TextInput())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('name'),
                                    widget=SelectMultiple(attrs={"class": "form-select", "size": "7"}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by('fullname'),
                              widget=Select(attrs={"class": "form-select"}))

    class Meta:
        model = Note
        fields = ['description']
        


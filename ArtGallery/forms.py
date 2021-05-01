from django import forms
from ArtGallery.models import Art

class ArtForm(forms.ModelForm):
  class Meta:
    saleType = (
      ('True', True),
      ('False', False)
    )

    tagTypes = ((
      ('Object','Object'),
      ('Place','Place'),
      ('Scenery','Scenery'),
      ('Portrait','Portrait')
    ))

    model = Art
    fields = ("id","title","arttype","saleStatus","quantity","date",'tags','price','desc', 'artImg')

    widgets = {
      'id':forms.HiddenInput(),
      'title': forms.TextInput(),
      'saleStatus': forms.RadioSelect(choices=saleType),
      'quantity': forms.NumberInput(),
      'date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'type':'date','required':True}),
      'tags': forms.CheckboxSelectMultiple(choices=tagTypes),
      'price': forms.NumberInput(),
      'desc': forms.Textarea(attrs={'rows': 5}),
      'artImg': forms.FileInput(),

    }
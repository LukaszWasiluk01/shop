from django import forms

class CartAddProductForm(forms.Form):
    def __init__(self, quantity_left, *args, **kwargs):
        self.quantity_choices = tuple([(i, str(i)) for i in range(1, quantity_left + 1)])
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        self.fields['quantity'] = forms.TypedChoiceField(coerce=int, choices=self.quantity_choices)
    
    
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)

class SearchForm(forms.Form):

    name = forms.CharField(max_length=128, required=False, widget=forms.HiddenInput(attrs={"id":"name_field","class":"form_field"}))
    price_from = forms.DecimalField(decimal_places=2, required=False,widget=forms.NumberInput(attrs={"class":"form_field"}))
    price_to = forms.DecimalField(decimal_places=2, required=False,widget=forms.NumberInput(attrs={"class":"form_field"}))
    
    def clean(self):
        cd = self.cleaned_data
        price_from = cd.get("price_from")
        price_to = cd.get("price_to")
        if price_from and price_to:
            if price_from > price_to:
                raise forms.ValidationError("Minimal price can't be higher than maximum.")
        
        return cd

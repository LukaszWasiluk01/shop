from django import forms

class CartAddProductForm(forms.Form):
    def __init__(self, quantity_left, *args, **kwargs):
        self.quantity_choices = tuple([(i, str(i)) for i in range(1, quantity_left + 1)])
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        self.fields['quantity'] = forms.TypedChoiceField(coerce=int, choices=self.quantity_choices)
    
    
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)

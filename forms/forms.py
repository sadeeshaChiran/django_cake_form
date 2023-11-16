from django import forms
from .models import Form

class MyForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        # name
        self.fields['name'].widget=forms.TextInput(attrs={'class': 'form-control'})
        

        # Contect number
        self.fields['contact_number'].widget = forms.TimeInput(attrs={'type': 'tel', 'class': 'form-control'})
        
        
        # email
        self.fields['email'].widget=forms.TextInput(attrs={'class': 'form-control'})


        # delivery address
        self.fields['delivery_address'].widget=forms.TextInput(attrs={'class': 'form-control'})


        # occasion
        self.fields['occasion'].widget.attrs.update({'class': 'form-select'})
        self.fields['other_occasion'].widget=forms.TextInput(attrs={'class': 'form-control'})
        self.fields['other_occasion'].required = False


        # cake size
        self.fields['cake_size'].widget.attrs.update({'class': 'form-select'})
        self.fields['other_cake_size'].widget=forms.TextInput(attrs={'class': 'form-control'})
        self.fields['other_cake_size'].required = False
        

        # cake shape
        self.fields['cake_shape'].widget.attrs.update({'class': 'form-select'})
        self.fields['cake_other_shape'].widget=forms.TextInput(attrs={'class': 'form-control'})
        self.fields['cake_other_shape'].required = False
        

        # cake flavor
        self.fields['cake_flavors'].widget.attrs.update({'class': 'form-select'})
        self.fields['cake_other_flavors'].widget=forms.TextInput(attrs={'class': 'form-control'})
        self.fields['cake_other_flavors'].required = False
        
        
        # cake dilling
        self.fields['cake_filling'].widget.attrs.update({'class': 'form-select'})
        self.fields['cake_other_filling'].widget=forms.TextInput(attrs={'class': 'form-control'})
        self.fields['cake_other_filling'].required = False
        self.fields['fruit_types'].widget=forms.TextInput(attrs={'class': 'form-control'})
        self.fields['fruit_types'].required = False

        # cake frosting
        self.fields['cake_frosting'].widget.attrs.update({'class': 'form-select'})


        # cake decorations
        self.fields['cake_decorations'].widget.attrs.update({'class': 'form-select'})
        self.fields['cake_other_decorations'].widget=forms.TextInput(attrs={'class': 'form-control'})
        self.fields['cake_other_decorations'].required = False
        

        # text
        self.fields['text'].widget=forms.TextInput(attrs={'class': 'form-control'})
       
       
        # font style
        self.fields['font_style'].widget=forms.TextInput(attrs={'class': 'form-control'})
        
        
        # colour
        self.fields['colour'].widget=forms.TextInput(attrs={'type': 'color','class': 'form-control'})
        
        
        # delivary type
        self.fields['delivaery_or_pickme'].widget.attrs.update({'class': 'form-select'})
        
        
        # preferred date
        self.fields['preferred_date'].widget = forms.DateInput(attrs={'class': 'form-control ', 'type': 'date'})
       
       
        # preferred time
        self.fields['preferred_time'].widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'time'})
        
        
        # additional requests
        self.fields['additional_requests'].widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
        
        
        # payment method
        self.fields['paymentmethod'].widget.attrs.update({'class': 'form-select'})
        self.fields['other_paymentmethod'].widget.attrs.update({'class': 'form-select'})
        self.fields['other_paymentmethod'].required = False
        
        
        # image
        self.fields['image'].widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'})
    
        

        
        instance = kwargs.get('instance')
        
        if instance and instance.occasion != 'other':
            del self.fields['other_occasion']
            
            
        if instance and instance.cake_size != 'Custom size':
            del self.fields['cake_other_size']
        
        
        if instance and instance.cake_shape != 'Custom shape':
            del self.fields['cake_other_shape']
            
            
        if instance and instance.cake_flavors != 'Custom flavor':
            del self.fields['cake_other_flavors']
            
            
            
        if instance and instance.cake_filling != 'other':
            del self.fields['cake_other_filling']
            
        if instance and instance.cake_filling != 'Fruit':
            del self.fields['fruit_types']
        
        if instance and instance.cake_decorations != 'Custom decoration':
            del self.fields['cake_other_decorations']
            
            
        if instance and instance.paymentmethod != 'other':
            del self.fields['other_paymentmethod']

            
    
        
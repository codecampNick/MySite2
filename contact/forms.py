from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True,
                                  widget=forms.TextInput(attrs={'placeholder': 'your.email@address.com',
                                                                'size': '22'}))
    subject = forms.CharField(required=True,
                              widget=forms.TextInput(attrs={'placeholder': 'I\'d like to chat because.... :)',
                                                            'size': '24'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '<sarcasm>Pretty obivious isn\'t it?\n' +
                                                            'I mean, wow.</sarcasm>','rows': '4', 'cols': 24 ,
                                                           'size': '24'}), required=True)


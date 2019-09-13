from django import forms


class ContactForm(forms.Form):
    from_name = forms.CharField(max_length=100, label='Your Name', required=True, help_text='100 Characters Max',
                                widget=forms.TextInput(attrs={'placeholder': 'FirstName LastName',
                                                              'size': '26'}))
    from_email = forms.EmailField(max_length=255, label='Email', required=True, help_text='255 Characters Max',
                                  widget=forms.TextInput(attrs={'placeholder': 'your.email@address.com',
                                                                'size': '26'}))
    subject = forms.CharField(required=True, max_length=255, help_text='255 Characters Max',
                              widget=forms.TextInput(attrs={'placeholder': 'I\'d like to chat because.... :)',
                                                            'size': '26'}))
    message = forms.CharField(max_length=5000, required=True, help_text='5000 Max Characters',
                              widget=forms.Textarea(attrs={'placeholder': '<sarcasm>Pretty obvious isn\'t it?\n' +
                                                                          'I mean, wow.</sarcasm>',
                                                                          'rows': '4', 'cols': 26}))


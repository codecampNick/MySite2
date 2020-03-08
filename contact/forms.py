from django import forms


class ContactForm(forms.Form):
    from_name = forms.CharField(max_length=100, label='Your Name', required=True, help_text=' Characters Remaining',
                                widget=forms.TextInput(attrs={'placeholder': 'FirstName LastName',
                                                              'size': '30'}))
    from_email = forms.EmailField(max_length=255, label='Email', required=True, help_text=' Characters Remaining',
                                  widget=forms.TextInput(attrs={'placeholder': 'your.email@address.com',
                                                                'size': '30'}))
    # This is a honey pot element. Simple anti spam. Validated in views
    optional_contact = forms.CharField(max_length=100, label='Optional Contact', required=False, help_text=' Characters Remaining',
                                       widget=forms.TextInput(attrs={'placeholder': 'xxx-xxx-xxxx',
                                                              'size': '30'}))
    subject = forms.CharField(required=True, max_length=255, help_text=' Characters Remaining',
                              widget=forms.TextInput(attrs={'placeholder': 'I\'d like to chat because.... :)',
                                                            'size': '30'}))
    message = forms.CharField(max_length=5000, required=True, help_text=' Characters Remaining',
                              widget=forms.Textarea(attrs={'placeholder': '<sarcasm>Pretty obvious isn\'t it?\n' +
                                                                          'I mean, wow.</sarcasm>',
                                                                          'rows': '4', 'cols': 29}))


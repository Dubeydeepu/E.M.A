from django import forms

class FeedbackForm(forms.Form):
    email=forms.EmailField(label="Enter Your Email",max_length=100)
    name=forms.CharField(label="Enter Your Name",max_length=100)
    feedback=forms.CharField(label="Write Your Feedback",widget=forms.Textarea)

    
    # Your declared form fields here


    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
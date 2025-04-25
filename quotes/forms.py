from django import forms
from .models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['content', 'author', 'tag']  # ✅ Include tag
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter quote here...'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author name'}),
            'tag': forms.Select(attrs={'class': 'form-select'}),  # Optional styling
        }

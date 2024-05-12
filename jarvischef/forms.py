from django import forms  

class RecipeForm(forms.Form) : 
    recipe_message=forms.CharField(max_length=255 ,
            widget=forms.TextInput(
                attrs={'placeholder':'Plz Ask Your Nutrition plans For Todays'}
    )   )
from django import forms

from Todo.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Task
        fields = "__all__"


class TaskCreateForm(TaskForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "datetime": forms.DateTimeInput(
                format="%Y-%m-%d", attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                }
            ),
            "deadline": forms.DateTimeInput(
                format="%Y-%m-%d", attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                }
            )}

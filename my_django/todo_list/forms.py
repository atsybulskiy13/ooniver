from django.forms import (
    Form, CharField, BooleanField, DateTimeField
)


class TodoForm(Form):
    title = CharField(
        max_length=121,
        min_length=3,
        required=True,
    )
    finish_date = DateTimeField(
        required=True
    )
    is_active = BooleanField(
        initial=True,
        required=False
    )
    is_finished = BooleanField(
        initial=False,
        required=False
    )

from django import forms


class DateInput(forms.DateInput):
    '''Defines the date input i want.'''
    input_type = 'date'

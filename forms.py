from django import forms
from django.forms import Textarea
from django.forms.fields import DateField, SelectMultiple
from django.utils.translation import ugettext_lazy as _
from .models import Neighborhood, Household, HouseholdBid, Payment, SupplierBid, Supplier
from decimal import *
from django.db import models

from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class HouseholdNonSurveyForm(forms.ModelForm):

	class Meta:
		model = Household
		fields = ('household_firstname', 'household_lastname', 'household_nickname', 
			'household_phone1', 'household_phone2', 'household_phone3',
			'household_is_claiming_survey', 'household_notes', 'primary_landmark_id', 'closest_main_street')

		widgets = {
			'household_notes': Textarea(attrs={'rows': 3}),
		}

class HouseholdEditForm(forms.ModelForm):

	class Meta:
		model = Household
		fields = ('household_firstname', 'household_lastname', 'household_nickname', 
			'household_head_firstname', 'household_head_lastname','household_phone1', 
			'household_phone2', 'household_phone3', 'household_notes')

		widgets = {
			'household_notes': Textarea(attrs={'rows': 3}),
		}

class HouseholdBidForm(forms.ModelForm):

	class Meta:
		model = HouseholdBid
		fields = ('bid_amount', 'bid_exception_1', 'bid_exception_2', 'bid_other_notes')

		labels = {
			'bid_amount': _('Bid amount'),
			'bid_exception_1': _('Large tank'),
			'bid_exception_2': _('Long hose'),
			'bid_other_notes': _('Other information'),
		}
		widgets = {
            'bid_other_notes': Textarea(attrs={'rows': 3}),
        }

	def clean_bid_amount(self):

		data = self.cleaned_data['bid_amount']

		if Decimal(0.0) >= data:
			raise forms.ValidationError("Bid amount must be positive")

		return data



class HouseholdBidChangeSupplierForm(forms.ModelForm):

	class Meta:
		model = HouseholdBid
		fields = ('assigned_supplier_offer',)

class HouseholdBidCancelBidForm(forms.ModelForm):

	class Meta:
		model = HouseholdBid
		fields = ('bid_canceled','is_hh_refuse_price')

class HouseholdBidMarkCompleteForm(forms.ModelForm):

	class Meta:
		model = HouseholdBid
		fields = ('household_rating_supplier', 'household_comments',)
		widgets = {
            'household_comments': Textarea(attrs={'rows': 3}),
        }

class PaymentForm(forms.ModelForm):

	class Meta:
		model = Payment
		fields = ('payment_completed',)

class SupplierBidForm(forms.ModelForm):

	class Meta:
		model = SupplierBid
		fields = ('offer_start_date', 'offer_end_date', 'neighborhoods_serviced', 'full_price', 'payment_advance', 'number_payment_advance', 'tank_size',)
		
		widgets = {
			'offer_start_date': forms.DateInput(attrs={'class':'datepicker'}),
			'offer_end_date': forms.DateInput(attrs={'class':'datepicker'}),
			'neighborhoods_serviced': SelectMultiple(attrs={'size':'80'}),
		} 
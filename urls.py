from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
		url(r'^/?$', views.index),
		url(r'^neighborhoods/?$', views.neighborhood_list),
		url(r'^neighborhoods/(?P<blockid>[0-9]+)/$', views.neighborhood_detail),
		url(r'^households/?$', views.household_list),
		url(r'^households/(?P<houseid>[0-9]+)/$', views.household_detail),
		url(r'^households/new/?$', views.household_newnonsurvey, name='household_new'),
		url(r'^households/(?P<houseid>[0-9]+)/edit/?$', views.household_edit, name='household_edit'),

		url(r'^householdbids/?$', views.householdbid_list),
		url(r'^householdbids/(?P<pk>[0-9]+)/?$', views.householdbid_detail),
		url(r'^householdbids/new/(?P<houseid>[0-9]+)/?$', views.householdbid_new, name='new_householdbid'),
		url(r'^householdbids/new/(?P<houseid>[0-9]+)/(?P<is_reject>[a-zA-Z]+)/?$', views.householdbid_new, name='householdbid_new_rejected'),
		url(r'^householdbids/new/(?P<houseid>[0-9]+)/(?P<negotiation_price>\w+|)/?$', views.householdbid_new, name='householdbid_new'),
		url(r'^householdbids/new/(?P<houseid>[0-9]+)/(?P<supplier_bid_id>[0-9]+)/(?P<is_reject>[a-zA-Z]+)/?$', views.householdbid_new, name='householdbid_new_reject_suppler'),
		url(r'^householdbids/new/accept/(?P<houseid>[0-9]+)/(?P<supplier_bid_id>[0-9]+)/?$', views.householdbid_new, name='householdbid_new_acepted_suppler'),
		url(r'^householdbids/accepted/(?P<houseid>[0-9]+)/(?P<supplier_bid_id>[0-9]+)/(?P<negotiation_price>\w+|)/?$', views.householdbid_new_upadte_price, name='householdbid_new_upadte_price'),
		url(r'^householdbids/(?P<pk>[0-9]+)/changesupplier/?$', views.householdbid_changesupplier),
		url(r'^householdbids/(?P<pk>[0-9]+)/cancelbid/?$', views.householdbid_cancelbid),
		url(r'^householdbids/(?P<pk>[0-9]+)/refuse/price/?$', views.household_refuse_price),
		url(r'^householdbids/(?P<pk>[0-9]+)/markcompleted/?$', views.householdbid_markcompleted),
		url(r'^householdfixpricebids/?$', views.household_fix_pricebid_list),
		url(r'^household/competativebids/?$', views.household_competitonbid_list),
		url(r'^householdbids/rejectbid/(?P<houseid>[0-9]+)/(?P<negotiation_price>\w+|)/(?P<hh_rejects_price>[a-zA-Z]+)/?$', views.household_rejects_bid_price, name='household_rejects_bid_price'),
		
		url(r'^suppliers/?$', views.supplier_list),
		url(r'^suppliers/(?P<supplyid>[0-9]+)/?$', views.supplier_detail),

		url(r'^supplierbids/?$', views.supplierbid_list),
		url(r'^supplierbids/(?P<pk>[0-9]+)/?$', views.supplierbid_detail),
		url(r'^supplierbids/new/(?P<supplyid>[0-9]+)/?$', views.supplierbid_new, name='supplierbid_new'),

		url(r'^payments/?$', views.payment_list),
		url(r'^payments/(?P<pk>[0-9]+)/?$', views.payment_detail),

		url(r'^household_search/?$', views.household_search),
		url(r'^household/bid/cancel/(?P<current_bid>\w+|)/(?P<lower_supplier_bid_id>\w+|)/?$', views.hh_bid_rejected_no_supplier_found,name='hh_bid_rejected_no_supplier_found'),
		url(r'^supplier/accept/newbids/(?P<houseid>[0-9]+)/(?P<supplier_bid_id>[0-9]+)/?$', views.supplier_accept_job_on_listed_price, name='bids_accepted_on_list_price'),
	)
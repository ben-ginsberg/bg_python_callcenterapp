from django.contrib import admin
from .models import Landmark, Cluster, Household, Neighborhood, HouseholdBid, Supplier, SupplierBid, Payment
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class NeighborhoodResource(resources.ModelResource):

	class Meta:
		model = Neighborhood
		import_id_fields = ['block_id_neighborhoods']

class NeighborhoodAdmin(ImportExportModelAdmin):
	resource_class = NeighborhoodResource
	pass

class LandmarkResource(resources.ModelResource):

	class Meta:
		model = Landmark
		import_id_fields = ['landmark_id']

class LandmarkAdmin(ImportExportModelAdmin):
	resource_class = LandmarkResource
	pass

class ClusterResource(resources.ModelResource):

	class Meta:
		model = Cluster
		import_id_fields = ['cluster_id']

class ClusterAdmin(ImportExportModelAdmin):
	resource_class = ClusterResource
	pass

class HouseholdResource(resources.ModelResource):

	class Meta:
		model = Household
		import_id_fields = ['cleaned_household_id']
		exclude = ('household_head_firstname', 'household_head_lastname','is_hh_select_tank','hh_selected_tank_size','price_is_accepted','hh_bid_accepted_time')

class HouseholdAdmin(ImportExportModelAdmin):
	resource_class = HouseholdResource
	pass

class SupplierResource(resources.ModelResource):

	class Meta:
		model = Supplier
		import_id_fields = ['supplier_id']

class SupplierAdmin(ImportExportModelAdmin):
	resource_class = SupplierResource
	pass

class SupplierBidResource(resources.ModelResource):

	class Meta:
		model = SupplierBid
		exclude = ('payment_advance', 'number_payment_advance', 'original_number_payment_advance', 'auctions_won',
			'neighborhoods_serviced','rejected_hh_bids','altenative_supplier_bids','random_supplier_bid')

class SupplierBidAdmin(ImportExportModelAdmin):
	resource_class = SupplierBidResource
	pass
class HouseholdBidResource(resources.ModelResource):

	class Meta:
		model = HouseholdBid
		exclude = ('is_hh_refuse_price',)

class HouseholdBidAdmin(ImportExportModelAdmin):
	resource_class = HouseholdBidResource
	pass

admin.site.register(Landmark, LandmarkAdmin)
admin.site.register(Cluster, ClusterAdmin)
admin.site.register(Household, HouseholdAdmin)
admin.site.register(Neighborhood,NeighborhoodAdmin)
admin.site.register(HouseholdBid,HouseholdBidAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(SupplierBid, SupplierBidAdmin)
admin.site.register(Payment)
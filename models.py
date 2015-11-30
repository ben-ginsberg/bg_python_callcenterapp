from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from decimal import *
from django.db.models.fields import TimeField
import itertools


class Neighborhood(models.Model):
    block_id_neighborhoods = models.IntegerField(primary_key=True)
    block_id_desludgers = models.IntegerField()

    related_neighborhoods = models.ManyToManyField("self", blank=True, null=True)
    fictitious = models.BooleanField(default=False)

    def __str__(self):
        if self.fictitious:
            return str(self.block_id_neighborhoods) + ' (' + str(self.block_id_desludgers) + ') Fictitious'
        return str(self.block_id_neighborhoods) + ' (' + str(self.block_id_desludgers) + ')'


class Landmark(models.Model):
    landmark_id = models.IntegerField(primary_key=True)
    cluster_id = models.IntegerField()
    type_prim_sec = models.IntegerField()
    block_id_desludgers = models.IntegerField()
    block_id_neighborhoods = models.ForeignKey(Neighborhood)
    latitude = models.FloatField()
    longitude = models.FloatField()
    sector_num_ouaga = models.IntegerField()
    neighborhood_name = models.CharField(max_length=200)
    type_of_landmark = models.IntegerField()
    type_other = models.CharField(max_length=200, blank=True)
    does_landmark_have_name = models.IntegerField(null=True)
    landmark_name = models.CharField(max_length=200, blank=True)
    closest_main_street = models.CharField(max_length=200, blank=True)
    arrond = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        if self.does_landmark_have_name == 1:
            return str(self.landmark_id) + ': ' + self.landmark_name
        else:
            return str(self.landmark_id) + ' (no name assignmed)'


class Cluster(models.Model):
    cluster_id = models.IntegerField(primary_key=True)
    block_id_desludgers = models.IntegerField()
    block_id_neighborhoods = models.ForeignKey(Neighborhood)
    sector_num_ouaga = models.IntegerField()
    arrond = models.IntegerField()
    neighborhood_name = models.CharField(max_length=200, blank=True)
    alternate_neighborhood_name = models.CharField(max_length=200, blank=True)
    closest_main_street = models.CharField(max_length=200, blank=True)
    primary_landmark_name = models.CharField(max_length=200, blank=True)
    primary_landmark_id = models.ForeignKey(Landmark, blank=True, null=True, related_name='primary_landmark_id')
    number_additional_landmarks = models.IntegerField(blank=True, null=True)
    general_comments = models.TextField(blank=True, null=True)
    second_landmark_id = models.ForeignKey(Landmark, blank=True, null=True, related_name='second_landmark_id')
    second_landmark_name = models.CharField(max_length=200, blank=True)
    third_landmark_id = models.ForeignKey(Landmark, blank=True, null=True, related_name='third_landmark_id')
    third_landmark_name = models.CharField(max_length=200, blank=True)
    fourth_landmark_id = models.ForeignKey(Landmark, blank=True, null=True, related_name='fourth_landmark_id')
    fourth_landmark_name = models.CharField(max_length=200, blank=True)
    fifth_landmark_id = models.ForeignKey(Landmark, blank=True, null=True, related_name='fifth_landmark_id')
    fifth_landmark_name = models.CharField(max_length=200, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.cluster_id)


class Household(models.Model):
    cleaned_household_id = models.IntegerField(primary_key=True)
    cluster_id = models.IntegerField(blank=True, null=True)
    compound_number = models.IntegerField(blank=True, null=True)
    block_id_desludgers = models.IntegerField()
    block_id_neighborhoods = models.ForeignKey(Neighborhood)
    sector_num_ouaga = models.IntegerField()
    arrond = models.IntegerField()
    neighborhood_name = models.CharField(max_length=200, blank=True)
    alternate_neighborhood_name = models.CharField(max_length=200, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    closest_main_street = models.CharField(max_length=200, blank=True)
    primary_landmark_name = models.CharField(max_length=200, blank=True)
    primary_landmark_id = models.ForeignKey(Landmark, blank=True, null=True,
                                            related_name='household_primary_landmark_id')
    number_additional_landmarks = models.IntegerField(blank=True, null=True)
    second_landmark_id = models.ForeignKey(Landmark, blank=True, null=True, related_name='household_second_landmark_id')
    second_landmark_name = models.CharField(max_length=200, blank=True)
    third_landmark_id = models.ForeignKey(Landmark, blank=True, null=True, related_name='household_third_landmark_id')
    third_landmark_name = models.CharField(max_length=200, blank=True)
    fourth_landmark_id = models.ForeignKey(Landmark, blank=True, null=True, related_name='household_fourth_landmark_id')
    fourth_landmark_name = models.CharField(max_length=200, blank=True)
    fifth_landmark_id = models.ForeignKey(Landmark, blank=True, null=True, related_name='household_fifth_landmark_id')
    fifth_landmark_name = models.CharField(max_length=200, blank=True)
    sixth_landmark_id = models.ForeignKey(Landmark, blank=True, null=True, related_name='household_sixth_landmark_id')
    sixth_landmark_name = models.CharField(max_length=200, blank=True)

    household_firstname = models.CharField(max_length=200, blank=True)
    household_lastname = models.CharField(max_length=200, blank=True)
    household_nickname = models.CharField(max_length=200, blank=True)
    household_survey_bid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    household_phone1 = models.IntegerField(blank=True, null=True)
    household_phone2 = models.IntegerField(blank=True, null=True)
    household_phone3 = models.IntegerField(blank=True, null=True)
    household_num_winners = models.IntegerField()  # Upon fixing household4 change to nullFalse
    household_is_survey = models.BooleanField(default=True)
    household_is_claiming_survey = models.BooleanField(default=False)
    household_is_fictitious = models.BooleanField(default=False)
    household_notes = models.TextField(blank=True, null=True)

    household_head_firstname = models.CharField(max_length=200, blank=True, null=True)
    household_head_lastname = models.CharField(max_length=200, blank=True, null=True)

    price_is_accepted = models.BooleanField(default=False)
    household_fixed_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    HH_CATEGORY_CHOICES = (
        (1, 'Surveyed'),
        (2, 'Non-Surveyed'),
        (3, 'Fixed Price'),
        (4, 'Competitive'),
    )

    household_category = models.IntegerField(blank=True, choices=HH_CATEGORY_CHOICES, null=True)
    is_hh_select_tank = models.BooleanField(default=False)
    hh_selected_tank_size = models.IntegerField(blank=True, null=True)
    hh_bid_accepted_time = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.save()

    def __str__(self):
        return str(self.cleaned_household_id)


class Supplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    driver_firstname = models.CharField(max_length=200, blank=True)
    driver_lastname = models.CharField(max_length=200, blank=True)
    driver_phone1 = models.IntegerField(blank=True, null=True)
    driver_phone2 = models.IntegerField(blank=True, null=True)
    driver_phone3 = models.IntegerField(blank=True, null=True)
    truck1_plate = models.CharField(max_length=200, blank=True)
    truck2_plate = models.CharField(max_length=200, blank=True, null=True)
    truck1_volume = models.CharField(max_length=200, blank=True)
    truck2_volume = models.CharField(max_length=200, blank=True, null=True)
    owner_firstname = models.CharField(max_length=200, blank=True)
    owner_lastname = models.CharField(max_length=200, blank=True)
    enterprise_name = models.CharField(max_length=200, blank=True, null=True)
    owner_phone1 = models.IntegerField(blank=True, null=True)
    owner_phone2 = models.CharField(max_length=100, blank=True, null=True)
    contact_name = models.CharField(max_length=200, blank=True, null=True)
    contact_phone1 = models.IntegerField(blank=True, null=True)
    contact_phone2 = models.IntegerField(blank=True, null=True)


    # driver_name = models.CharField(max_length=200, blank=True)
    # license_number = models.CharField(max_length=200, blank=True)
    # plate_number = models.CharField(max_length=200, blank=True)
    # driver_phone = models.IntegerField(blank=True, null=True)
    # owner_name = models.CharField(max_length=200, blank=True)
    # owner_phone = models.IntegerField(blank=True, null=True)
    # truck_size = models.CharField(max_length=200, blank=True)
    # hose_addition = models.BooleanField(default=False)
    # main_garage = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(
            self.supplier_id) + ' ' + self.driver_firstname + ' ' + self.driver_lastname + ' (owner: ' + self.owner_firstname + ' ' + self.owner_lastname + ')'


class SupplierBid(models.Model):
    CHOICES = (
        (1, 'Petit'),
        (2, 'Grand'),
    )

    supplier = models.ForeignKey(Supplier)
    offer_start_date = models.DateField(default=timezone.now)
    offer_end_date = models.DateField()
    neighborhoods_serviced = models.ManyToManyField(Neighborhood, blank=True, null=True)
    neighborhoods_serviced_2 = models.ForeignKey(Neighborhood, related_name='neighborhoods_serviced_2', blank=True,
                                                 null=True)  #
    full_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_advance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    number_payment_advance = models.IntegerField(default=0)
    original_number_payment_advance = models.IntegerField(default=0)
    tank_size = models.IntegerField(blank=True, choices=CHOICES, default=1)
    auctions_won = models.IntegerField(default=0)

    rejected_hh_bids = models.ManyToManyField('HouseholdBid', default=None, null=True)
    # altenative_supplier_bids field is used for to save the supplier bid when purpose alternative bidder button is clicked to avoid the repetition
    altenative_supplier_bids = models.ManyToManyField('HouseholdBid', default=None, null=True,
                                                      related_name="alternative_supplierbids")
    random_supplier_bid = models.ManyToManyField('HouseholdBid', default=None, null=True,
                                                 related_name="random_supplierbid")
    supplier_rank = models.PositiveIntegerField(default=0)
    HH_SET_CHOICES = (
        (1, 'Surveyed'),
        (2, 'Non-Surveyed'),
        (3, 'Fixed Price'),
        (4, 'Competitive'),
    )

    household_set_number = models.IntegerField(blank=True, choices=HH_SET_CHOICES, null=True)

    def __str__(self):
        return str(self.supplier.supplier_id) + ' (' + self.offer_start_date.strftime('%Y-%m-%d %H:%M') + ')'


class HouseholdBid(models.Model):
    CHOICES = [(i, i) for i in range(1, 6)]

    household = models.ForeignKey(Household)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_exception_1 = models.BooleanField(default=False)
    bid_exception_2 = models.BooleanField(default=False)
    bid_other_notes = models.TextField(blank=True, null=True)
    bid_date = models.DateTimeField(default=timezone.now)
    bid_win = models.BooleanField(default=False)
    bid_win_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bid_competing = models.ManyToManyField("self", blank=True, null=True)
    assigned_supplier_offer = models.ForeignKey(SupplierBid, blank=True, null=True)
    no_supplier_found = models.BooleanField(default=False)
    household_rating_supplier = models.IntegerField(blank=True, null=True, choices=CHOICES)
    household_comments = models.TextField(blank=True, null=True)
    job_complete = models.BooleanField(blank=True, default=None)
    date_completed = models.DateTimeField(blank=True, null=True)
    bid_canceled = models.BooleanField(blank=True, default=None)
    is_hh_refuse_price = models.BooleanField(default=False)

    def __str__(self):
        return str(self.household.cleaned_household_id) + ' (' + self.bid_date.strftime('%Y-%m-%d %H:%M') + ')'

    def assignInitialSupplier(self):

        if self.household.household_is_survey:
            hh_lastes_bid = []
            bid_against_exclude_self = []
            # Get all the households form the that neighbourhood form which HH calling
            survey_househodls_list = list(
                Household.objects.filter(block_id_neighborhoods=self.household.block_id_neighborhoods,
                                         household_is_survey=True).exclude(household_category__in=[3, 4]))
            competitors = 8
            househodls_list = survey_househodls_list
            if ( not self.bid_exception_1) and (not self.bid_exception_2):
                #Get all the fictitious householdbids
                fictitious_householdbids_list = list(HouseholdBid.objects.filter(
                    household__block_id_neighborhoods=self.household.block_id_neighborhoods.related_neighborhoods.all(),
                    bid_exception_1=False, bid_exception_2=False, household__household_is_survey=True,
                    household__household_is_fictitious=True))
                for house_hold in househodls_list:
                    hh_lastes_bid = HouseholdBid.objects.filter(bid_exception_1=False, bid_exception_2=False,
                                                                household__household_is_survey=True,
                                                                household=house_hold.cleaned_household_id).exclude(
                        household=self.household).order_by('-bid_date').first()
                    if hh_lastes_bid:
                        bid_against_exclude_self.append(hh_lastes_bid)
            if (self.bid_exception_1) and (not self.bid_exception_2):
                #Get all the fictitious householdbids
                fictitious_householdbids_list = list(HouseholdBid.objects.filter(
                    household__block_id_neighborhoods=self.household.block_id_neighborhoods.related_neighborhoods.all(),
                    bid_exception_1=True, bid_exception_2=False, household__household_is_survey=True,
                    household__household_is_fictitious=True))
                for house_hold in househodls_list:
                    hh_lastes_bid = HouseholdBid.objects.filter(bid_exception_1=True, bid_exception_2=False,
                                                                household__household_is_survey=True,
                                                                household=house_hold.cleaned_household_id).exclude(
                        household=self.household).order_by('-bid_date').first()
                    if hh_lastes_bid:
                        bid_against_exclude_self.append(hh_lastes_bid)

            if (not self.bid_exception_1) and (self.bid_exception_2):
                #Get all the fictitious householdbids
                fictitious_householdbids_list = list(HouseholdBid.objects.filter(
                    household__block_id_neighborhoods=self.household.block_id_neighborhoods.related_neighborhoods.all(),
                    bid_exception_1=False, bid_exception_2=True, household__household_is_survey=True,
                    household__household_is_fictitious=True))
                for house_hold in househodls_list:
                    hh_lastes_bid = HouseholdBid.objects.filter(bid_exception_1=False, bid_exception_2=True,
                                                                household__household_is_survey=True,
                                                                household=house_hold.cleaned_household_id).exclude(
                        household=self.household).order_by('-bid_date').first()
                    if hh_lastes_bid:
                        bid_against_exclude_self.append(hh_lastes_bid)

            if (self.bid_exception_1) and (self.bid_exception_2):
                #Get all the fictitious householdbids
                fictitious_householdbids_list = list(HouseholdBid.objects.filter(
                    household__block_id_neighborhoods=self.household.block_id_neighborhoods.related_neighborhoods.all(),
                    bid_exception_1=True, bid_exception_2=True, household__household_is_survey=True,
                    household__household_is_fictitious=True))
                for house_hold in househodls_list:
                    hh_lastes_bid = HouseholdBid.objects.filter(bid_exception_1=True, bid_exception_2=True,
                                                                household__household_is_survey=True,
                                                                household=house_hold.cleaned_household_id).exclude(
                        household=self.household).order_by('-bid_date').first()
                    if hh_lastes_bid:
                        bid_against_exclude_self.append(hh_lastes_bid)
            bid_against_exclude_self = bid_against_exclude_self + fictitious_householdbids_list
            bid_against_exclude_self.sort(key=lambda x: x.bid_date)
            bid_against_exclude_self = bid_against_exclude_self[-competitors:]
            self.bid_competing.add(*bid_against_exclude_self)

            if len(bid_against_exclude_self) >= 8:
                # Conditions to check if the household won the auction
                min_win = bid_against_exclude_self[-self.household.household_num_winners].bid_amount

                if self.bid_amount >= min_win:
                    self.bid_win = True
                    self.bid_win_pay = min_win

                # If we win the auction, assign the supplier
                if self.bid_win:

                    #For now we are just checking if the server time is between start_date and end_date
                    assigned_supplier = None

                    if self.bid_exception_1:
                        assigned_supplier = list(SupplierBid.objects.filter(
                            neighborhoods_serviced_2__in=[self.household.block_id_neighborhoods.block_id_neighborhoods],
                            offer_start_date__lte=timezone.now(), offer_end_date__gte=timezone.now(),
                            tank_size=2).order_by('full_price', 'auctions_won', '?').exclude(household_set_number=4)[
                                                 :1])
                    else:
                        assigned_supplier = list(SupplierBid.objects.filter(
                            neighborhoods_serviced_2__in=[self.household.block_id_neighborhoods.block_id_neighborhoods],
                            offer_start_date__lte=timezone.now(), offer_end_date__gte=timezone.now(),
                            tank_size=1).order_by('full_price', 'auctions_won', '?').exclude(household_set_number=4)[
                                                 :1])

                    # Check to make sure that a supplier actually exists
                    if assigned_supplier:
                        self.assigned_supplier_offer = assigned_supplier[0]
                        self.no_supplier_found = False
                        assigned_supplier[0].auctions_won += 1
                        assigned_supplier[0].save()
                    else:
                        self.no_supplier_found = True
                        self.bid_canceled = True
                        self.assigned_supplier_offer = None
            else:
                self.bid_win = False
                self.bid_canceled = True
                self.assigned_supplier_offer = None

        elif self.household.household_category not in [3, 4]:

            assigned_supplier = None

            if self.bid_exception_1:
                assigned_supplier = list(SupplierBid.objects.filter(
                    neighborhoods_serviced_2__in=[self.household.block_id_neighborhoods.block_id_neighborhoods],
                    offer_start_date__lte=timezone.now(), offer_end_date__gte=timezone.now(),
                    full_price__lte=self.bid_amount, tank_size=2).order_by('full_price', 'auctions_won', '?').exclude(
                    household_set_number=4)[:1])
            else:
                assigned_supplier = list(SupplierBid.objects.filter(
                    neighborhoods_serviced_2__in=[self.household.block_id_neighborhoods.block_id_neighborhoods],
                    offer_start_date__lte=timezone.now(), offer_end_date__gte=timezone.now(),
                    full_price__lte=self.bid_amount, tank_size=1).order_by('full_price', 'auctions_won', '?').exclude(
                    household_set_number=4)[:1])

            if assigned_supplier:
                self.bid_win = True
                self.bid_win_pay = self.bid_amount
                self.assigned_supplier_offer = assigned_supplier[0]
                self.no_supplier_found = False
                assigned_supplier[0].auctions_won += 1
                assigned_supplier[0].save()
            else:
                self.no_supplier_found = True
                self.bid_canceled = True
                self.assigned_supplier_offer = None

        if self.household.household_category == 3:
            self.bid_win = True
            self.bid_win_pay = self.bid_amount


            # For now we are just checking if the server time is between start_date and end_date
            assigned_supplier = None

            if self.bid_exception_1:
                assigned_supplier = list(SupplierBid.objects.filter(
                    neighborhoods_serviced_2__in=[self.household.block_id_neighborhoods.block_id_neighborhoods],
                    offer_start_date__lte=timezone.now(), offer_end_date__gte=timezone.now(), tank_size=2).order_by(
                    'full_price', 'auctions_won', '?').exclude(household_set_number=4)[:1])
            else:
                assigned_supplier = list(SupplierBid.objects.filter(
                    neighborhoods_serviced_2__in=[self.household.block_id_neighborhoods.block_id_neighborhoods],
                    offer_start_date__lte=timezone.now(), offer_end_date__gte=timezone.now(), tank_size=1).order_by(
                    'full_price', 'auctions_won', '?').exclude(household_set_number=4)[:1])

            # Check to make sure that a supplier actually exists
            if assigned_supplier:
                self.assigned_supplier_offer = assigned_supplier[0]
                self.no_supplier_found = False
                assigned_supplier[0].auctions_won += 1
                assigned_supplier[0].save()
            else:
                self.no_supplier_found = True
                self.bid_canceled = True
                self.assigned_supplier_offer = None

        self.save()

    def assignSupplierBid(self, supplier_bid_id):
        self.bid_win = True

        assigned_supplier = SupplierBid.objects.get(pk=supplier_bid_id)

        if assigned_supplier:
            self.assigned_supplier_offer = assigned_supplier
            self.bid_win_pay = self.bid_amount
            self.no_supplier_found = False

            assigned_supplier.auctions_won += 1
            assigned_supplier.save()

        self.save()

    def markJobCompleted(self, request):

        use_advance = False
        advance_amount = Decimal(0.00)

        if self.household.household_is_survey or self.household.household_category in [3, 4]:

            if self.assigned_supplier_offer.number_payment_advance > 0:
                use_advance = True
                advance_amount = self.assigned_supplier_offer.payment_advance

                supplierbid = get_object_or_404(SupplierBid, pk=self.assigned_supplier_offer.pk)
                supplierbid.number_payment_advance -= 1
                supplierbid.save()

        if self.assigned_supplier_offer.full_price > 20000 and self.household.household_category == 4 and self.assigned_supplier_offer.tank_size == 1:
            total_price = 20000
        elif self.assigned_supplier_offer.full_price > 35000 and self.household.household_category == 4 and self.assigned_supplier_offer.tank_size == 2:
            total_price = 35000
        else:
            total_price = self.assigned_supplier_offer.full_price
        amount_due = total_price - (self.bid_win_pay + advance_amount)
        payment = Payment(householdbid=self, supplierbid=self.assigned_supplier_offer, advance_used=use_advance,
                          amount_due=amount_due, user_job_done=request.user)
        payment.save()


class Payment(models.Model):
    householdbid = models.ForeignKey(HouseholdBid)
    supplierbid = models.ForeignKey(SupplierBid)

    advance_used = models.BooleanField(default=False)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)

    date_opened = models.DateTimeField(default=timezone.now)
    date_payment_sent = models.DateTimeField(blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)

    payment_sent = models.BooleanField(default=False)
    payment_completed = models.BooleanField(default=False)

    user_job_done = models.ForeignKey(User, null=True, related_name='user_job_done')
    user_payment_sent = models.ForeignKey(User, null=True, related_name='user_payment_sent')
    user_payment_confirmed = models.ForeignKey(User, null=True, related_name='user_payment_confirmed')


class LowActivityDesludger(models.Model):
    supplierbid = models.ForeignKey(SupplierBid)
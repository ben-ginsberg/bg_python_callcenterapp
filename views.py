from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from .models import *
from .forms import *
from django.forms.models import modelform_factory
from django.utils import timezone
from decimal import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.db.models import Q, Count
import datetime
import random


@login_required
def index(request):
    return render(request, 'callcenterapp/index.html', {})


@login_required
def neighborhood_list(request):
    neighborhoods = Neighborhood.objects.all().order_by('block_id_neighborhoods')
    landmarks = Landmark.objects.all().order_by('landmark_name')

    return render(request, 'callcenterapp/neighborhood_list.html',
                  {'neighborhoods': neighborhoods, 'landmarks': landmarks})


@login_required
def household_list(request):
    households = Household.objects.all().order_by('cleaned_household_id')
    return render(request, 'callcenterapp/household_list.html', {'households': households})


@login_required
def neighborhood_detail(request, blockid):
    households = Household.objects.filter(block_id_neighborhoods=blockid).order_by('cleaned_household_id')

    return render(request, 'callcenterapp/neighborhood_detail.html', {'households': households})


@login_required
def household_detail(request, houseid):
    household = get_object_or_404(Household, cleaned_household_id=houseid)
    bid_time_minute = None
    bid_time_seconds = None
    time_diff = None
    # listed_price_option is used to identify if a supplier do job on negotiation price or its orignals price
    listed_price_option = False
    #on click "propose alternative bidder" the supplier bid we exclued the loaded supplier bids on template
    desludger_tank_size = None
    negotiation_price = None
    current_household_bid = None
    exculed_supplier_bids_list = []
    lowest_supplierbid = []
    competative_supplierbid_list = []
    low_activity_bid_ids = []
    low_activity_supplier_bid = None
    included_lowest_supplier_bid = None
    alternative_three_supplierbids_list = []
    exculed_alternative_supplier_bids = []
    include_randow_supplier_bids = []
    neighborhoods = [household.block_id_neighborhoods.block_id_neighborhoods]
    # Get last HH bid.
    householdbid = (
        HouseholdBid.objects
        .filter(household=household)
        .order_by('-bid_date').first()
    )
    if householdbid:
        if not householdbid.bid_win:
            exculed_alternative_supplier_bids = householdbid.alternative_supplierbids.all().values_list('id', flat=True)
            include_randow_supplier_bids = householdbid.random_supplierbid.all().values_list('id', flat=True)
    if "sizeoftank" in request.POST:
        if "tank_size" in request.POST:
            desludger_tank_size = int(request.POST.get("tank_size"))
            household.is_hh_select_tank = True
            household.hh_selected_tank_size = desludger_tank_size
            household.save()
    if "alternativebidBtn" in request.POST:
        listed_price_option = True
        SupplierBid.random_supplier_bid.through.objects.all().delete()
        LowActivityDesludger.objects.all().delete()
        if "current_bid" in request.POST:
            current_household_bid = int(request.POST.get("current_bid"))
        if "lowestSupplier" in request.POST:
            included_lowest_supplier_bid = int(request.POST.get("lowestSupplier"))
        if "compitativeSupplier1" in request.POST:
            exculed_supplier_bids_list.append(int(request.POST.get("compitativeSupplier1")))
            altenative_bid = get_object_or_404(SupplierBid, id=int(request.POST.get("compitativeSupplier1")))
            altenative_bid.altenative_supplier_bids.add(current_household_bid)
        if "compitativeSupplier2" in request.POST:
            exculed_supplier_bids_list.append(int(request.POST.get("compitativeSupplier2")))
            altenative_bid = get_object_or_404(SupplierBid, id=int(request.POST.get("compitativeSupplier2")))
            altenative_bid.altenative_supplier_bids.add(current_household_bid)
        if "compitativeSupplier3" in request.POST:
            exculed_supplier_bids_list.append(int(request.POST.get("compitativeSupplier3")))
            altenative_bid = get_object_or_404(SupplierBid, id=int(request.POST.get("compitativeSupplier3")))
            altenative_bid.altenative_supplier_bids.add(current_household_bid)
        if included_lowest_supplier_bid:
            lowest_supplierbid = SupplierBid.objects.get(pk=included_lowest_supplier_bid)
            negotiation_price = lowest_supplierbid.full_price - 500
            exculed_supplier_bids_list.append(lowest_supplierbid.id)
            request.session['lowest_supplier_bid'] = lowest_supplierbid.id
        househod_bid = HouseholdBid.objects.get(pk=current_household_bid)
        alternative_supplier_bids_list = househod_bid.alternative_supplierbids.all()
        if alternative_supplier_bids_list:
            for supp_bid_id in alternative_supplier_bids_list:
                exculed_supplier_bids_list.append(supp_bid_id.id)

        alternative_supplierbids_list = list(SupplierBid.objects.filter(neighborhoods_serviced_2__in=neighborhoods, \
                                                                        offer_start_date__lte=timezone.now(), \
                                                                        offer_end_date__gte=timezone.now(), \
                                                                        tank_size=household.hh_selected_tank_size,
                                                                        household_set_number=4).exclude(
            id__in=exculed_supplier_bids_list))
        if alternative_supplierbids_list:
            random.shuffle(alternative_supplierbids_list)
            alternative_three_supplierbids_list = alternative_supplierbids_list[:3]

        if len(alternative_three_supplierbids_list) > 0:
            competative_supplierbid_list = alternative_three_supplierbids_list
            for altenative_bid in competative_supplierbid_list:
                altenative_bid.random_supplier_bid.add(current_household_bid)

    elif include_randow_supplier_bids:
        if request.session.get('lowest_supplier_bid'):
            lowest_supplierbid = SupplierBid.objects.get(pk=request.session.get('lowest_supplier_bid'))
            negotiation_price = lowest_supplierbid.full_price - 500
        random_bid_list = list(include_randow_supplier_bids)
        competative_supplierbid_list = list(SupplierBid.objects.filter(id__in=include_randow_supplier_bids))
        for competetative_bid in competative_supplierbid_list:
            pop_old_index = competative_supplierbid_list.index(competetative_bid)
            index_of_random_list = random_bid_list.index(competetative_bid.id)
            competative_supplierbid_list.insert(index_of_random_list, competative_supplierbid_list.pop(pop_old_index))
    else:
        if exculed_alternative_supplier_bids:
            suppliers = (
                SupplierBid.objects
                .filter(neighborhoods_serviced_2__in=neighborhoods,
                        offer_start_date__lte=timezone.now(),
                        offer_end_date__gte=timezone.now(), tank_size=household.hh_selected_tank_size,
                        household_set_number=4).exclude(id__in=exculed_alternative_supplier_bids)
            )
        else:
            suppliers = (
                SupplierBid.objects
                .filter(neighborhoods_serviced_2__in=neighborhoods,
                        offer_start_date__lte=timezone.now(),
                        offer_end_date__gte=timezone.now(), tank_size=household.hh_selected_tank_size,
                        household_set_number=4)
            )
        if suppliers:
            suppliers_list = list(suppliers.order_by('full_price', 'supplier_rank')[:3])
            lowest_supplierbid = suppliers_list[0]
            competative_supplierbid_list = suppliers_list[1:3]
            negotiation_price = lowest_supplierbid.full_price - 500
            # Get all valid supplier bid IDs in our neighborhoods.
            supplier_ids = suppliers.values_list('pk', flat=True)

            # Select the suppliers bids which have least
            # amount of auctions won but exclude the
            # lowest price supplier and previous two
            # competivie suppliers.
            to_exclude = [supplier.id for supplier in suppliers_list]

            low_activity_supplier_bids = (
                SupplierBid.objects
                .filter(id__in=supplier_ids)
                .exclude(id__in=to_exclude)
            )

            low_activity_bid_ids = low_activity_supplier_bids.values_list('pk', flat=True)
            if len(low_activity_bid_ids) > 0:
                # Now randomly select any one.
                low_activity_desludger_bid = LowActivityDesludger.objects.filter(supplierbid__in=low_activity_bid_ids)
                if not low_activity_desludger_bid:
                    index = random.randrange(0, len(low_activity_bid_ids))
                    low_activity_supplier_bid = suppliers.get(pk=low_activity_bid_ids[index])
                    lowactivitysupplier = LowActivityDesludger(supplierbid=low_activity_supplier_bid)
                    lowactivitysupplier.save()
                else:
                    low_activity_supplier_bid = suppliers.get(pk=low_activity_desludger_bid[0].supplierbid.id)
                competative_supplierbid_list.append(low_activity_supplier_bid)


    #Here we set a variable that make the buttons disable on rejects button click
    if householdbid:
        all_suppliers = [lowest_supplierbid]
        all_suppliers.extend(competative_supplierbid_list)
        all_suppliers.extend([low_activity_supplier_bid])
        if all_suppliers:
            for supplier in all_suppliers:
                if supplier:
                    rejected_bids = (
                        supplier.rejected_hh_bids
                        .all()
                        .values_list('id', flat=True)
                    )

                    supplier.is_rejected = householdbid.id in rejected_bids

    householdbids = HouseholdBid.objects.filter(household__cleaned_household_id=houseid).order_by('-bid_date')
    #household_category value 4 is to represent the Competitive HH
    if household.household_category == 4 and household.price_is_accepted:
        time_diff = timezone.now() - household.hh_bid_accepted_time
        time_minute = time_diff.total_seconds() / 60
        time_second = time_diff.total_seconds() % 60
        if time_second >= 0 and time_minute >= 0 and time_minute <= 59:
            bid_time_seconds = int(time_second)
            bid_time_minute = int(time_minute)
            bid_time_minute = 59 - bid_time_minute
            bid_time_seconds = 59 - bid_time_seconds
    return render(request, 'callcenterapp/household_detail.html',
                  {'household': household,
                   'householdbids': householdbids,
                   'lowest_supplierbid': lowest_supplierbid,
                   'negotiation_price': negotiation_price,
                   'competative_supplierbid_list': competative_supplierbid_list,
                   'bid_time_minute': bid_time_minute, 'bid_time_seconds': bid_time_seconds,
                   'listed_price_option': listed_price_option})


@login_required
def household_edit(request, houseid):
    household = get_object_or_404(Household, cleaned_household_id=houseid)

    if request.method == "POST":

        form = HouseholdEditForm(request.POST, instance=household)
        if form.is_valid():
            household = form.save(commit=False)
            household.save()
            return redirect('callcenterapp.views.household_detail', houseid=household.cleaned_household_id)
    else:
        form = HouseholdEditForm(instance=household)

    return render(request, 'callcenterapp/household_edit.html', {'form': form})


@login_required
def household_newnonsurvey(request):
    if request.method == "POST":

        form = HouseholdNonSurveyForm(request.POST)

        if form.is_valid():
            household = form.save(commit=False)

            new_id = 0

            while True:

                new_id = random.randrange(9000, 10000)
                households_match = Household.objects.filter(cleaned_household_id=new_id)[:1]
                list_match = list(households_match)

                if len(list_match) == 0:
                    break

            household.cleaned_household_id = new_id

            new_landmark = Landmark.objects.get(landmark_id=household.primary_landmark_id.landmark_id)

            household.primary_landmark_name = new_landmark.landmark_name

            household.cluster_id = 0
            household.compound_number = 0
            household.block_id_desludgers = new_landmark.block_id_neighborhoods.block_id_desludgers
            household.block_id_neighborhoods = new_landmark.block_id_neighborhoods
            household.sector_num_ouaga = 0
            household.arrond = 0
            household.neighborhood_name = ""
            household.alternate_neighborhood_name = ""
            household.latitude = 0.0
            household.longitude = 0.0
            household.household_is_survey = False
            household.household_num_winners = 0  # We don't care about predetermined winners in this case

            household.save()

            return household_detail(request, household.cleaned_household_id)
    else:
        form = HouseholdNonSurveyForm()
        form.fields['primary_landmark_id'].empty_label = None

    return render(request, 'callcenterapp/household_newnonsurvey.html', {'form': form})


@login_required
def householdbid_list(request):
    householdbids = HouseholdBid.objects.exclude(
        household__in=Household.objects.filter(household_category__in=[3, 4])).order_by('-bid_win', 'job_complete',
                                                                                        '-bid_date')
    return render(request, 'callcenterapp/householdbid_list.html', {'householdbids': householdbids})


@login_required
def household_fix_pricebid_list(request):
    householdbids = HouseholdBid.objects.filter(household__in=Household.objects.filter(household_category=3)).order_by(
        '-bid_win', 'job_complete', '-bid_date')
    return render(request, 'callcenterapp/householdfixpricebids_list.html', {'householdbids': householdbids})


@login_required
def household_competitonbid_list(request):
    householdbids = HouseholdBid.objects.filter(household__in=Household.objects.filter(household_category=4)).order_by(
        '-bid_win', 'job_complete', '-bid_date')
    return render(request, 'callcenterapp/householdcompetativebids_list.html', {'householdbids': householdbids})


@login_required
def householdbid_detail(request, pk):
    householdbid = get_object_or_404(HouseholdBid, pk=pk)
    payment = Payment.objects.filter(householdbid=householdbid)
    template = None

    if householdbid.household.household_category == 3:
        template = 'callcenterapp/householdbid_fixed_price_detail.html'
    elif householdbid.household.household_category == 4:
        template = 'callcenterapp/household_competaticebid_detail.html'
    else:
        template = 'callcenterapp/householdbid_detail.html'

    return render(request, template, {'householdbid': householdbid, 'payment': payment})


@login_required
def householdbid_new(request, houseid, is_reject=None, supplier_bid_id=None,
                     negotiation_price=None):
    household = get_object_or_404(Household, cleaned_household_id=houseid)

    if household.household_category == 3:
        if is_reject:
            householdbid = HouseholdBid(household=household, job_complete=False,
                                        bid_canceled=True, bid_amount=household.household_fixed_price)
            householdbid.save()

            household.price_is_accepted = False
            household.save()
        else:
            if request.method == "POST":
                form = HouseholdBidForm(request.POST)
                if form.is_valid():
                    householdbid = form.save(commit=False)
                    householdbid.household = household

                    householdbid.job_complete = False
                    householdbid.bid_canceled = False
                    householdbid.save()

                    household.price_is_accepted = True
                    household.save()

                    householdbid.assignInitialSupplier()

                    return redirect('callcenterapp.views.householdbid_detail', pk=householdbid.pk)
            else:
                form = HouseholdBidForm(initial={'bid_amount': household.household_fixed_price})

            return render(request, "callcenterapp/fixedpricehhbid_new.html", {'form': form})
        
        return redirect('callcenterapp.views.householdbid_detail', pk=householdbid.pk)

    elif household.household_category == 4:

        if household.price_is_accepted and supplier_bid_id and is_reject:
            supplier_bid = get_object_or_404(SupplierBid, id=supplier_bid_id)
            # get last HH bid
            householdbid = (
                HouseholdBid.objects
                .filter(household=household)
                .order_by('-bid_date').first()
            )

            if householdbid:
                supplier_bid.rejected_hh_bids.add(householdbid.id)
        elif household.price_is_accepted and supplier_bid_id:
            supplier_bid = get_object_or_404(SupplierBid, id=supplier_bid_id)
            # get last HH bid
            householdbid = (
                HouseholdBid.objects
                .filter(household=household)
                .order_by('-bid_date').first()
            )

            if householdbid:
                householdbid.job_complete = False
                householdbid.bid_canceled = False
                householdbid.save()
                householdbid.assignSupplierBid(supplier_bid.id)
                return redirect('callcenterapp.views.householdbid_detail', pk=householdbid.pk)
        else:
            householdbid = HouseholdBid(household=household, job_complete=False,
                                        bid_canceled=False, bid_amount=negotiation_price)
            if household.hh_selected_tank_size == 2:
                # bid_exception_1 = True means large tank is selected for that bid.
                householdbid.bid_exception_1 = True
            householdbid.save()
            household.hh_bid_accepted_time = datetime.datetime.now()
            household.price_is_accepted = True
            household.save()

        return redirect('callcenterapp.views.household_detail', houseid=houseid)
    else:
        if request.method == "POST":

            form = HouseholdBidForm(request.POST)

            if form.is_valid():
                householdbid = form.save(commit=False)
                householdbid.household = get_object_or_404(Household, cleaned_household_id=houseid)

                householdbid.job_complete = False
                householdbid.bid_canceled = False
                householdbid.save()

                householdbid.assignInitialSupplier()

                return redirect('callcenterapp.views.householdbid_detail', pk=householdbid.pk)
        else:
            form = HouseholdBidForm()

        return render(request, "callcenterapp/householdbid_new.html", {'form': form})


@login_required
def supplier_accept_job_on_listed_price(request, houseid, supplier_bid_id):
    household = get_object_or_404(Household, cleaned_household_id=houseid)
    # get last HH bid
    householdbid = (
        HouseholdBid.objects
        .filter(household=household)
        .order_by('-bid_date').first()
    )
    if household.price_is_accepted and supplier_bid_id:
        supplier_bid = get_object_or_404(SupplierBid, id=supplier_bid_id)
        if householdbid:
            householdbid.job_complete = False
            householdbid.bid_canceled = False
            householdbid.save()
            householdbid.assignSupplierBid(supplier_bid.id)
            return redirect('callcenterapp.views.householdbid_detail', pk=householdbid.pk)


@login_required
def householdbid_new_upadte_price(request, houseid, supplier_bid_id=None, negotiation_price=None):
    household = get_object_or_404(Household, cleaned_household_id=houseid)
    neighborhood = [household.block_id_neighborhoods.block_id_neighborhoods]
    if household.household_category == 4:

        if household.price_is_accepted and supplier_bid_id and negotiation_price:
            supplier_bid = get_object_or_404(SupplierBid, id=supplier_bid_id)
            supplier_bid.supplier_rank = 1
            supplier_bid.full_price = negotiation_price
            supplier_list_for_update_rank = SupplierBid.objects.filter(neighborhoods_serviced_2__in=neighborhood, \
                                                                       offer_start_date__lte=timezone.now(), \
                                                                       offer_end_date__gte=timezone.now(), \
                                                                       tank_size=household.hh_selected_tank_size, \
                                                                       full_price__gte=supplier_bid.full_price,
                                                                       household_set_number=4). \
                order_by('full_price', 'supplier_rank'). \
                exclude(supplier=supplier_bid.supplier)
            if supplier_list_for_update_rank:
                rank_count = 1
                for supplier in supplier_list_for_update_rank:
                    rank_count += 1
                    supplier.supplier_rank = rank_count
                    supplier.save()
            supplier_bid.save()
            # get last HH bid
            householdbid = (HouseholdBid.objects
                            .filter(household=household)
                            .order_by('-bid_date').first()
            )

            if householdbid:
                householdbid.job_complete = False
                householdbid.bid_canceled = False
                householdbid.save()
                householdbid.assignSupplierBid(supplier_bid.id)

    return redirect('callcenterapp.views.householdbid_detail', pk=householdbid.pk)


@login_required
def household_rejects_bid_price(request, houseid, negotiation_price=None, hh_rejects_price=None):
    SupplierBid.altenative_supplier_bids.through.objects.all().delete()
    household = get_object_or_404(Household, cleaned_household_id=houseid)
    LowActivityDesludger.objects.all().delete()
    if household and negotiation_price and hh_rejects_price:
        householdbid = HouseholdBid(household=household, job_complete=False,
                                    bid_canceled=True, bid_amount=negotiation_price)
        householdbid.save()
        household.is_hh_select_tank = False
        household.hh_selected_tank_size = None
        household.price_is_accepted = False
        household.save()
    return render(request, 'callcenterapp/household_competaticebid_detail.html', {'householdbid': householdbid})


@login_required
def household_refuse_price(request, pk):
    SupplierBid.altenative_supplier_bids.through.objects.all().delete()
    householdbid = get_object_or_404(HouseholdBid, pk=pk)
    household = get_object_or_404(Household, cleaned_household_id=householdbid.household.cleaned_household_id)
    if request.method == "POST":
        LowActivityDesludger.objects.all().delete()
        form = HouseholdBidCancelBidForm(request.POST, instance=householdbid)

        if form.is_valid():
            householdbid = form.save(commit=False)
            householdbid.bid_canceled = True
            householdbid.is_hh_refuse_price = True
            householdbid.save()
            household.is_hh_select_tank = False
            household.hh_selected_tank_size = None
            household.price_is_accepted = False
            household.save()
            return redirect('callcenterapp.views.householdbid_detail', pk=pk)
    else:
        form = HouseholdBidCancelBidForm(instance=householdbid)

    return render(request, 'callcenterapp/householdbid_cancelprice.html', {'form': form})


@login_required
def householdbid_markcompleted(request, pk):
    SupplierBid.altenative_supplier_bids.through.objects.all().delete()
    householdbid = get_object_or_404(HouseholdBid, pk=pk)
    household = get_object_or_404(Household, cleaned_household_id=householdbid.household.cleaned_household_id)
    if request.method == "POST":
        LowActivityDesludger.objects.all().delete()
        form = HouseholdBidMarkCompleteForm(request.POST, instance=householdbid)

        if form.is_valid():
            # Now on job done we set household variables is_hh_select_tank to false and hh_selected_tank_size is None
            household.is_hh_select_tank = False
            household.hh_selected_tank_size = None
            household.price_is_accepted = False
            household.save()
            householdbid = form.save(commit=False)
            householdbid.job_complete = True
            householdbid.date_completed = timezone.now()
            householdbid.save()

            householdbid.markJobCompleted(request)

            return redirect('callcenterapp.views.householdbid_detail', pk=pk)
    else:
        form = HouseholdBidMarkCompleteForm(instance=householdbid)
        if householdbid.household.household_category == 4:
            return render(request, 'callcenterapp/competativebid_markcompleted.html', {'form': form})
        elif householdbid.household.household_category == 3:
            return render(request, 'callcenterapp/fixeprice_markcompleted.html', {'form': form})
        else:
            return render(request, 'callcenterapp/householdbid_markcompleted.html', {'form': form})


@login_required
def householdbid_changesupplier(request, pk):
    householdbid = get_object_or_404(HouseholdBid, pk=pk)

    if request.method == "POST":

        previous_supplier_bid = get_object_or_404(SupplierBid, pk=householdbid.assigned_supplier_offer.pk)
        form = HouseholdBidChangeSupplierForm(request.POST, instance=householdbid)

        if form.is_valid():

            previous_supplier_bid.auctions_won -= 1
            previous_supplier_bid.save()

            householdbid = form.save(commit=False)
            householdbid.save()

            if householdbid.assigned_supplier_offer is not None:
                new_supplier_bid = get_object_or_404(SupplierBid, pk=householdbid.assigned_supplier_offer.pk)
                new_supplier_bid.auctions_won += 1
                new_supplier_bid.save()
            else:
                householdbid.no_supplier_found = True
                householdbid.bid_canceled = True
                householdbid.save()

            print 'new assigned: %r' % (householdbid.assigned_supplier_offer)
            return redirect('callcenterapp.views.householdbid_detail', pk=pk)
    else:
        form = HouseholdBidChangeSupplierForm(instance=householdbid)

        # Handling the large tank restriction for survey households
        if householdbid.bid_exception_1:
            supplierbids_list = SupplierBid.objects.filter(
                neighborhoods_serviced_2__in=[householdbid.household.block_id_neighborhoods.block_id_neighborhoods],
                offer_start_date__lte=timezone.now(), offer_end_date__gte=timezone.now(), tank_size=2).exclude(
                supplier__supplier_id=householdbid.assigned_supplier_offer.supplier.supplier_id).order_by('full_price',
                                                                                                          'auctions_won',
                                                                                                          '?')
            form.fields['assigned_supplier_offer'].queryset = supplierbids_list.exclude(household_set_number=4)
        else:
            supplierbids_list = SupplierBid.objects.filter(
                neighborhoods_serviced_2__in=[householdbid.household.block_id_neighborhoods.block_id_neighborhoods],
                offer_start_date__lte=timezone.now(), offer_end_date__gte=timezone.now(), tank_size=1).exclude(
                supplier__supplier_id=householdbid.assigned_supplier_offer.supplier.supplier_id).order_by('full_price',
                                                                                                          'auctions_won',
                                                                                                          '?')
            form.fields['assigned_supplier_offer'].queryset = supplierbids_list.exclude(household_set_number=4)

        if not householdbid.household.household_is_survey and not householdbid.household.household_category in [1,3,4]:
            #Handling the large tank restriction for non-survey households
            if householdbid.bid_exception_1:
                supplierbids_list = SupplierBid.objects.filter(
                    neighborhoods_serviced_2__in=[householdbid.household.block_id_neighborhoods.block_id_neighborhoods],
                    offer_start_date__lte=timezone.now(), offer_end_date__gte=timezone.now(),
                    full_price__lte=householdbid.bid_win_pay, tank_size=2).exclude(
                    supplier__supplier_id=householdbid.assigned_supplier_offer.supplier.supplier_id,
                    household_set_number=4).order_by('full_price', 'auctions_won', '?')
                form.fields['assigned_supplier_offer'].queryset = supplierbids_list.exclude(household_set_number=4)
            else:
                supplierbids_list = SupplierBid.objects.filter(
                    neighborhoods_serviced_2__in=[householdbid.household.block_id_neighborhoods.block_id_neighborhoods],
                    offer_start_date__lte=timezone.now(), offer_end_date__gte=timezone.now(),
                    full_price__lte=householdbid.bid_win_pay, tank_size=1).exclude(
                    supplier__supplier_id=householdbid.assigned_supplier_offer.supplier.supplier_id,
                    household_set_number=4).order_by('full_price', 'auctions_won', '?')
                form.fields['assigned_supplier_offer'].queryset = supplierbids_list.exclude(household_set_number=4)

        # If there are no eligible suppliers, we want to enable the 'None' option
        if list(form.fields['assigned_supplier_offer'].queryset) is not None:
            form.fields['assigned_supplier_offer'].empty_label = None
        if householdbid.household.household_category == 3:
            return render(request, 'callcenterapp/fixprice_hh_changesupplier.html', {'form': form})
        else:
            return render(request, 'callcenterapp/householdbid_changesupplier.html', {'form': form})


@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all().order_by('supplier_id')
    return render(request, 'callcenterapp/supplier_list.html', {'suppliers': suppliers})


@login_required
def supplier_detail(request, supplyid):
    supplier_bid_ids_list = []
    payments_completed_list = []
    payments_due_list = []
    paid_amount_list = []
    due_amount_list = []
    sum_of_paid_amount = 0
    sum_of_due_amount = 0
    supplier = get_object_or_404(Supplier, supplier_id=supplyid)
    supplierbids = SupplierBid.objects.filter(supplier__supplier_id=supplier.supplier_id).order_by('-offer_start_date',
                                                                                                   '-offer_end_date')
    for supp_bid in supplierbids:
        supplier_bid_ids_list.append(supp_bid.id)
    payments_completed_list = Payment.objects.filter(supplierbid__in=supplier_bid_ids_list, payment_completed=True)
    payments_due_list = Payment.objects.filter(supplierbid__in=supplier_bid_ids_list).exclude(payment_completed=True)
    if payments_completed_list:
        for paid_amount in payments_completed_list:
            paid_amount_list.append(paid_amount.amount_due)
    if payments_due_list:
        for due_payment in payments_due_list:
            due_amount_list.append(due_payment.amount_due)
    sum_of_paid_amount = sum(paid_amount_list)
    sum_of_due_amount = sum(due_amount_list)
    return render(request, 'callcenterapp/supplier_detail.html',
                  {'supplier': supplier, 'supplierbids': supplierbids, 'currdate': timezone.now().date(), \
                   'sum_of_paid_amount': sum_of_paid_amount, 'sum_of_due_amount': sum_of_due_amount})


@login_required
def supplierbid_list(request):
    supplierbids = SupplierBid.objects.all().order_by('-offer_start_date', '-offer_end_date')
    return render(request, 'callcenterapp/supplierbid_list.html',
                  {'supplierbids': supplierbids, 'currdate': timezone.now().date()})


@login_required
def supplierbid_detail(request, pk):
    supplierbid = get_object_or_404(SupplierBid, pk=pk)
    return render(request, 'callcenterapp/supplierbid_detail.html',
                  {'supplierbid': supplierbid, 'currdate': timezone.now().date()})


@login_required
@permission_required('callcenterapp.can_add_supplierbid')
def supplierbid_new(request, supplyid):
    if request.method == "POST":

        form = SupplierBidForm(request.POST)

        if form.is_valid():
            supplierbid = form.save(commit=False)
            supplierbid.original_number_payment_advance = supplierbid.number_payment_advance
            supplierbid.supplier = get_object_or_404(Supplier, supplier_id=supplyid)
            supplierbid.save()
            form.save_m2m()
            return redirect('callcenterapp.views.supplierbid_detail', pk=supplierbid.pk)

    else:
        form = SupplierBidForm()

    return render(request, 'callcenterapp/supplierbid_new.html', {'form': form})


@login_required
def payment_list(request):
    payments = Payment.objects.all().order_by('payment_completed', '-date_opened')
    return render(request, 'callcenterapp/payment_list.html', {'payments': payments})


@login_required
@permission_required('callcenterapp.can_change_payment')
def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)

    if request.method == "POST":

        form = PaymentForm(request.POST, instance=payment)

        if form.is_valid():
            payment = form.save(commit=False)
            payment.payment_completed = True
            payment.date_closed = timezone.now()
            payment.save()

            return render(request, 'callcenterapp/payment_detail.html', {'payment': payment})

    else:
        form = PaymentForm(instance=payment)

    return render(request, 'callcenterapp/payment_detail.html', {'payment': payment, 'form': form})


@login_required
def hh_bid_rejected_no_supplier_found(request, current_bid, lower_supplier_bid_id):
    SupplierBid.altenative_supplier_bids.through.objects.all().delete()
    householdbid = get_object_or_404(HouseholdBid, pk=current_bid)
    supplierbid = get_object_or_404(SupplierBid, pk=lower_supplier_bid_id)
    household = get_object_or_404(Household, cleaned_household_id=householdbid.household.cleaned_household_id)
    neighborhood = [household.block_id_neighborhoods.block_id_neighborhoods]
    if supplierbid:
        updated_price = supplierbid.full_price + 1000
        supplier_on_same_price = SupplierBid.objects.filter(neighborhoods_serviced_2__in=neighborhood, \
                                                            offer_start_date__lte=timezone.now(), \
                                                            offer_end_date__gte=timezone.now(), \
                                                            tank_size=household.hh_selected_tank_size, \
                                                            full_price__gte=supplierbid.full_price,
                                                            household_set_number=4). \
            order_by('full_price', 'supplier_rank'). \
            exclude(supplier=supplierbid.supplier).first()
    if household and householdbid and supplier_on_same_price:
        supplier_at_price_bw_update_and_same = None
        price_diff = supplierbid.full_price + 500
        supplier_at_price_bw_update_and_same = SupplierBid.objects.filter(neighborhoods_serviced_2__in=neighborhood, \
                                                                          offer_start_date__lte=timezone.now(), \
                                                                          offer_end_date__gte=timezone.now(), \
                                                                          tank_size=household.hh_selected_tank_size, \
                                                                          household_set_number=4, \
                                                                          full_price__range=(
                                                                              supplierbid.full_price, price_diff)). \
            order_by('full_price', 'supplier_rank'). \
            exclude(supplier=supplierbid.supplier)  # .first()
        if supplier_at_price_bw_update_and_same:
            count_rank = 1
            for all_supplier_on_same_price in supplier_at_price_bw_update_and_same:
                all_supplier_on_same_price.supplier_rank = all_supplier_on_same_price.supplier_rank - 1
                all_supplier_on_same_price.save(force_update=True)
                count_rank += 1
            supplierbid.supplier_rank = count_rank
        supplierbid.full_price = updated_price
        supplierbid.save()
        household.is_hh_select_tank = False
        household.hh_selected_tank_size = None
        household.price_is_accepted = False
        household.save()
        householdbid.bid_canceled = True
        householdbid.no_supplier_found = True
        householdbid.job_complete = False
        householdbid.save()
    return redirect('callcenterapp.views.householdbid_detail', pk=current_bid)


@login_required
def householdbid_cancelbid(request, pk):
    SupplierBid.altenative_supplier_bids.through.objects.all().delete()
    householdbid = get_object_or_404(HouseholdBid, pk=pk)
    household = get_object_or_404(Household, cleaned_household_id=householdbid.household.cleaned_household_id)
    if request.method == "POST":
        LowActivityDesludger.objects.all().delete()
        form = HouseholdBidCancelBidForm(request.POST, instance=householdbid)

        if form.is_valid():
            household.is_hh_select_tank = False
            household.hh_selected_tank_size = None
            household.price_is_accepted = False
            household.save()
            householdbid = form.save(commit=False)
            householdbid.bid_canceled = True
            householdbid.save()

            if householdbid.assigned_supplier_offer is not None:
                supplier_bid = get_object_or_404(SupplierBid, pk=householdbid.assigned_supplier_offer.pk)
                supplier_bid.auctions_won -= 1
                supplier_bid.save()

            return redirect('callcenterapp.views.householdbid_detail', pk=pk)

    else:
        form = HouseholdBidCancelBidForm(instance=householdbid)
        if householdbid.household.household_category == 4:
            return render(request, 'callcenterapp/competative_householdbid_cancelbid.html', {'form': form})
        elif householdbid.household.household_category == 3:
            return render(request, 'callcenterapp/fixprice_householdbid_cancelbid.html', {'form': form})
        else:
            return render(request, 'callcenterapp/householdbid_cancelbid.html', {'form': form})


@login_required
def household_search(request):
    s_houseid = 0
    s_firstname = '<none>'
    s_lastname = '<none>'
    s_phonenumber = 0
    s_landmark = '<none>'

    if 'houseid' in request.GET and request.GET['houseid']:
        s_houseid = int(request.GET['houseid'])
    if 'firstname' in request.GET and request.GET['firstname']:
        s_firstname = request.GET['firstname']
    if 'lastname' in request.GET and request.GET['lastname']:
        s_lastname = request.GET['lastname']
    if 'phonenumber' in request.GET and request.GET['phonenumber']:
        s_phonenumber = int(request.GET['phonenumber'])
    if 'landmark' in request.GET and request.GET['landmark']:
        s_landmark = request.GET['landmark']

    households = Household.objects.filter(Q(cleaned_household_id=s_houseid) |
                                          Q(household_firstname__icontains=s_firstname) |
                                          Q(household_lastname__icontains=s_lastname) |
                                          Q(household_nickname__icontains=s_firstname) |
                                          Q(household_head_firstname__icontains=s_firstname) |
                                          Q(household_head_lastname__icontains=s_lastname) |
                                          Q(household_phone1=s_phonenumber) |
                                          Q(household_phone2=s_phonenumber) |
                                          Q(household_phone3=s_phonenumber) |
                                          Q(primary_landmark_name__icontains=s_landmark) |
                                          Q(second_landmark_name__icontains=s_landmark) |
                                          Q(third_landmark_name__icontains=s_landmark) |
                                          Q(fourth_landmark_name__icontains=s_landmark) |
                                          Q(fifth_landmark_name__icontains=s_landmark) |
                                          Q(sixth_landmark_name__icontains=s_landmark) |
                                          Q(closest_main_street__icontains=s_landmark) |
                                          Q(household_notes__icontains=s_landmark))

    return render(request, 'callcenterapp/household_search.html', {'households': households})

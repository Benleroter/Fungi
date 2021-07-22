from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Show
from .models import ShowSearchFields
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms

def filtershome(request):
	all_users= get_user_model().objects.all()
	all_show = Show.objects.all()
	context = {
		'shows' : all_show,
		'usersexists' : all_users #not currently rendered
	}
	return render(request, 'usersettings/filtershome.html', context)

class EditFilter(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	testcb = forms.BooleanField()
	model = Show
	fields = [
	'ShowOtherCommonNames','ShowOtherLatinNames',
	'ShowPoresAndTubes',	'ShowGills',	'ShowSpores','ShowFlesh','ShowHabitat','ShowCuisine',	'ShowCap',
	'ShowStipe','ShowSeasons','ShowSimilarFungi','ShowStatus','ShowFungiComments','ShowLatinNames',
	'ShowClassification', 'ShowOnlyUKOccurences','ShowMacromycetes'
	] 
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-EditFilter'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit_survey'
		self.helper.add_input(Submit('submit', 'Submit'))

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		show = self.get_object()
		if self.request.user == show.user:
			return True
		return False

class EditSearchFields(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = ShowSearchFields
	template_name = 'usersettings/searchfields_form.html'  # <app>/<model>_<viewtype>.html
	fields = '__all__' 
	fields = [
	'ExactMatch',
	'CommonName',
	'LatinName',
	'HabitatAssociations',
	'MonthFound',
	'HabitatPh',
	'HabitatGrowingMedium',
	'HabitatSoil',
	'CapColour',
	'CapShape',
	'CapRim',
	'CapTexture',
	'CapBruiseColour',
	'CapCutColour',
	'CapWidth',
	'StipeColour',
	'StipeBruiseColour',
	'StipeCutColour',
	'StipeLength',
	'StipeThickness',
	'StipeShape',
	'StipeReticulationPresent',
	'StipeReticulationColour',
	'StipeBase',
	'StipeTexture',
	'StipeRing',
	'PoresPresent',
	'PoreColour',
	'PoreShape',
	'PoreBruiseColour',
	'TubeColour',
	'TubeShape',
	'TubeBruiseColour',
	'PoreMilk',
	'GillsPresent',
	'GillsColour',
	'GillsBruiseColour',
	'GillsCutColour',
	'GillsAttachment',
	'GillsArrangement',
	'GillsMilk',
	'FleshCapColour',
	'FleshCapBruiseColour',
	'FleshCapCutColour',
	'FleshStipeColour',
	'FleshStipeBruiseColour',
	'FleshStipeCutColour',
	'SporeColour',
	'OtherCommonNames',
	'OtherLatinNames',
	'Kingdom',
	'Phyum',
	'SubPhyum',	
	'Class',
	'SubClass',
	'Order',
	'Family',
	'Genus',	
	'PoisonType',
	'CulinaryRating',
	'Odour',
	'Taste',
	'StatusStatusData',
	'StatusWhereFound'
	]

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		show = self.get_object()
		if self.request.user == show.user:
			return True
		return False
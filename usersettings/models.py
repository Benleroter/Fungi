from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Show(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	ShowAll  = models.BooleanField(default=False ,verbose_name=  ' _'+'show all')
	ShowOtherCommonNames  = models.BooleanField(default=False ,verbose_name=  ' _'+'Common name')
	ShowLatinNames  = models.BooleanField(default=False ,verbose_name=  ' _'+'Latin name')
	ShowOtherLatinNames  = models.BooleanField(default=False ,verbose_name=  ' _'+'Other Latin names')
	ShowClassification  = models.BooleanField(default=False ,verbose_name=  ' _'+'Classification')
	ShowPoresAndTubes  = models.BooleanField(default=False ,verbose_name=  ' _'+'Pores & Tubes')
	ShowGills  = models.BooleanField(default=False ,verbose_name=  ' _'+'Gills')
	ShowSpores  = models.BooleanField(default=False ,verbose_name=  ' _'+'Spores')
	ShowFlesh  = models.BooleanField(default=False ,verbose_name=  ' _'+'Flesh')
	ShowHabitat  = models.BooleanField(default=False ,verbose_name=  ' _'+'Habitat')
	ShowCuisine  = models.BooleanField(default=False ,verbose_name=  ' _'+'Cuisine')
	ShowCap  = models.BooleanField(default=False ,verbose_name=  ' _'+'Cap')
	ShowStipe  = models.BooleanField(default=False ,verbose_name=  ' _'+'Stipe/Stem')
	ShowSeasons  = models.BooleanField(default=False ,verbose_name=  ' _'+'Seasons')
	ShowSimilarFungi  = models.BooleanField(default=False ,verbose_name=  ' _'+'Similar Fungi')
	ShowStatus  = models.BooleanField(default=False ,verbose_name=  ' _'+'Status')
	ShowFungiComments  = models.BooleanField(default=False ,verbose_name=  ' _'+'Comments')
	ShowOnlyUKOccurences = models.BooleanField(default=False ,verbose_name=  ' _'+'UK Species Only')
	ShowMacromycetes =  models.BooleanField(default=False ,verbose_name=  ' _'+'Macromycetes (Large fungi) Only')

	class Meta:
		managed = True
		db_table = 'Show'

	def __str__(self):
		return f'{self.user.username}'+' ID: ' +str(self.user.id)

	def get_absolute_url(self):
		#return  reverse('usersettings:view-show-filters', kwargs={'pk': self.pk})
		#return  reverse('AllFungi-HomePage')AllFungiList
		return  reverse('AllFungiList')

	
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

class ShowSearchFields(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	ExactMatch = models.BooleanField(default=False, verbose_name=  ' _'+'Exact match')
	CommonName = models.BooleanField(default=False, verbose_name= ' _'+'Common name')
	LatinName = models.BooleanField(default=False ,verbose_name=  ' _'+'Latin name')
	HabitatAssociations = models.BooleanField(default=False, verbose_name=  ' _'+'Associated Trees')
	HabitatPh = models.BooleanField(default=False, verbose_name=  ' _'+'Ph')
	HabitatGrowingMedium = models.BooleanField(default=False, verbose_name=  ' _'+'Growing Medium')
	HabitatSoil = models.BooleanField(default=False, verbose_name=  ' _'+'Soil')
	MonthFound = models.BooleanField(default=False, verbose_name=  ' _'+'Month found')
	CapColour = models.BooleanField(default=False, verbose_name=  ' _'+'Colour')
	CapShape = models.BooleanField(default=False, verbose_name=  ' _'+'Shape')
	CapRim= models.BooleanField(default=False, verbose_name=  ' _'+'Rim')
	CapTexture = models.BooleanField(default=False, verbose_name=  ' _'+'Texture')
	CapBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Bruise colour')
	CapCutColour = models.BooleanField(default=False, verbose_name=  ' _'+'Cut colour')
	CapWidth = models.BooleanField(default=False, verbose_name=  ' _'+'width')
	StipeColour = models.BooleanField(default=False, verbose_name=  ' _'+'Colour')
	StipeBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Bruise colour')
	StipeCutColour = models.BooleanField(default=False, verbose_name=  ' _'+'Cut colour')
	StipeLength = models.BooleanField(default=False, verbose_name=  ' _'+'length')
	StipeThickness = models.BooleanField(default=False, verbose_name=  ' _'+'thickness')
	StipeShape = models.BooleanField(default=False, verbose_name=  ' _'+'Shape')
	StipeReticulationPresent = models.BooleanField(default=False, verbose_name=  ' _'+'Reticulation')
	StipeReticulationColour = models.BooleanField(default=False, verbose_name=  ' _'+'Reticulation colour')
	StipeBase = models.BooleanField(default=False, verbose_name=  ' _'+'Base')
	StipeTexture = models.BooleanField(default=False, verbose_name=  ' _'+'Texture')
	StipeRing = models.BooleanField(default=False, verbose_name=  ' _'+'Ring')
	PoresPresent = models.BooleanField(default=False, verbose_name=  ' _'+'Pores Present')
	PoreColour = models.BooleanField(default=False, verbose_name=  ' _'+'Pore Colour')
	PoreShape = models.BooleanField(default=False, verbose_name=  ' _'+'PoreShape')
	PoreBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Pore Bruise colour')
	TubeColour = models.BooleanField(default=False, verbose_name=  ' _'+'Tube Colour')
	TubeShape = models.BooleanField(default=False, verbose_name=  ' _'+'Tube Shape')
	TubeBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Tube Bruise colour')
	PoreMilk = models.BooleanField(default=False, verbose_name=  ' _'+'Milk')
	GillsPresent = models.BooleanField(default=False, verbose_name=  ' _'+'Present')
	GillsColour = models.BooleanField(default=False, verbose_name=  ' _'+'Colour')
	GillsBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Bruise colour')
	GillsCutColour = models.BooleanField(default=False, verbose_name=  ' _'+'Cut colour')
	GillsAttachment = models.BooleanField(default=False, verbose_name=  ' _'+'Attachment')
	GillsArrangement = models.BooleanField(default=False, verbose_name=  ' _'+'Arrangement')
	GillsMilk = models.BooleanField(default=False, verbose_name=  ' _'+'Milk')
	FleshCapColour = models.BooleanField(default=False, verbose_name=  ' _'+'Flesh colour')
	FleshCapBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Flesh bruise colour')
	FleshCapCutColour = models.BooleanField(default=False, verbose_name=  ' _'+'Flesh cut colour')
	FleshStipeColour = models.BooleanField(default=False, verbose_name=  ' _'+'Fesh colour')
	FleshStipeBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Flesh bruise colour')
	FleshStipeCutColour = models.BooleanField(default=False, verbose_name=  ' _'+'Flesh cut colour')
	SporeColour = models.BooleanField(default=False, verbose_name=  ' _'+'Colour')
	OtherCommonNames = models.BooleanField(default=False, verbose_name=  ' _'+'alt. common names')
	OtherLatinNames = models.BooleanField(default=False, verbose_name=  ' _'+'alt. latin names')
	Kingdom = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. Kingdom')	
	Phyum = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. Phyum')
	SubPhyum = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. SubPhyum')
	Class = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. Class')
	SubClass = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. SubClass')
	Order = models.BooleanField(default=False, verbose_name=  ' _'+'Tax, Order')
	Family = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. Family')
	Genus = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. Genus')
	PoisonType = models.BooleanField(default=False, verbose_name=  ' _'+'Poision type')
	CulinaryRating = models.BooleanField(default=False, verbose_name=  ' _'+'Culinary rating')
	Odour = models.BooleanField(default=False, verbose_name=  ' _'+'Odour')
	Taste = models.BooleanField(default=False, verbose_name=  ' _'+'Taste')
	StatusStatusData = models.BooleanField(default=False, verbose_name=  ' _ '+'Status')
	StatusWhereFound = models.BooleanField(default=False, verbose_name=  ' _'+'Where found (geographically')
	#StatusUKOccurences = models.BooleanField(default=False, verbose_name=  ' _'+'UK Occurences')
	StatusRecordedInUK= models.BooleanField(default=False, verbose_name=  ' _'+'In UK')

	class Meta:
		managed = True
		db_table = 'ShowSearchFields'
		verbose_name = 'ShowSearchFields'
		verbose_name_plural = 'ShowSearchFields'

	def __str__(self):
		return f'{self.user.username}'+' ID: ' +str(self.user.id)		


	def get_absolute_url(self):
		#return  reverse('usersettings:edit-search-fields', kwargs={'pk': self.pk})
		return  reverse('search-fungi')


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
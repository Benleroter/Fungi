from django.db import models
from django.db import models
from django.contrib.auth.models import User
#Import PIL
#from PIL import _imaging
#rom PIL.Image import core as imaging
#from io import BytesIO
from PIL.Image import Image
#from PIL import _imaging
#from PIL.Image import core as _imaging
#from PIL.Image import core as _imaging
#from PIL import _imaging
from django.urls import reverse


class Fungi(models.Model):
	CommonName = models.CharField(max_length=255, blank=True, null=True)
	LatinName = models.CharField(max_length=255, blank=False, null=False)
	GenusEnglish =  models.CharField(max_length=255,blank=True,null=True, default='NoData')
	GenusLatin =  models.CharField(max_length=255,blank=True,null=True, default='NoData')
	UKSpecies = models.CharField(max_length=8,blank=True,null=True, default='NoData')
	Macromycetes = models.CharField(max_length=8,blank=True,null=True, default='NoData')

	class Meta:
		managed = True
		db_table = 'Fungi'
		verbose_name = "Fungi"
		verbose_name_plural = "Fungi"
		ordering = ['CommonName']

	def __str__(self):
		#return ID:"+str(self.id)+self.CommonName+", "+self.LatinName+" ID:"+str(self.id)+', recoded in UK:'+self.UKSpecies
		return 'ID:'+str(self.id)+', '+self.CommonName+", "+self.LatinName+', ID:'+str(self.id)
		#return self.CommonName+", "+self.LatinName+self.ID:"+str(self.id)

	def get_absolute_url(self):
		return  reverse('FungiDetail-Page', kwargs={'pk': self.pk})

	#Following function creates all child records with default data
	def save(self, *args, **kwargs):
		is_new = not self.pk
		super().save(*args, **kwargs)
		if is_new:
			OtherCommonNames.objects.create(Fungi=self)
			OtherLatinNames.objects.create(Fungi=self)
			Cap.objects.create(Fungi=self)
			Stipe.objects.create(Fungi=self)
			PoresAndTubes.objects.create(Fungi=self)
			Gills.objects.create(Fungi=self)
			Spores.objects.create(Fungi=self)
			Picture.objects.create(Fungi=self)
			Habitat.objects.create(Fungi=self)
			Cuisine.objects.create(Fungi=self)
			Flesh.objects.create(Fungi=self)
			Classification.objects.create(Fungi=self)
			Seasons.objects.create(Fungi=self)
			NetLinks.objects.create(Fungi=self)
			SimilarFungi.objects.create(Fungi=self)
			Status.objects.create(Fungi=self)
			FungiComments.objects.create(Fungi=self)

def FungiChoices():
	FCL =[]
	FChoices = Fungi.objects.all().distinct()
	Data = ('NoData', 'NoData')
	FCL.append(Data)
	for i in FChoices:
		data = (i.CommonName, i.CommonName)
		FCL.append(data)
	return FCL

def FungiChoices2():
	FCL2 =[]
	FChoices = Fungi.objects.all().distinct()
	for i in FChoices:
		data = (i.id, i.CommonName+', '+str(i.id))
		FCL2.append(data)
	return FCL2

class SimilarFungi(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_similar')
	SimilarFungiName = models.CharField(max_length=255,blank=True, default='NoData',null=True,  choices=FungiChoices())
	SimilarFungiID = models.IntegerField(blank=True, null=True, default=0, choices=FungiChoices2())
	SimilarFungiComments = models.CharField(max_length=255,blank=True,null=True, default='NoData')	#
	
	class Meta:
		managed = True
		db_table = 'SimilarFungi'
		ordering = ['Fungi']

	def __str__(self):
		return self.Fungi.CommonName+', '+self.SimilarFungiName

class Variants(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_variants')
	VariantCommonName = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	VariantLatinName = models.CharField(max_length=255,blank=True,null=True, default='NoData')

	class Meta:
		managed = True
		db_table = 'Variants'
		ordering = ['Fungi']

	def __str__(self):
		return self.Fungi.CommonName+', '+self.SimilarFungiName+',  '+self.VariantLatinName

class FungiComments(models.Model):
	Fungi = models.OneToOneField(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_comments')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')

	class Meta:
		managed = True
		db_table = 'FungiComments'
		ordering = ['Fungi']

	def __str__(self):
		return self.Fungi.CommonName+', Comments: '+self.Comments

class Seasons(models.Model):
	Fungi = models.OneToOneField(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_seasons')
	Season = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')

	class Meta:
		managed = True
		db_table = 'Seasons'
		verbose_name = 'Seasons'
		verbose_name_plural = 'Seasons'
		ordering = ['Fungi']

	def __str__(self):
		return self.Fungi.CommonName+", "+self.Season

	def get_absolute_url(self):
		return  reverse('FungiDetail-Page', kwargs={'pk': self.pk})

class Habitat(models.Model):
	Fungi = models.OneToOneField(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_habitat')
	Associations = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Ph = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Soil = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	GrowingMedium = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')

	class Meta:
		managed = True
		db_table = 'Habitat'
		verbose_name = "Habitat"
		verbose_name_plural = "Habitats"
		ordering = ['Fungi']
		
	def __str__(self):
		#return self.Fungi.CommonName+", id: "+str(self.Fungi.id)+", "+self.Associations+", "+self.Ph+", "+self.Soil+", id:"+str(self.id)
		#return "Fungi_ID:"+str(self.Fungi.id)+", "+self.Fungi.CommonName+", "+self.Associations+", id:"+str(self.id)
		return "Fungi_ID:"+str(self.Fungi.id)+", "+self.Fungi.CommonName+", "+self.Associations


class Cap(models.Model):
	Fungi = models.OneToOneField(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_cap')
	DataPresent = models.BooleanField(default=False)
	Colour = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	ColourDescription = models.CharField(max_length=1028, blank=True, default='NoData', null=True)
	ShapeDescription = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	Rim = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	RimDescription = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	CapTexture= models.CharField(max_length=255, blank=True, default='NoData', null=True)
	CapTextureDescription = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	BruiseColour = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	CutColour = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	WidthMin = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0.00, null=True)
	WidthMax = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0.00, null=True)
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')
	
	class Meta:
		managed = True
		db_table = 'Cap'
		verbose_name = "Cap"
		verbose_name_plural = "Caps"
		ordering = ['Fungi']

	def __str__(self):
		return str(self.Fungi)+', WidthMin:'+str(self.WidthMin)+', WidthMax:'+str(self.WidthMax)+', colour: '+self.Colour+', id:'+str(self.Fungi.id)+', DS:'+str(self.DataPresent)

	def get_absolute_url(self):
		return  reverse('FungiDetail-Page', kwargs={'pk': self.pk})		
		
'''	def save(self, *args, **kwargs):
		super(Cap,self).save(*args, **kwargs)'''


class Stipe(models.Model):
	Fungi = models.OneToOneField(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_Stipe')
	Colour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	BruiseColour = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	CutColour = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	LengthMin = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0.00, null=True)
	LengthMax = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0.00, null=True)#
	ThicknessMin = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0.00, null=True)
	ThicknessMax = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0.00, null=True)
	ShapeDescription = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	ReticulationPresent = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	ReticulationColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	ReticulationDescription = models.CharField(max_length=2048, blank=True, null=True, default='NoData')	
	Base = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	BaseDescription = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	Texture = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	TextureDescription= models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Ring = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	RingDescription = models.CharField(max_length=255,blank=True,null=True, default='NoData')

	Volva = models.CharField(max_length=255, blank=True, default='NoData', null=True)



	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')

	class Meta:
		managed = True
		db_table = 'Stipe'
		verbose_name = "Stipe"
		verbose_name_plural = "Stipes"
		ordering = ['Fungi']

	def __str__(self):
		return str(self.Fungi)+', LM:'+str(self.LengthMax)

class PoresAndTubes(models.Model):
	Fungi = models.OneToOneField(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_pores')
	PoresPresent = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	PoreColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	PoreShape = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	PoreBruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	TubeColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	TubeShape = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	TubeBruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Milk = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')

	class Meta:
		managed = True
		db_table = 'PoresAndTubes'
		verbose_name = "Pores and Tubes"
		verbose_name_plural = "Pores and Tubes"
		ordering = ['Fungi']

	def __str__(self):
		return self.Fungi.CommonName     

class Gills(models.Model):
	Fungi = models.OneToOneField(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_gills')
	GillsPresent = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Colour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	BruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	CutColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Attachment = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Arrangement = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Milk = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')

	class Meta:
		managed = True
		db_table = 'Gills'
		verbose_name = "Gills"
		verbose_name_plural = "Gills"
		ordering = ['Fungi']

	def __str__(self):
		return self.Fungi.CommonName+", Colour: "+self.Colour   

class Flesh(models.Model):
	Fungi = models.OneToOneField(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_flesh')
	FleshCapColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	FleshCapBruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	FleshCapCutColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	FleshStipeColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	FleshStipeBruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	FleshStipeCutColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')
	class Meta:
		managed = True
		db_table = 'Flesh'
		verbose_name = 'Flesh'
		verbose_name_plural = 'Flesh'
		ordering = ['Fungi']

	def __str__(self):
		return self.Fungi.CommonName

class Spores(models.Model):
	Fungi = models.OneToOneField(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_spores')
	Colour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')

	class Meta:
		managed = True
		db_table = 'Spores'
		verbose_name = "Spores"
		verbose_name_plural = "Spores"
		ordering = ['Fungi']

	def __str__(self):
		return self.Fungi.CommonName+", spore print colour: "+self.Colour   


class NetLinks(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_netlinks')
	Website = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Websiteurl = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	OrderToDisplay = models.IntegerField(blank=True, null=True, default=50)

	class Meta:
		managed = True
		db_table = 'NetLinks'
		verbose_name = "NetLinks"
		verbose_name_plural = "NetLinks"
		ordering = ['Fungi']

	def __str__(self):
		return self.Fungi.CommonName+', '+self.Fungi.LatinName+', '+self.Website

class OtherCommonNames(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_commonname')
    AltCommonName = models.CharField(max_length=255, blank=True, null=True, default='NoData')

    class Meta:
        managed = True
        db_table =  'OtherCommonNames'
        verbose_name = "Other Common Name"
        verbose_name_plural = "Other Common Names"	
        ordering = ['Fungi']

    def __str__(self):
    	return self.Fungi.CommonName+', '+self.AltCommonName  

class OtherLatinNames(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_latinnname')
    AltLatinName = models.CharField(max_length=255, blank=True, null=True, default='NoData')

    class Meta:
        managed = True
        db_table = 'OtherLatinNames'
        verbose_name = "Other Latin Name"
        verbose_name_plural = "Other Latin Names"
        ordering = ['Fungi']

    def __str__(self):
        return self.Fungi.CommonName+', '+self.AltLatinName 

class Classification(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_taxonomy')
	Kingdom = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	Phyum = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	SubPhyum = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	Class = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	SubClass = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	Order = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	Family = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	Genus = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	Source = models.CharField(max_length=255, blank=False, null=False, default='NoData')

	class Meta:
		managed = True
		db_table = 'Classification'
		verbose_name = "Classification"
		verbose_name_plural = "Classification"
		ordering = ['Fungi']

	def __str__(self):
		return self.Fungi.LatinName+", "+self.Fungi.CommonName+", "+self.Phyum+", "+self.Class+", "+self.Order+", "+self.Family+", "+self.Genus

class Cuisine(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_cuisine')
	PoisonType = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	CulinaryRating = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Odour = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Taste = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')

	class Meta:
		managed = True
		db_table = 'Cuisine'
		verbose_name = 'Cuisine'
		verbose_name_plural = 'Cuisine'
		ordering =['Fungi']

	def __str__(self):
		return self.Fungi.CommonName+", "+"Culinary rating: "+self.CulinaryRating

class Picture(models.Model):
	Fungi = models.OneToOneField(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_picture')
	image = models.ImageField(default='default.jpg', upload_to='images')
	
	class Meta:
		managed = True
		db_table = 'Pictures'
		verbose_name = "Picture"
		verbose_name_plural = "Pictures"

	def __str__(self):
		return self.Fungi.CommonName

	def save(self, *args, **kwargs):
		super(Picture, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		#if img.height > 20 or img.width > 20:
		output_size = (350, 350)
		img.thumbnail(output_size)
		img.save(self.image.path)

class Status(models.Model):
	Fungi = models.OneToOneField(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_Status')
	StatusData = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	WhereFound = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	RecordedInUK = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	UKOccurences = models.CharField(max_length=16, blank=True, null=True, default='0') 
	StatusComments = models.CharField(max_length=2048, blank=True, null=True, default='no comments') 

	class Meta:
		managed = True
		db_table = 'Status'
		verbose_name = 'Status'
		verbose_name_plural = 'Status'
		ordering =['Fungi']

	def __str__(self):
		return self.Fungi.CommonName+', status: '+self.StatusData+', mainly found in: '+self.WhereFound+', recorded in UK: '+self.RecordedInUK+' UKO:'+self.UKOccurences

	def get_absolute_url(self):
		return  reverse('FungiDetail-Page', kwargs={'pk': self.Fungi.pk})
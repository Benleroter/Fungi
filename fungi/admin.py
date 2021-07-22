from django.contrib import admin

from fungi.models import (
	Fungi,
	OtherCommonNames,
	OtherLatinNames,
	FungiComments,
	Cap,
	Stipe,
	PoresAndTubes,
	Gills,
	Spores,
	Picture,
	Habitat,
	Cuisine,
	Flesh,
	Classification,
	Seasons,
	NetLinks,
	SimilarFungi,
	Status,
	Variants,
)

admin.site.register(Fungi)
admin.site.register(OtherCommonNames)
admin.site.register(OtherLatinNames)
admin.site.register(Cap)
admin.site.register(Stipe)
admin.site.register(PoresAndTubes)
admin.site.register(Gills)
admin.site.register(Spores)
admin.site.register(Picture)
admin.site.register(Habitat)
admin.site.register(Flesh)
admin.site.register(Classification)
admin.site.register(Cuisine)
admin.site.register(Seasons)
admin.site.register(NetLinks)
admin.site.register(SimilarFungi)
admin.site.register(FungiComments)
admin.site.register(Status)
admin.site.register(Variants)
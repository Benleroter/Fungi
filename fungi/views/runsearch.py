from fungi.models import Fungi
from fungi.models import *
from django.db.models import Q  
from django.apps import apps
from itertools import chain
import collections

def RunSearch(QParams):
	FoundList = []
	QueryComponents = {}
	QCList= []
	ResultsList = []
	SearchModels =[]
	SearchTermsCount = 0
	Matches = []

	for p in QParams:
		SearchTermsCount += 1

	for i in QParams:
		if i == 'CommonName':
			CommonNameDict ={}
			CommonNameDict['SearchTerm'] = QParams[i]
			CommonNameDict['table'] = 'Fungi'
			CommonNameDict['column'] = 'CommonName'
			CommonNameDict['qstr'] = '__icontains'
			CommonNameDict['model'] = apps.get_model(app_label='fungi', model_name='Fungi')
			QCList.append(CommonNameDict)
			name_list = CommonNameDict['model'].objects.filter(Q(**{CommonNameDict['column']+CommonNameDict['qstr'] :CommonNameDict['SearchTerm']}))
			for i in name_list:
				ResultsList.append(i.id)	

		elif i =="LatinName":
			LatinNameDict = {}
			LatinNameDict['SearchTerm'] = QParams[i]
			LatinNameDict['table'] = 'Fungi'
			LatinNameDict['column'] = 'LatinName'
			LatinNameDict['qstr'] = '__icontains'
			LatinNameDict['model'] = apps.get_model(app_label='fungi', model_name='Fungi')
			LatinName_list = LatinNameDict['model'].objects.filter(Q(**{LatinNameDict['column']+LatinNameDict['qstr'] :LatinNameDict['SearchTerm']}))
			for i in LatinName_list:
				ResultsList.append(i.id)			

		elif i =="HabitatAssociations":
			HabitatAssociationsDict = {}
			HabitatAssociationsDict['SearchTerm'] = QParams[i]
			HabitatAssociationsDict['table'] = 'Habitat'
			HabitatAssociationsDict['column'] = 'Associations'
			HabitatAssociationsDict['qstr'] = '__icontains'
			HabitatAssociationsDict['model'] = apps.get_model(app_label='fungi', model_name='Habitat')

			QCList.append(HabitatAssociationsDict)
			tree_list = HabitatAssociationsDict['model'].objects.filter(Q(**{HabitatAssociationsDict['column']+HabitatAssociationsDict['qstr'] :HabitatAssociationsDict['SearchTerm']}))
			for i in tree_list:
				ResultsList.append(i.Fungi_id)

		elif i =="HabitatPh":
			HabitatPhDict = {}
			HabitatPhDict['SearchTerm'] = QParams[i]
			HabitatPhDict['table'] = 'Habitat'
			HabitatPhDict['column'] = 'Ph'
			HabitatPhDict['qstr'] = '__icontains'
			HabitatPhDict['model'] = apps.get_model(app_label='fungi', model_name='Habitat')
			HabitatPh_list = HabitatPhDict['model'].objects.filter(Q(**{HabitatPhDict['column']+HabitatPhDict['qstr'] :HabitatPhDict['SearchTerm']}))
			for i in HabitatPh_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="HabitatSoil":
			HabitatSoilDict = {}
			HabitatSoilDict['SearchTerm'] = QParams[i]
			HabitatSoilDict['table'] = 'Habitat'
			HabitatSoilDict['column'] = 'Soil'
			HabitatSoilDict['qstr'] = '__icontains'
			HabitatSoilDict['model'] = apps.get_model(app_label='fungi', model_name='Habitat')
			HabitatSoil_list = HabitatSoilDict['model'].objects.filter(Q(**{HabitatSoilDict['column']+HabitatSoilDict['qstr'] :HabitatSoilDict['SearchTerm']}))
			for i in HabitatSoil_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="HabitatGrowingMedium":
			HabitatGrowingMediumDict = {}
			HabitatGrowingMediumDict['SearchTerm'] = QParams[i]
			HabitatGrowingMediumDict['table'] = 'Habitat'
			HabitatGrowingMediumDict['column'] = 'GrowingMedium'
			HabitatGrowingMediumDict['qstr'] = '__icontains'
			HabitatGrowingMediumDict['model'] = apps.get_model(app_label='fungi', model_name='Habitat')
			HabitatGrowingMedium_list = HabitatGrowingMediumDict['model'].objects.filter(Q(**{HabitatGrowingMediumDict['column']+HabitatGrowingMediumDict['qstr'] :HabitatGrowingMediumDict['SearchTerm']}))
			for i in HabitatGrowingMedium_list:
				ResultsList.append(i.Fungi_id)	


		elif i =="Season":
			SeasonDict = {}
			SeasonDict['SearchTerm'] = QParams[i]
			SeasonDict['table'] = 'Seasons'
			SeasonDict['column'] = 'Season'
			SeasonDict['qstr'] = '__icontains'
			SeasonDict['model'] = apps.get_model(app_label='fungi', model_name='Seasons')

			QCList.append(SeasonDict)
			Season_list = SeasonDict['model'].objects.filter(Q(**{SeasonDict['column']+SeasonDict['qstr'] :SeasonDict['SearchTerm']}))
			for i in Season_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="CapColour":
			CapColourDict = {}
			CapColourDict['SearchTerm'] = QParams[i]
			CapColourDict['table'] = 'Cap'
			CapColourDict['column'] = 'Colour'
			CapColourDict['qstr'] = '__icontains'
			CapColourDict['model'] = apps.get_model(app_label='fungi', model_name='Cap')
			CapColour_list = CapColourDict['model'].objects.filter(Q(**{CapColourDict['column']+CapColourDict['qstr'] :CapColourDict['SearchTerm']}))
			for i in CapColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="CapShape":
			CapShapeDict = {}
			CapShapeDict['SearchTerm'] = QParams[i]
			CapShapeDict['table'] = 'Cap'
			CapShapeDict['column'] = 'ShapeDescription'
			CapShapeDict['qstr'] = '__icontains'
			CapShapeDict['model'] = apps.get_model(app_label='fungi', model_name=CapShapeDict['table'])
			CapShape_list = CapShapeDict['model'].objects.filter(Q(**{CapShapeDict['column']+CapShapeDict['qstr'] :CapShapeDict['SearchTerm']}))
			for i in CapShape_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="CapRim":
			CapRimDict = {}
			CapRimDict['SearchTerm'] = QParams[i]
			CapRimDict['table'] = 'Cap'
			CapRimDict['column'] = 'Rim'
			CapRimDict['qstr'] = '__icontains'
			CapRimDict['model'] = apps.get_model(app_label='fungi', model_name=CapRimDict['table'])
			CapRim_list = CapRimDict['model'].objects.filter(Q(**{CapRimDict['column']+CapRimDict['qstr'] :CapRimDict['SearchTerm']}))
			for i in CapRim_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="CapTexture":
			CapTextureDict = {}
			CapTextureDict['SearchTerm'] = QParams[i]
			CapTextureDict['table'] = 'Cap'
			CapTextureDict['column'] = 'CapTexture'
			CapTextureDict['qstr'] = '__icontains'
			CapTextureDict['model'] = apps.get_model(app_label='fungi', model_name=CapTextureDict['table'])
			CapTexture_list = CapTextureDict['model'].objects.filter(Q(**{CapTextureDict['column']+CapTextureDict['qstr'] :CapTextureDict['SearchTerm']}))
			for i in CapTexture_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="CapBruiseColour":
			CapBruiseColourDict = {}
			CapBruiseColourDict['SearchTerm'] = QParams[i]
			CapBruiseColourDict['table'] = 'Cap'
			CapBruiseColourDict['column'] = 'BruiseColour'
			CapBruiseColourDict['qstr'] = '__icontains'
			CapBruiseColourDict['model'] = apps.get_model(app_label='fungi', model_name=CapBruiseColourDict['table'])

			QCList.append(CapBruiseColourDict)
			CapBruiseColour_list = CapBruiseColourDict['model'].objects.filter(Q(**{CapBruiseColourDict['column']+CapBruiseColourDict['qstr'] :CapBruiseColourDict['SearchTerm']}))
			for i in CapBruiseColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="CapCutColour":
			StipeColourDict = {}
			StipeColourDict['SearchTerm'] = QParams[i]
			StipeColourDict['table'] = 'Cap'
			StipeColourDict['column'] = 'CutColour'
			StipeColourDict['qstr'] = '__icontains'
			StipeColourDict['model'] = apps.get_model(app_label='fungi', model_name=StipeColourDict['table'])

			QCList.append(StipeColourDict)
			StipeColour_list = StipeColourDict['model'].objects.filter(Q(**{StipeColourDict['column']+StipeColourDict['qstr'] :StipeColourDict['SearchTerm']}))
			for i in StipeColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="CapWidth":
			CapWidthDict = {}
			CapWidthDict['SearchTerm'] = QParams[i]
			CapWidthDict['table'] = 'Cap'
			CapWidthDict['column1'] = 'WidthMin'
			CapWidthDict['column2'] = 'WidthMax'
			CapWidthDict['qstr1'] = '__lte'
			CapWidthDict['qstr2'] = '__gte'
			CapWidthDict['model'] = apps.get_model(app_label='fungi', model_name=CapWidthDict['table'])
			CapWidth_list = CapWidthDict['model'].objects.filter(Q(**{CapWidthDict['column1']+CapWidthDict['qstr1'] :CapWidthDict['SearchTerm']}) &  Q(**{CapWidthDict['column2']+CapWidthDict['qstr2'] :CapWidthDict['SearchTerm']}))
			for i in CapWidth_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="StipeColour":
			StipeColourDict = {}
			StipeColourDict['SearchTerm'] = QParams[i]
			StipeColourDict['table'] = 'Stipe'
			StipeColourDict['column'] = 'Colour'
			StipeColourDict['qstr'] = '__icontains'
			StipeColourDict['model'] = apps.get_model(app_label='fungi', model_name=StipeColourDict['table'])

			QCList.append(StipeColourDict)
			StipeColourDict_list = StipeColourDict['model'].objects.filter(Q(**{StipeColourDict['column']+StipeColourDict['qstr'] :StipeColourDict['SearchTerm']}))
			for i in StipeColourDict_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="StipeBruiseColour":
			StipeBruiseColourDict = {}
			StipeBruiseColourDict['SearchTerm'] = QParams[i]
			StipeBruiseColourDict['table'] = 'Stipe'
			StipeBruiseColourDict['column'] = 'BruiseColour'
			StipeBruiseColourDict['qstr'] = '__icontains'
			StipeBruiseColourDict['model'] = apps.get_model(app_label='fungi', model_name=StipeBruiseColourDict['table'])

			QCList.append(StipeBruiseColourDict)
			StipeBruiseColour_list = StipeBruiseColourDict['model'].objects.filter(Q(**{StipeBruiseColourDict['column']+StipeBruiseColourDict['qstr'] :StipeBruiseColourDict['SearchTerm']}))
			for i in StipeBruiseColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="StipeCutColour":
			StipeCutColourDict = {}
			StipeCutColourDict['SearchTerm'] = QParams[i]
			StipeCutColourDict['table'] = 'Stipe'
			StipeCutColourDict['column'] = 'CutColour'
			StipeCutColourDict['qstr'] = '__icontains'
			StipeCutColourDict['model'] = apps.get_model(app_label='fungi', model_name=StipeCutColourDict['table'])

			QCList.append(StipeCutColourDict)
			StipeCutColour_list = StipeCutColourDict['model'].objects.filter(Q(**{StipeCutColourDict['column']+StipeCutColourDict['qstr'] :StipeCutColourDict['SearchTerm']}))
			for i in StipeCutColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="StipeLength":
			StipeLengthDict = {}
			StipeLengthDict['SearchTerm'] = QParams[i]
			StipeLengthDict['table'] = 'Stipe'
			StipeLengthDict['column1'] = 'LengthMin'
			StipeLengthDict['column2'] = 'LengthMax'
			StipeLengthDict['qstr1'] = '__lte'
			StipeLengthDict['qstr2'] = '__gte'
			StipeLengthDict['model'] = apps.get_model(app_label='fungi', model_name=StipeLengthDict['table'])
			QCList.append(StipeLengthDict)
			StipeLength_list = StipeLengthDict['model'].objects.filter(Q(**{StipeLengthDict['column1']+StipeLengthDict['qstr1'] :StipeLengthDict['SearchTerm']}) &  Q(**{StipeLengthDict['column2']+StipeLengthDict['qstr2'] :StipeLengthDict['SearchTerm']}))
			for i in StipeLength_list:
				ResultsList.append(i.Fungi_id)			

		elif i =="StipeThickness":
			StipeThicknessDict = {}
			StipeThicknessDict['SearchTerm'] = QParams[i]
			StipeThicknessDict['table'] = 'Stipe'
			StipeThicknessDict['column1'] = 'ThicknessMin'
			StipeThicknessDict['column2'] = 'ThicknessMax'
			StipeThicknessDict['qstr1'] = '__lte'
			StipeThicknessDict['qstr2'] = '__gte'
			StipeThicknessDict['model'] = apps.get_model(app_label='fungi', model_name=StipeThicknessDict['table'])
			QCList.append(StipeThicknessDict)
			StipeThickness_list = StipeThicknessDict['model'].objects.filter(Q(**{StipeThicknessDict['column1']+StipeThicknessDict['qstr1'] :StipeThicknessDict['SearchTerm']}) &  Q(**{StipeThicknessDict['column2']+StipeThicknessDict['qstr2'] :StipeThicknessDict['SearchTerm']}))
			for i in StipeThickness_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="StipeShape":
			StipeDescriptionDict = {}
			StipeDescriptionDict['SearchTerm'] = QParams[i]
			StipeDescriptionDict['table'] = 'Stipe'
			StipeDescriptionDict['column'] = 'ShapeDescription'
			StipeDescriptionDict['qstr'] = '__icontains'
			StipeDescriptionDict['model'] = apps.get_model(app_label='fungi', model_name=StipeDescriptionDict['table'])
			StipeDescription_list = StipeDescriptionDict['model'].objects.filter(Q(**{StipeDescriptionDict['column']+StipeDescriptionDict['qstr'] :StipeDescriptionDict['SearchTerm']}))
			for i in StipeDescription_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="StipeReticulationPresent":
			StipeReticulationPresentDict = {}
			StipeReticulationPresentDict['SearchTerm'] = QParams[i]
			StipeReticulationPresentDict['table'] = 'Stipe'
			StipeReticulationPresentDict['column'] = 'ReticulationPresent'
			StipeReticulationPresentDict['qstr'] = '__icontains'
			StipeReticulationPresentDict['model'] = apps.get_model(app_label='fungi', model_name=StipeReticulationPresentDict['table'])
			StipeReticulationPresent_list = StipeReticulationPresentDict['model'].objects.filter(Q(**{StipeReticulationPresentDict['column']+StipeReticulationPresentDict['qstr'] :StipeReticulationPresentDict['SearchTerm']}))
			for i in StipeReticulationPresent_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="StipeReticulationColour":
			StipeReticulationColourDict = {}
			StipeReticulationColourDict['SearchTerm'] = QParams[i]
			StipeReticulationColourDict['table'] = 'Stipe'
			StipeReticulationColourDict['column'] = 'ReticulationColour'
			StipeReticulationColourDict['qstr'] = '__icontains'
			StipeReticulationColourDict['model'] = apps.get_model(app_label='fungi', model_name=StipeReticulationColourDict['table'])
			StipeReticulationColour_list = StipeReticulationColourDict['model'].objects.filter(Q(**{StipeReticulationColourDict['column']+StipeReticulationColourDict['qstr'] :StipeReticulationColourDict['SearchTerm']}))
			for i in StipeReticulationColour_list:
				ResultsList.append(i.Fungi_id)	


		elif i =="StipeBase":
			StipeBaseDict = {}
			StipeBaseDict['SearchTerm'] = QParams[i]
			StipeBaseDict['table'] = 'Stipe'
			StipeBaseDict['column'] = 'Base'
			StipeBaseDict['qstr'] = '__icontains'
			StipeBaseDict['model'] = apps.get_model(app_label='fungi', model_name=StipeBaseDict['table'])
			StipeBase_list = StipeBaseDict['model'].objects.filter(Q(**{StipeBaseDict['column']+StipeBaseDict['qstr'] :StipeBaseDict['SearchTerm']}))
			for i in StipeBase_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="StipeTexture":
			StipeTextureDict = {}
			StipeTextureDict['SearchTerm'] = QParams[i]
			StipeTextureDict['table'] = 'Stipe'
			StipeTextureDict['column'] = 'Texture'
			StipeTextureDict['qstr'] = '__icontains'
			StipeTextureDict['model'] = apps.get_model(app_label='fungi', model_name=StipeTextureDict['table'])
			StipeTexture_list = StipeTextureDict['model'].objects.filter(Q(**{StipeTextureDict['column']+StipeTextureDict['qstr'] :StipeTextureDict['SearchTerm']}))
			for i in StipeTexture_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="StipeRing":
			StipeRingDict = {}
			StipeRingDict['SearchTerm'] = QParams[i]
			StipeRingDict['table'] = 'Stipe'
			StipeRingDict['column'] = 'Ring'
			StipeRingDict['qstr'] = '__icontains'
			StipeRingDict['model'] = apps.get_model(app_label='fungi', model_name=StipeRingDict['table'])
			StipeTexture_list = StipeRingDict['model'].objects.filter(Q(**{StipeRingDict['column']+StipeRingDict['qstr'] :StipeRingDict['SearchTerm']}))
			for i in StipeRing_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="PoresPresent":
			PoresPresentDict = {}
			PoresPresentDict['SearchTerm'] = QParams[i]
			PoresPresentDict['table'] = 'PoresAndTubes'
			PoresPresentDict['column'] = 'PoresPresent'
			PoresPresentDict['qstr'] = '__iexact'
			PoresPresentDict['model'] = apps.get_model(app_label='fungi', model_name=PoresPresentDict['table'])
			PoresPresent_list = PoresPresentDict['model'].objects.filter(Q(**{PoresPresentDict['column']+PoresPresentDict['qstr'] :PoresPresentDict['SearchTerm']}))
			for i in PoresPresent_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="PoreColour":
			PoresColourDict = {}
			PoresColourDict['SearchTerm'] = QParams[i]
			PoresColourDict['table'] = 'PoresAndTubes'
			PoresColourDict['column'] = 'PoreColour'
			PoresColourDict['qstr'] = '__icontains'
			PoresColourDict['model'] = apps.get_model(app_label='fungi', model_name=PoresColourDict['table'])
			PoresColour_list = PoresColourDict['model'].objects.filter(Q(**{PoresColourDict['column']+PoresColourDict['qstr'] :PoresColourDict['SearchTerm']}))
			for i in PoresColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="PoreShape":
			PoresShapeDict = {}
			PoresShapeDict['SearchTerm'] = QParams[i]
			PoresShapeDict['table'] = 'PoresAndTubes'
			PoresShapeDict['column'] = 'PoreShape'
			PoresShapeDict['qstr'] = '__icontains'
			PoresShapeDict['model'] = apps.get_model(app_label='fungi', model_name=PoresShapeDict['table'])
			PoresShape_list = PoresShapeDict['model'].objects.filter(Q(**{PoresShapeDict['column']+PoresShapeDict['qstr'] :PoresShapeDict['SearchTerm']}))
			for i in PoresShape_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="PoreBruiseColour":
			PoresBruiseColourDict = {}
			PoresBruiseColourDict['SearchTerm'] = QParams[i]
			PoresBruiseColourDict['table'] = 'PoresAndTubes'
			PoresBruiseColourDict['column'] = 'PoreBruiseColour'
			PoresBruiseColourDict['qstr'] = '__icontains'
			PoresBruiseColourDict['model'] = apps.get_model(app_label='fungi', model_name=PoresBruiseColourDict['table'])
			PoresBruiseColour_list = PoresBruiseColourDict['model'].objects.filter(Q(**{PoresBruiseColourDict['column']+PoresBruiseColourDict['qstr'] :PoresBruiseColourDict['SearchTerm']}))
			for i in PoresBruiseColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="TubeColour":
			TubeColourDict = {}
			TubeColourDict['SearchTerm'] = QParams[i]
			TubeColourDict['table'] = 'PoresAndTubes'
			TubeColourDict['column'] = 'TubeColour'
			TubeColourDict['qstr'] = '__icontains'
			TubeColourDict['model'] = apps.get_model(app_label='fungi', model_name=TubeColourDict['table'])
			TubeColour_list = TubeColourDict['model'].objects.filter(Q(**{TubeColourDict['column']+TubeColourDict['qstr'] :TubeColourDict['SearchTerm']}))
			for i in TubeColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="TubeShape":
			TubeShapeDict = {}
			TubeShapeDict['SearchTerm'] = QParams[i]
			TubeShapeDict['table'] = 'PoresAndTubes'
			TubeShapeDict['column'] = 'TubeShape'
			TubeShapeDict['qstr'] = '__icontains'
			TubeShapeDict['model'] = apps.get_model(app_label='fungi', model_name=TubeShapeDict['table'])
			TubeShape_list = TubeShapeDict['model'].objects.filter(Q(**{TubeShapeDict['column']+TubeShapeDict['qstr'] :TubeShapeDict['SearchTerm']}))
			for i in TubeShape_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="TubeBruiseColour":
			TubeShapeDict = {}
			TubeShapeDict['SearchTerm'] = QParams[i]
			TubeShapeDict['table'] = 'PoresAndTubes'
			TubeShapeDict['column'] = 'TubeBruiseColour'
			TubeShapeDict['qstr'] = '__icontains'
			TubeShapeDict['model'] = apps.get_model(app_label='fungi', model_name=TubeShapeDict['table'])
			TubeShape_list = TubeShapeDict['model'].objects.filter(Q(**{TubeShapeDict['column']+TubeShapeDict['qstr'] :TubeShapeDict['SearchTerm']}))
			for i in TubeShape_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="PoreMilk":
			PoreMilkDict = {}
			PoreMilkDict['SearchTerm'] = QParams[i]
			PoreMilkDict['table'] = 'PoresAndTubes'
			PoreMilkDict['column'] = 'Milk'
			PoreMilkDict['qstr'] = '__icontains'
			PoreMilkDict['model'] = apps.get_model(app_label='fungi', model_name=PoreMilkDict['table'])
			PoreMilk_list = PoreMilkDict['model'].objects.filter(Q(**{PoreMilkDict['column']+PoreMilkDict['qstr'] :PoreMilkDict['SearchTerm']}))
			for i in PoreMilk_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="GillsPresent":
			GillsPresentDict = {}
			GillsPresentDict['SearchTerm'] = QParams[i]
			GillsPresentDict['table'] = 'Gills'
			GillsPresentDict['column'] = 'GillsPresent'
			GillsPresentDict['qstr'] = '__iexact'
			GillsPresentDict['model'] = apps.get_model(app_label='fungi', model_name=GillsPresentDict['table'])
			GillsPresent_list = GillsPresentDict['model'].objects.filter(Q(**{GillsPresentDict['column']+GillsPresentDict['qstr'] :GillsPresentDict['SearchTerm']}))
			for i in GillsPresent_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="GillsColour":
			GillsColourDict = {}
			GillsColourDict['SearchTerm'] = QParams[i]
			GillsColourDict['table'] = 'Gills'
			GillsColourDict['column'] = 'Colour'
			GillsColourDict['qstr'] = '__icontains'
			GillsColourDict['model'] = apps.get_model(app_label='fungi', model_name=GillsColourDict['table'])
			GillsColour_list = GillsColourDict['model'].objects.filter(Q(**{GillsColourDict['column']+GillsColourDict['qstr'] :GillsColourDict['SearchTerm']}))
			for i in GillsColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="GillsBruiseColour":
			GillsBruiseColourDict = {}
			GillsBruiseColourDict['SearchTerm'] = QParams[i]
			GillsBruiseColourDict['table'] = 'Gills'
			GillsBruiseColourDict['column'] = 'BruiseColour'
			GillsBruiseColourDict['qstr'] = '__icontains'
			GillsBruiseColourDict['model'] = apps.get_model(app_label='fungi', model_name=GillsBruiseColourDict['table'])
			GillsBruiseColour_list = GillsBruiseColourDict['model'].objects.filter(Q(**{GillsBruiseColourDict['column']+GillsBruiseColourDict['qstr'] :GillsBruiseColourDict['SearchTerm']}))
			for i in GillsBruiseColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="GillsCutColour":
			GillsCutColourDict = {}
			GillsCutColourDict['SearchTerm'] = QParams[i]
			GillsCutColourDict['table'] = 'Gills'
			GillsCutColourDict['column'] = 'CutColour'
			GillsCutColourDict['qstr'] = '__icontains'
			GillsCutColourDict['model'] = apps.get_model(app_label='fungi', model_name=GillsCutColourDict['table'])
			GillsCutColour_list = GillsCutColourDict['model'].objects.filter(Q(**{GillsCutColourDict['column']+GillsCutColourDict['qstr'] :GillsCutColourDict['SearchTerm']}))
			for i in GillsCutColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="GillsAttachment":
			GillsAttachmentDict = {}
			GillsAttachmentDict['SearchTerm'] = QParams[i]
			GillsAttachmentDict['table'] = 'Gills'
			GillsAttachmentDict['column'] = 'Attachment'
			GillsAttachmentDict['qstr'] = '__icontains'
			GillsAttachmentDict['model'] = apps.get_model(app_label='fungi', model_name=GillsAttachmentDict['table'])
			GillsAttachment_list = GillsAttachmentDict['model'].objects.filter(Q(**{GillsAttachmentDict['column']+GillsAttachmentDict['qstr'] :GillsAttachmentDict['SearchTerm']}))
			for i in GillsAttachment_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="GillsArrangement":
			GillsArrangementDict = {}
			GillsArrangementDict['SearchTerm'] = QParams[i]
			GillsArrangementDict['table'] = 'Gills'
			GillsArrangementDict['column'] = 'Arrangement'
			GillsArrangementDict['qstr'] = '__icontains'
			GillsArrangementDict['model'] = apps.get_model(app_label='fungi', model_name=GillsArrangementDict['table'])
			GillsArrangement_list = GillsArrangementDict['model'].objects.filter(Q(**{GillsArrangementDict['column']+GillsArrangementDict['qstr'] :GillsArrangementDict['SearchTerm']}))
			for i in GillsArrangement_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="GillsMilk":
			GillsMilkDict = {}
			GillsMilkDict['SearchTerm'] = QParams[i]
			GillsMilkDict['table'] = 'Gills'
			GillsMilkDict['column'] = 'Milk'
			GillsMilkDict['qstr'] = '__icontains'
			GillsMilkDict['model'] = apps.get_model(app_label='fungi', model_name=GillsMilkDict['table'])
			GillsMilk_list = GillsMilkDict['model'].objects.filter(Q(**{GillsMilkDict['column']+GillsMilkDict['qstr'] :GillsMilkDict['SearchTerm']}))
			for i in GillsMilk_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="FleshCapColour":
			FleshCapColourDict = {}
			FleshCapColourDict['SearchTerm'] = QParams[i]
			FleshCapColourDict['table'] = 'Flesh'
			FleshCapColourDict['column'] = 'FleshCapColour'
			FleshCapColourDict['qstr'] = '__icontains'
			FleshCapColourDict['model'] = apps.get_model(app_label='fungi', model_name=FleshCapColourDict['table'])
			FleshCapColour_list = FleshCapColourDict['model'].objects.filter(Q(**{FleshCapColourDict['column']+FleshCapColourDict['qstr'] :FleshCapColourDict['SearchTerm']}))
			for i in FleshCapColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="FleshCapBruiseColour":
			FleshCapBruiseColourDict = {}
			FleshCapBruiseColourDict['SearchTerm'] = QParams[i]
			FleshCapBruiseColourDict['table'] = 'Flesh'
			FleshCapBruiseColourDict['column'] = 'FleshCapBruiseColour'
			FleshCapBruiseColourDict['qstr'] = '__icontains'
			FleshCapBruiseColourDict['model'] = apps.get_model(app_label='fungi', model_name=FleshCapBruiseColourDict['table'])
			FleshCapBruiseColour_list = FleshCapBruiseColourDict['model'].objects.filter(Q(**{FleshCapBruiseColourDict['column']+FleshCapBruiseColourDict['qstr'] :FleshCapBruiseColourDict['SearchTerm']}))
			for i in FleshCapBruiseColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="FleshCapCutColour":
			FleshCapCutColourDict = {}
			FleshCapCutColourDict['SearchTerm'] = QParams[i]
			FleshCapCutColourDict['table'] = 'Flesh'
			FleshCapCutColourDict['column'] = 'FleshCapCutColour'
			FleshCapCutColourDict['qstr'] = '__icontains'
			FleshCapCutColourDict['model'] = apps.get_model(app_label='fungi', model_name=FleshCapCutColourDict['table'])
			FleshCapCutColour_list = FleshCapCutColourDict['model'].objects.filter(Q(**{FleshCapCutColourDict['column']+FleshCapCutColourDict['qstr'] :FleshCapCutColourDict['SearchTerm']}))
			for i in FleshCapCutColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="FleshStipeColour":
			FleshStipeColourDict = {}
			FleshStipeColourDict['SearchTerm'] = QParams[i]
			FleshStipeColourDict['table'] = 'Flesh'
			FleshStipeColourDict['column'] = 'FleshStipeColour'
			FleshStipeColourDict['qstr'] = '__icontains'
			FleshStipeColourDict['model'] = apps.get_model(app_label='fungi', model_name=FleshStipeColourDict['table'])
			FleshStipeColour_list = FleshStipeColourDict['model'].objects.filter(Q(**{FleshStipeColourDict['column']+FleshStipeColourDict['qstr'] :FleshStipeColourDict['SearchTerm']}))
			for i in FleshStipeColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="FleshStipeBruiseColour":
			FleshStipeBruiseColourDict = {}
			FleshStipeBruiseColourDict['SearchTerm'] = QParams[i]
			FleshStipeBruiseColourDict['table'] = 'Flesh'
			FleshStipeBruiseColourDict['column'] = 'FleshStipeBruiseColour'
			FleshStipeBruiseColourDict['qstr'] = '__icontains'
			FleshStipeBruiseColourDict['model'] = apps.get_model(app_label='fungi', model_name=FleshStipeBruiseColourDict['table'])
			FleshStipeBruiseColour_list = FleshStipeBruiseColourDict['model'].objects.filter(Q(**{FleshStipeBruiseColourDict['column']+FleshStipeBruiseColourDict['qstr'] :FleshStipeBruiseColourDict['SearchTerm']}))
			for i in FleshStipeBruiseColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="FleshStipeCutColour":
			FleshStipeCutColourDict = {}
			FleshStipeCutColourDict['SearchTerm'] = QParams[i]
			FleshStipeCutColourDict['table'] = 'Flesh'
			FleshStipeCutColourDict['column'] = 'FleshStipeCutColour'
			FleshStipeCutColourDict['qstr'] = '__icontains'
			FleshStipeCutColourDict['model'] = apps.get_model(app_label='fungi', model_name=FleshStipeCutColourDict['table'])
			FleshStipeCutColour_list = FleshStipeCutColourDict['model'].objects.filter(Q(**{FleshStipeCutColourDict['column']+FleshStipeCutColourDict['qstr'] :FleshStipeCutColourDict['SearchTerm']}))
			for i in FleshStipeCutColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="SporeColour":
			SporeColourDict = {}
			SporeColourDict['SearchTerm'] = QParams[i]
			SporeColourDict['table'] = 'Spores'
			SporeColourDict['column'] = 'Colour'
			SporeColourDict['qstr'] = '__icontains'
			SporeColourDict['model'] = apps.get_model(app_label='fungi', model_name=SporeColourDict['table'])
			SporeColour_list = SporeColourDict['model'].objects.filter(Q(**{SporeColourDict['column']+SporeColourDict['qstr'] :SporeColourDict['SearchTerm']}))
			for i in SporeColour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="OtherCommonNames":
			OtherCommonNamesDict = {}
			OtherCommonNamesDict['SearchTerm'] = QParams[i]
			OtherCommonNamesDict['table'] = 'OtherCommonNames'
			OtherCommonNamesDict['column'] = 'AltCommonName'
			OtherCommonNamesDict['qstr'] = '__icontains'
			OtherCommonNamesDict['model'] = apps.get_model(app_label='fungi', model_name=OtherCommonNamesDict['table'])
			OtherCommonNames_list = OtherCommonNamesDict['model'].objects.filter(Q(**{OtherCommonNamesDict['column']+OtherCommonNamesDict['qstr'] :OtherCommonNamesDict['SearchTerm']}))
			for i in OtherCommonNames_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="OtherLatinNames":
			OtherLatinNamesDict = {}
			OtherLatinNamesDict['SearchTerm'] = QParams[i]
			OtherLatinNamesDict['table'] = 'OtherLatinNames'
			OtherLatinNamesDict['column'] = 'AltLatinName'
			OtherLatinNamesDict['qstr'] = '__icontains'
			OtherLatinNamesDict['model'] = apps.get_model(app_label='fungi', model_name=OtherLatinNamesDict['table'])
			OtherLatinNames_list = OtherLatinNamesDict['model'].objects.filter(Q(**{OtherLatinNamesDict['column']+OtherLatinNamesDict['qstr'] :OtherLatinNamesDict['SearchTerm']}))
			for i in OtherLatinNames_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="Kingdom":
			KingdomDict = {}
			KingdomDict['SearchTerm'] = QParams[i]
			KingdomDict['table'] = 'Classification'
			KingdomDict['column'] = 'Kingdom'
			KingdomDict['qstr'] = '__icontains'
			KingdomDict['model'] = apps.get_model(app_label='fungi', model_name=KingdomDict['table'])
			Kingdom_list = KingdomDict['model'].objects.filter(Q(**{KingdomDict['column']+KingdomDict['qstr'] :KingdomDict['SearchTerm']}))
			for i in Kingdom_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="Phyum":
			PhyumDict = {}
			PhyumDict['SearchTerm'] = QParams[i]
			PhyumDict['table'] = 'Classification'
			PhyumDict['column'] = 'Phyum'
			PhyumDict['qstr'] = '__icontains'
			PhyumDict['model'] = apps.get_model(app_label='fungi', model_name=PhyumDict['table'])
			Phyum_list = PhyumDict['model'].objects.filter(Q(**{PhyumDict['column']+PhyumDict['qstr'] :PhyumDict['SearchTerm']}))
			for i in Phyum_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="SubPhyum":
			SubPhyumDict = {}
			SubPhyumDict['SearchTerm'] = QParams[i]
			SubPhyumDict['table'] = 'Classification'
			SubPhyumDict['column'] = 'SubPhyum'
			SubPhyumDict['qstr'] = '__icontains'
			SubPhyumDict['model'] = apps.get_model(app_label='fungi', model_name=SubPhyumDict['table'])
			SubPhyum_list = SubPhyumDict['model'].objects.filter(Q(**{SubPhyumDict['column']+SubPhyumDict['qstr'] :SubPhyumDict['SearchTerm']}))
			for i in SubPhyum_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="Class":
			ClassDict = {}
			ClassDict['SearchTerm'] = QParams[i]
			ClassDict['table'] = 'Classification'
			ClassDict['column'] = 'Class'
			ClassDict['qstr'] = '__icontains'
			ClassDict['model'] = apps.get_model(app_label='fungi', model_name=ClassDict['table'])
			Class_list = ClassDict['model'].objects.filter(Q(**{ClassDict['column']+ClassDict['qstr'] :ClassDict['SearchTerm']}))
			for i in Class_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="SubClass":
			SubClassDict = {}
			SubClassDict['SearchTerm'] = QParams[i]
			SubClassDict['table'] = 'Classification'
			SubClassDict['column'] = 'SubClass'
			SubClassDict['qstr'] = '__icontains'
			SubClassDict['model'] = apps.get_model(app_label='fungi', model_name=SubClassDict['table'])
			SubClass_list = SubClassDict['model'].objects.filter(Q(**{SubClassDict['column']+SubClassDict['qstr'] :SubClassDict['SearchTerm']}))
			for i in SubClass_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="Order":
			OrderDict = {}
			OrderDict['SearchTerm'] = QParams[i]
			OrderDict['table'] = 'Classification'
			OrderDict['column'] = 'Order'
			OrderDict['qstr'] = '__icontains'
			OrderDict['model'] = apps.get_model(app_label='fungi', model_name=OrderDict['table'])
			Order_list = OrderDict['model'].objects.filter(Q(**{OrderDict['column']+OrderDict['qstr'] :OrderDict['SearchTerm']}))
			for i in Order_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="Family":
			FamilyDict = {}
			FamilyDict['SearchTerm'] = QParams[i]
			FamilyDict['table'] = 'Classification'
			FamilyDict['column'] = 'Family'
			FamilyDict['qstr'] = '__icontains'
			FamilyDict['model'] = apps.get_model(app_label='fungi', model_name=FamilyDict['table'])
			Family_list = FamilyDict['model'].objects.filter(Q(**{FamilyDict['column']+FamilyDict['qstr'] :FamilyDict['SearchTerm']}))
			for i in Family_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="Genus":
			GenusDict = {}
			GenusDict['SearchTerm'] = QParams[i]
			GenusDict['table'] = 'Classification'
			GenusDict['column'] = 'Genus'
			GenusDict['qstr'] = '__icontains'
			GenusDict['model'] = apps.get_model(app_label='fungi', model_name=GenusDict['table'])
			Genus_list = GenusDict['model'].objects.filter(Q(**{GenusDict['column']+GenusDict['qstr'] :GenusDict['SearchTerm']}))
			for i in Genus_list:
				ResultsList.append(i.Fungi_id)	


		elif i =="PoisonType":
			PoisonTypeDict = {}
			PoisonTypeDict['SearchTerm'] = QParams[i]
			PoisonTypeDict['table'] = 'Cuisine'
			PoisonTypeDict['column'] = 'PoisonType'
			PoisonTypeDict['qstr'] = '__icontains'
			PoisonTypeDict['model'] = apps.get_model(app_label='fungi', model_name=PoisonTypeDict['table'])
			PoisonType_list = PoisonTypeDict['model'].objects.filter(Q(**{PoisonTypeDict['column']+PoisonTypeDict['qstr'] :PoisonTypeDict['SearchTerm']}))
			for i in PoisonType_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="CulinaryRating":
			CulinaryRatingDict = {}
			CulinaryRatingDict['SearchTerm'] = QParams[i]
			CulinaryRatingDict['table'] = 'Cuisine'
			CulinaryRatingDict['column'] = 'CulinaryRating'
			CulinaryRatingDict['qstr'] = '__icontains'
			CulinaryRatingDict['model'] = apps.get_model(app_label='fungi', model_name=CulinaryRatingDict['table'])
			CulinaryRating_list = CulinaryRatingDict['model'].objects.filter(Q(**{CulinaryRatingDict['column']+CulinaryRatingDict['qstr'] :CulinaryRatingDict['SearchTerm']}))
			for i in CulinaryRating_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="Odour":
			OdourDict = {}
			OdourDict['SearchTerm'] = QParams[i]
			OdourDict['table'] = 'Cuisine'
			OdourDict['column'] = 'Odour'
			OdourDict['qstr'] = '__icontains'
			OdourDict['model'] = apps.get_model(app_label='fungi', model_name=OdourDict['table'])
			Odour_list = OdourDict['model'].objects.filter(Q(**{OdourDict['column']+OdourDict['qstr'] :OdourDict['SearchTerm']}))
			for i in Odour_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="Taste":
			TasteDict = {}
			TasteDict['SearchTerm'] = QParams[i]
			TasteDict['table'] = 'Cuisine'
			TasteDict['column'] = 'Taste'
			TasteDict['qstr'] = '__icontains'
			TasteDict['model'] = apps.get_model(app_label='fungi', model_name=TasteDict['table'])
			Taste_list = TasteDict['model'].objects.filter(Q(**{TasteDict['column']+TasteDict['qstr'] :TasteDict['SearchTerm']}))
			for i in Taste_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="StatusStatusData":
			StatusStatusDataDict = {}
			StatusStatusDataDict['SearchTerm'] = QParams[i]
			StatusStatusDataDict['table'] = 'Status'
			StatusStatusDataDict['column'] = 'StatusData'
			StatusStatusDataDict['qstr'] = '__icontains'
			StatusStatusDataDict['model'] = apps.get_model(app_label='fungi', model_name=StatusStatusDataDict['table'])
			StatusStatusData_list = StatusStatusDataDict['model'].objects.filter(Q(**{StatusStatusDataDict['column']+StatusStatusDataDict['qstr'] :StatusStatusDataDict['SearchTerm']}))
			for i in StatusStatusData_list:
				ResultsList.append(i.Fungi_id)	

		elif i =="StatusWhereFound":
			StatusWhereFoundDict = {}
			StatusWhereFoundDict['SearchTerm'] = QParams[i]
			StatusWhereFoundDict['table'] = 'Status'
			StatusWhereFoundDict['column'] = 'WhereFound'
			StatusWhereFoundDict['qstr'] = '__icontains'
			StatusWhereFoundDict['model'] = apps.get_model(app_label='fungi', model_name=StatusWhereFoundDict['table'])
			StatusWhereFound_list = StatusWhereFoundDict['model'].objects.filter(Q(**{StatusWhereFoundDict['column']+StatusWhereFoundDict['qstr'] :StatusWhereFoundDict['SearchTerm']}))
			for i in StatusWhereFound_list:
				ResultsList.append(i.Fungi_id)	


		FiD = collections.Counter(ResultsList)
		for match, count in sorted(FiD.items()):
			if count == SearchTermsCount:
				M = Fungi.objects.get(id= match)
				Matches.append(M)

			#print('"%s" is repeated %d time%s.' % (match, count, "s" if count > 1 else ""))

	return Matches
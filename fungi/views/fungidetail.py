from django.views.generic import DetailView
from usersettings.models import Show
from fungi.models import Fungi
from fungi.models import *

class FungiDetail(DetailView):
    model = Fungi
    template_name = 'fungi/detail.html'
    context_object_name = 'funRetrievedObjectsetail'

    def get_context_data(self, **kwargs):
        context = super(FungiDetail, self).get_context_data(**kwargs)

        NoDataToDisplay = True

        def DataPresent(Fungi_attribute):
            count =0
            context_var =[f for f in Fungi_attribute._meta.get_fields() if f.name not in  ['id', 'DataPresent', 'Fungi']]
            for i in context_var:
                count += count
                field_value = getattr(Fungi_attribute, i.name, None)
                if field_value == None:
                    field_value = 'NoData'
                if field_value == 'NoData' or field_value == 0.00 or field_value == 'no comments' or field_value == 'NoData66':
                    DP = False
                else:
                    DP = 'True'
                    break
            return DP   

        #retrieving user id's to get filter preferences
        #if request.user.is_authenticated
        U = self.request.user
        UserShowSettings = Show.objects.get(user_id= U.id)

        #if UserShowSettings.ShowNonUKOccurences:

        #LINKS
        RetrievedObjects = NetLinks.objects.filter(Fungi_id= self.object).distinct()
        if RetrievedObjects:
            context['NetLinks'] = RetrievedObjects

        #PICTURES
        RetrievedObjects = Picture.objects.get(Fungi_id= self.object)
        context['Picture'] = RetrievedObjects

        #HABITAT
        PID = Habitat.objects.get(Fungi_id= self.object)
        if DataPresent(PID):
            DataToDisplay = False
            context['ShowHabitatFlag'] = 'Yes'
            context['DataToDisplay'] = True

            if UserShowSettings.ShowHabitat:
                RetrievedObjects = Habitat.objects.get(Fungi_id= self.object)
                context['Associations'] = RetrievedObjects.Associations
                context['Ph'] = RetrievedObjects.Ph
                context['Soil'] = RetrievedObjects.Soil
                context['HabitatComments'] = RetrievedObjects.Comments
                context['ShowHabitatFlag'] = 'Yes'
                context['DataToDisplay'] = True
            else:
                context['ShowHabitatFlag'] = 'No'        

        #FUNGI COMMENTS

        PID = FungiComments.objects.get(Fungi_id= self.object)
        if DataPresent(PID):
            context['FungiCommentsFlag'] = 'Yes'
            if UserShowSettings.ShowFungiComments:
                RetrievedObjects = FungiComments.objects.get(Fungi_id= self.object)
                context['FungiComments'] = RetrievedObjects.Comments
                context['FungiCommentsFlag'] = 'Yes'
                context['DataToDisplay'] = True
            else:
                context['FungiCommentsFlag'] = 'No'
        else:
            context['FungiCommentsFlag'] = 'No'     

        #COMMONNAMES
        PID = OtherCommonNames.objects.filter(Fungi_id= self.object).first()
        if DataPresent(PID):
            context['ShowCommonNameFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowOtherCommonNames:
                RetrievedObjects = OtherCommonNames.objects.filter(Fungi_id= self.object)
                if RetrievedObjects:
                    context['OtherCommonNames'] = RetrievedObjects
                    context['ShowCommonNameFlag'] = 'Yes'
                else:
                    context['ShowCommonNameFlag'] = 'No'
        else:
            context['ShowCommonNameFlag'] = 'No'

        #SIMILARTO
        PID = SimilarFungi.objects.filter(Fungi_id= self.object).first()
        if DataPresent(PID):
            context['ShowSimilarFungiFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowSimilarFungi:
                RetrievedObjects = SimilarFungi.objects.filter(Fungi_id= self.object).distinct()
                if RetrievedObjects:
                    context['SimilarFungiNames'] = RetrievedObjects
                    context['ShowSimilarFungiFlag'] = 'Yes'
            else:
                context['ShowSimilarFungiFlag'] = 'No'
        else:
            context['ShowSimilarFungiFlag'] = 'No'

        #OTHERLATINNAMES
        PID = OtherLatinNames.objects.filter(Fungi_id= self.object).first()
        if DataPresent(PID):
            context['ShowLatinNameFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowOtherLatinNames:
                RetrievedObjects = OtherLatinNames.objects.filter(Fungi_id= self.object).distinct()
                if RetrievedObjects:
                    context['OtherLatinNames'] = RetrievedObjects
                    context['ShowLatinNameFlag'] = 'Yes'
            else:
                context['ShowLatinNameFlag'] = 'No'
        else:
            context['ShowLatinNameFlag'] = 'No'

        #CLASSIFICATION
        if DataPresent(Classification.objects.get(Fungi_id= self.object)):
            context['ShowClassificationFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowClassification:                
                RetrievedObjects = Classification.objects.get(Fungi_id= self.object)
                context['Kingdom'] = RetrievedObjects.Kingdom
                context['Phyum'] = RetrievedObjects.Phyum
                context['SubPhyum'] = RetrievedObjects.SubPhyum
                context['Class'] = RetrievedObjects.Class
                context['SubClass'] = RetrievedObjects.SubClass
                context['Order'] = RetrievedObjects.Order
                context['Family'] = RetrievedObjects.Family
                context['Genus'] = RetrievedObjects.Genus
                context['Source'] = RetrievedObjects.Source

                context['ShowClassificationFlag'] = 'Yes'
            else:
                context['ShowClassificationFlag'] = 'No'
        else:
            context['ShowClassificationFlag'] = 'No'
       
        #CAP
        if DataPresent(Cap.objects.get(Fungi_id= self.object)):
            context['ShowCapFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowCap:                    
                RetrievedObjects = Cap.objects.get(Fungi_id= self.object)
                context['CapColour'] = RetrievedObjects.Colour
                context['CapShapeDescription'] = RetrievedObjects.ShapeDescription
                context['CapRim'] = RetrievedObjects.Rim
                context['CapRimDescription'] = RetrievedObjects.RimDescription
                context['CapTexture'] = RetrievedObjects.CapTexture
                context['CapTextureDescription'] = RetrievedObjects.CapTextureDescription
                context['CapBruiseColour'] = RetrievedObjects.BruiseColour
                context['CapCutColour'] = RetrievedObjects.CutColour
                if float(RetrievedObjects.WidthMin) > 0.00 and float(RetrievedObjects.WidthMax) > 0.00:
                    context['CapWidthMin'] = float(RetrievedObjects.WidthMin)
                    context['CapWidthMax'] = float(RetrievedObjects.WidthMax)
                if float(RetrievedObjects.WidthMin) == 0.00 and float(RetrievedObjects.WidthMax) == 0.00:
                    context['CapWidthMin'] = float(RetrievedObjects.WidthMin)
                    context['CapWidthMax'] = float(RetrievedObjects.WidthMax)    
                if float(RetrievedObjects.WidthMin) == 0.00 and float(RetrievedObjects.WidthMax) > 0.00:
                    context['CapWidthMin'] = "up to"
                    context['CapWidthMax'] = float(RetrievedObjects.WidthMax)
                context['CapComments'] = RetrievedObjects.Comments  
                context['ShowCapFlag'] = 'Yes'
            else:
                context['ShowCapFlag'] = 'No'
        else:
            context['ShowCapFlag'] = 'No'
       
        #STIPE
        if DataPresent(Stipe.objects.get(Fungi_id= self.object)):
            context['ShowStipeFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowStipe:    
                RetrievedObjects = Stipe.objects.get(Fungi_id= self.object)
                context['StipeColour'] = RetrievedObjects.Colour
                context['StipeTexture'] = RetrievedObjects.Texture
                context['TextureDescription'] = RetrievedObjects.TextureDescription
                context['StipeBruiseColour'] = RetrievedObjects.BruiseColour
                context['StipeCutColour'] = RetrievedObjects.CutColour
                if float(RetrievedObjects.ThicknessMin) > 0.00 and float(RetrievedObjects.ThicknessMax) > 0.00:
                    context['StipeThicknessMin'] = float(RetrievedObjects.ThicknessMin)
                    context['StipeThicknessMax'] = float(RetrievedObjects.ThicknessMax)
                if float(RetrievedObjects.ThicknessMin) == 0.00 and float(RetrievedObjects.ThicknessMax) > 0.00:
                    context['StipeThicknessMin'] = "up to"
                    context['StipeThicknessMax'] = float(RetrievedObjects.ThicknessMax)
                if float(RetrievedObjects.ThicknessMin) == 0.00 and float(RetrievedObjects.ThicknessMax) == 0.00:
                    context['StipeThicknessMin'] =float(RetrievedObjects.ThicknessMin)
                    context['StipeThicknessMax'] = float(RetrievedObjects.ThicknessMax)
               
                if RetrievedObjects.LengthMin > 0.00 and RetrievedObjects.LengthMax > 0.00:
                    context['StipeLengthMin'] = round(RetrievedObjects.LengthMin,2)
                    context['StipeLengthMax'] = round(RetrievedObjects.LengthMax,2)
                if RetrievedObjects.LengthMin == 0.00 and RetrievedObjects.LengthMax == 0.00:
                    context['StipeLengthMin'] = round(RetrievedObjects.LengthMin,2)
                    context['StipeLengthMax'] = round(RetrievedObjects.LengthMax,2)
                if RetrievedObjects.LengthMin == 0.00 and RetrievedObjects.LengthMax > 0.00:
                    context['StipeLengthMin'] = "up to"
                    context['StipeLengthMax'] = float(RetrievedObjects.LengthMax)

                context['ShapeDescription'] = RetrievedObjects.ShapeDescription
                context['StipeRing'] = RetrievedObjects.Ring
                context['RingDescription'] = RetrievedObjects.RingDescription
                context['Reticulation'] = RetrievedObjects.ReticulationPresent
                context['ReticulationColour'] = RetrievedObjects.ReticulationColour
                context['ReticulationDescription'] = RetrievedObjects.ReticulationDescription
                context['Base'] = RetrievedObjects.Base
                context['BaseDescription'] = RetrievedObjects.BaseDescription
                context['StipeComments'] = RetrievedObjects.Comments
                context['ShowStipeFlag'] = 'Yes'
            else:
                context['ShowStipeFlag'] = 'No'
        else:
            context['ShowStipeFlag'] = 'No'

        #PORES
        if DataPresent(PoresAndTubes.objects.get(Fungi_id= self.object)):
            context['ShowPoresAndTubesFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowPoresAndTubes:   
                RetrievedObjects = PoresAndTubes.objects.get(Fungi_id= self.object)
                context['PoresPresent'] = RetrievedObjects.PoresPresent
                context['PoreColour'] = RetrievedObjects.PoreColour
                context['PoreShape'] = RetrievedObjects.PoreShape
                context['PoreBruiseColour'] = RetrievedObjects.PoreBruiseColour
                context['TubeColour'] = RetrievedObjects.TubeColour
                context['TubeShape'] = RetrievedObjects.TubeShape
                context['TubeBruiseColour'] = RetrievedObjects.TubeBruiseColour
                context['PoreMilk'] = RetrievedObjects.Milk
                context['PoreComments'] = RetrievedObjects.Comments
                context['ShowPoresAndTubesFlag'] = 'Yes'
            else:
                context['ShowPoresAndTubesFlag'] = 'No'
        else:
            context['ShowPoresAndTubesFlag'] = 'No'

        #GILLS
        if DataPresent(Gills.objects.get(Fungi_id= self.object)):
            context['ShowGillsFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowGills: 
                RetrievedObjects = Gills.objects.get(Fungi_id= self.object)
                context['GillsPresent'] = RetrievedObjects.GillsPresent  
                context['GillsBruiseColour'] = RetrievedObjects.BruiseColour 
                context['GillsCutColour'] = RetrievedObjects.CutColour
                context['GillsAttachment'] = RetrievedObjects.Attachment
                context['GillsArrangement'] = RetrievedObjects.Arrangement  
                context['GillsMilk'] = RetrievedObjects.Milk  
                context['GillsComments'] = RetrievedObjects.Comments  
                context['ShowGillsFlag'] = 'Yes'
            else:
                context['ShowGillsFlag'] = 'No'
        else:
            context['ShowGillsFlag'] = 'No'

        #SPORES
        if DataPresent(Spores.objects.get(Fungi_id= self.object)):
            context['ShowSporesFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowSpores: 
                RetrievedObjects = Spores.objects.get(Fungi_id= self.object)
                context['SporesColour']= RetrievedObjects.Colour  
                context['SporesComments'] = RetrievedObjects.Comments  
                context['ShowSporesFlag'] = 'Yes'
            else:
                context['ShowSporesFlag'] = 'No'
        else:
            context['ShowSporesFlag'] = 'No'


        #FLESH
        if DataPresent(Flesh.objects.get(Fungi_id= self.object)):
            context['ShowFleshFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowFlesh: 
                RetrievedObjects = Flesh.objects.get(Fungi_id= self.object)
                context['FleshCapColour'] = RetrievedObjects.FleshCapColour
                context['FleshCapBruiseColour'] = RetrievedObjects.FleshCapBruiseColour
                context['FleshCapCutColour'] = RetrievedObjects.FleshCapCutColour
                context['FleshStipeColour'] = RetrievedObjects.FleshStipeColour
                context['FleshStipeBruiseColour'] = RetrievedObjects.FleshStipeBruiseColour
                context['FleshStipeCutColour'] = RetrievedObjects.FleshStipeCutColour
                context['FleshComments'] = RetrievedObjects.Comments
                context['ShowFleshFlag'] = 'Yes'
            else:
                context['ShowFleshFlag'] = 'No'
        else:
            context['ShowFleshFlag'] = 'No'

        #STATUS
        if DataPresent(Status.objects.get(Fungi_id= self.object)):
            context['ShowStatusFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowStatus: 
                if Status.objects.filter(Fungi_id= self.object):
                    RetrievedObjects = Status.objects.get(Fungi_id= self.object)
                    context['StatusData'] = RetrievedObjects.StatusData
                    context['WhereFound'] = RetrievedObjects.WhereFound
                    context['StatusComments'] = RetrievedObjects.StatusComments
                    context['UKOccurences'] = RetrievedObjects.UKOccurences
                    context['RecordedInUK'] = RetrievedObjects.RecordedInUK
                    context['ShowStatusFlag'] = 'Yes'
            else:
                context['ShowStatusFlag'] = 'No'
        else:
            context['ShowStatusFlag'] = 'No'

        #SEASON
        if DataPresent(Seasons.objects.get(Fungi_id= self.object)):
            context['ShowSeasonFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowSeasons: 
                RetrievedObjects =  Seasons.objects.get(Fungi_id= self.object)
                if RetrievedObjects.Season != 'NoData':
                    From = RetrievedObjects.Season[0:RetrievedObjects.Season.index(',')]            
                    To = RetrievedObjects.Season[(RetrievedObjects.Season.rfind(','))+1:len(RetrievedObjects.Season)]
                    FruitingSeason = 'Season: '+From+'-'+To 
                    context['FruitingSeason'] = FruitingSeason
                    context['SeasonComments'] = RetrievedObjects.Comments
                    context['ShowSeasonFlag'] = 'Yes'
            else:
                context['ShowSeasonFlag'] = 'No'
        else:
            context['ShowSeasonFlag'] = 'No'

        #CUISINE
        RetrievedObjects = Cuisine.objects.get(Fungi_id= self.object)
        if DataPresent(Cuisine.objects.get(Fungi_id= self.object)):
            context['ShowCuisineFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowCuisine: 
                RetrievedObjects = Cuisine.objects.get(Fungi_id= self.object)
                context['PoisonType'] = RetrievedObjects.PoisonType
                context['CulinaryRating'] = RetrievedObjects.CulinaryRating
                context['Odour']= RetrievedObjects.Odour
                context['Taste'] = RetrievedObjects.Taste
                context['CuisineComments'] = RetrievedObjects.Comments
                context['ShowCuisineFlag'] = 'Yes'
            else:
                context['ShowCuisineFlag'] = 'No'
        else:
            context['ShowCuisineFlag'] = 'No'

        return context
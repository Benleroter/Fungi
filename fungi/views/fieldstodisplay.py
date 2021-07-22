from django import forms 
from fungi.views.choices import *


def FieldsToDisplay(UserSearchFields):
    fieldsToDisplay = {}

    if UserSearchFields.CommonName:
        fieldsToDisplay['CommonName'] = forms.CharField(required=False, max_length=255, label='Common Name', initial='cn')

    if UserSearchFields.LatinName:
        fieldsToDisplay['LatinName'] = forms.CharField(required=False, max_length=255, label='Latin Name', initial='')
            
    if UserSearchFields.HabitatAssociations:
        fieldsToDisplay['HabitatAssociations'] = forms.CharField(required=False, max_length=255, label='Associated Trees', initial='')
                     
    if UserSearchFields.HabitatPh:
        fieldsToDisplay['HabitatPh'] = forms.ChoiceField(choices = PhTypeChoices, required=False, label='Ph',initial='')

    if UserSearchFields.HabitatGrowingMedium:
        fieldsToDisplay['HabitatGrowingMedium'] = forms.CharField(required=False, max_length=255, label='Growing Medium',initial='')

    if UserSearchFields.HabitatSoil:
        fieldsToDisplay['HabitatSoil'] = forms.CharField(required=False, max_length=255, label='Growing Medium', initial='')

    if UserSearchFields.MonthFound:
        fieldsToDisplay['MonthFound'] = forms.ChoiceField(choices = MonthFoundChoices, required=False, label='Month Found',initial='month')

    if UserSearchFields.CapColour:
        fieldsToDisplay['CapColour'] = forms.CharField(required=False, max_length=255, label='Cap Colour', initial='')
 
    if UserSearchFields.CapShape:
        fieldsToDisplay['CapShape'] = forms.CharField(required=False, max_length=255, label='Cap Shape', initial='')

    if UserSearchFields.CapRim:
        fieldsToDisplay['CapRim'] = forms.ChoiceField(choices = CapRimChoices, required=False, label='Cap Rim', initial='')

    if UserSearchFields.CapTexture:
        fieldsToDisplay['CapTexture'] = forms.ChoiceField(choices=CapTextureChoices,required=False, label='Cap Texture', initial='')

    if UserSearchFields.CapBruiseColour:
        fieldsToDisplay['CapBruiseColour'] = forms.CharField(required=False, max_length=255, label='Cap Bruise Colour', initial='')

    if UserSearchFields.CapCutColour:
        fieldsToDisplay['CapCutColour'] = forms.CharField(required=False, max_length=255, label='Cap Cut Colour', initial='')

    if UserSearchFields.CapWidth:
        fieldsToDisplay['CapWidth'] = forms.CharField(required=False, max_length=255, label='Cap Width', initial='')

    if UserSearchFields.StipeColour:
        fieldsToDisplay['StipeColour'] = forms.CharField(required=False, max_length=255, label='Stipe Colour', initial='')

    if UserSearchFields.StipeBruiseColour:
        fieldsToDisplay['StipeBruiseColour'] = forms.CharField(required=False, max_length=255, label='Stipe Bruise Colour', initial='')

    if UserSearchFields.StipeCutColour:
        fieldsToDisplay['StipeCutColour'] = forms.CharField(required=False, max_length=255, label='Stipe Cut Colour', initial='')

    if UserSearchFields.StipeLength:
        fieldsToDisplay['StipeLength'] = forms.CharField(required=False, max_length=255, label='Stipe Length', initial='')

    if UserSearchFields.StipeThickness:
        fieldsToDisplay['StipeThickness'] = forms.CharField(required=False, max_length=255, label='Stipe Thickness', initial='')

    if UserSearchFields.StipeShape:
        fieldsToDisplay['StipeShape'] = forms.CharField(required=False, max_length=255, label='Stipe Shape', initial='')

    if UserSearchFields.StipeReticulationPresent:
        fieldsToDisplay['StipeReticulationPresent'] = forms.ChoiceField(choices = ReticulationChoices, required=False, label='Stipe Reticutaion Present', initial='')
 
    if UserSearchFields.StipeReticulationColour:
        fieldsToDisplay['StipeReticulationColour'] = forms.CharField(required=False, max_length=255, label='Reticulation Colour', initial='')

    if UserSearchFields.StipeBase:
        fieldsToDisplay['StipeBase'] = forms.CharField(required=False, max_length=255, label='Stipe Base', initial='')

    if UserSearchFields.StipeTexture:        
        fieldsToDisplay['StipeTexture'] = forms.ChoiceField(choices = StipeTextureChoices, required=False, label='Stipe Texture', initial='')

    if UserSearchFields.StipeRing:
        fieldsToDisplay['StipeRing'] = forms.ChoiceField(choices = StipeRingChoices, required=False, label='Stipe Ring', initial='')

    if UserSearchFields.PoresPresent:
        fieldsToDisplay['PoresPresent'] = forms.ChoiceField(choices = PoresPresentChoices, required=False, label='Pores Present', initial='')

    if UserSearchFields.PoreColour:
        fieldsToDisplay['PoreColour'] = forms.CharField(required=False, max_length=255, label='Pore Colour', initial='')

    if UserSearchFields.PoreShape:
        fieldsToDisplay['PoreShape'] = forms.CharField(required=False, max_length=255, label='Pore Shape', initial='')

    if UserSearchFields.PoreBruiseColour:
        fieldsToDisplay['PoreBruiseColour'] = forms.CharField(required=False, max_length=255, label='Pore Bruise Colour', initial='')

    if UserSearchFields.TubeColour:
        fieldsToDisplay['TubeColour'] = forms.CharField(required=False, max_length=255, label='Latin Name', initial='')

    if UserSearchFields.TubeShape:
        fieldsToDisplay['TubeShape'] = forms.CharField(required=False, max_length=255, label='Tube Shap', initial='')

    if UserSearchFields.TubeBruiseColour:
        fieldsToDisplay['TubeBruiseColour'] = forms.CharField(required=False, max_length=255, label='Tube TubeBruiseColour Colour', initial='')

    if UserSearchFields.PoreMilk:
        fieldsToDisplay['PoreMilk'] = forms.ChoiceField(choices =PoresMilkChoices, required=False, label='Pore Milk', initial='')

    if UserSearchFields.GillsPresent:
        fieldsToDisplay['GillsPresent'] = forms.ChoiceField(choices =GillsPresentChoices, required=False, label='Gills Present', initial='')

    if UserSearchFields.GillsColour:
        fieldsToDisplay['GillsColour'] = forms.CharField(required=False, max_length=255, label='Gills Colour', initial='')
 
    if UserSearchFields.GillsBruiseColour:
        fieldsToDisplay['GillsBruiseColour'] = forms.CharField(required=False, max_length=255, label='Gills Bruise Colour', initial='')

    if UserSearchFields.GillsCutColour:
        fieldsToDisplay['GillsCutColour'] = forms.CharField(required=False, max_length=255, label='Gills Cut Colour', initial='')

    if UserSearchFields.GillsAttachment:
        fieldsToDisplay['GillsAttachment'] = forms.CharField(required=False, max_length=255, label='Gills Attachment', initial='')

    if UserSearchFields.GillsArrangement:
        fieldsToDisplay['GillsArrangement'] = forms.CharField(required=False, max_length=255, label='Gills Arrangement', initial='')

    if UserSearchFields.GillsMilk:
        fieldsToDisplay['GillsMilk'] = forms.ChoiceField(choices =GillsMilkChoices, required=False, label='Gill Milk', initial='')

    if UserSearchFields.FleshCapColour:
        fieldsToDisplay['FleshCapColour'] = forms.CharField(required=False, max_length=255, label='Cap Flesh Colour ', initial='')

    if UserSearchFields.FleshCapBruiseColour:
        fieldsToDisplay['FleshCapBruiseColour'] = forms.CharField(required=False, max_length=255, label='Cap Flesh Bruise Colour', initial='')

    if UserSearchFields.FleshCapCutColour:
        fieldsToDisplay['FleshCapCutColour'] = forms.CharField(required=False, max_length=255, label='Cap Flesh Cut Colour', initial='')

    if UserSearchFields.FleshStipeColour:
        fieldsToDisplay['FleshStipeBruiseColour'] = forms.CharField(required=False, max_length=255, label='Stipe Flesh Colour', initial='')

    if UserSearchFields.FleshStipeBruiseColour:
        fieldsToDisplay['FleshStipeBruiseColour'] = forms.CharField(required=False, max_length=255, label='Stipe Flesh Bruise Colour', initial='')

    if UserSearchFields.FleshStipeCutColour:
        fieldsToDisplay['FleshStipeCutColour'] = forms.CharField(required=False, max_length=255, label='Stipe Flesh Cut Colour', initial='')

    if UserSearchFields.SporeColour:
        fieldsToDisplay['SporeColour'] = forms.CharField(required=False, max_length=255, label='Spore Colour', initial='')

    if UserSearchFields.OtherCommonNames:
        fieldsToDisplay['OtherCommonNames'] = forms.CharField(required=False, max_length=255, label='Other Common Name', initial='')

    if UserSearchFields.OtherLatinNames:
        fieldsToDisplay['OtherLatinNames'] = forms.CharField(required=False, max_length=255, label='Other Latin Name', initial='')

    if UserSearchFields.Kingdom:
        fieldsToDisplay['Kingdom'] = forms.CharField(required=False, max_length=255, label='Taxonmic Kingdom', initial='')        

    if UserSearchFields.Phyum:
        fieldsToDisplay['Phyum'] = forms.CharField(required=False, max_length=255, label='Taxonmic Phyum', initial='')

    if UserSearchFields.SubPhyum:
        fieldsToDisplay['SubPhyum'] = forms.CharField(required=False, max_length=255, label='Taxonmic SubPhyum', initial='')        

    if UserSearchFields.Class:
        fieldsToDisplay['Class'] = forms.CharField(required=False, max_length=255, label='Taxonmic Class', initial='')

    if UserSearchFields.SubClass:
        fieldsToDisplay['SubClass'] = forms.CharField(required=False, max_length=255, label='Taxonmic SubClass', initial='')        
 
    if UserSearchFields.Order:
        fieldsToDisplay['Order'] = forms.CharField(required=False, max_length=255, label='Taxonmic Order', initial='')

    if UserSearchFields.Family:
        fieldsToDisplay['Family'] = forms.CharField(required=False, max_length=255, label='Taxonmic Family', initial='')

    if UserSearchFields.Genus:
        fieldsToDisplay['Genus'] = forms.CharField(required=False, max_length=255, label='Taxonmic Genus', initial='')        

    if UserSearchFields.PoisonType:
        fieldsToDisplay['PoisonType'] = forms.CharField(required=False, max_length=255, label='Poison Type', initial='')

    if UserSearchFields.CulinaryRating:
        fieldsToDisplay['CulinaryRating'] = forms.ChoiceField(choices=CulinaryRatingChoices,required=False, label='Culinary Rating', initial='')
        #fieldsToDisplay['CulinaryRating'] = forms.CharField(required=False, max_length=255, label='Culinary Rating', initial='')

    if UserSearchFields.Odour:
        fieldsToDisplay['Odour'] = forms.CharField(required=False, max_length=255, label='Odour', initial='')

    if UserSearchFields.Taste:
        fieldsToDisplay['Taste'] = forms.CharField(required=False, max_length=255, label='Taste', initial='')

    if UserSearchFields.StatusStatusData:
        fieldsToDisplay['StatusStatusData'] = forms.CharField(required=False, max_length=255, label='Status', initial='')

    if UserSearchFields.StatusWhereFound:
        fieldsToDisplay['StatusWhereFound'] = forms.CharField(required=False, max_length=255, label='Where Found', initial='')

    return fieldsToDisplay

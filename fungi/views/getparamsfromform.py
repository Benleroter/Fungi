
 
def GetParamsFromForm(form):
       QParams = {}
       field_name = 'CommonName'
       if field_name in form.fields:
              QParams["CommonName"] = form.cleaned_data['CommonName']

       field_name = 'LatinName'
       if field_name in form.fields:
              QParams["LatinName"] = form.cleaned_data['LatinName']

       field_name = 'HabitatAssociations'
       if field_name in form.fields:
              QParams["HabitatAssociations"] = form.cleaned_data['HabitatAssociations']

       field_name = 'HabitatPh'
       if field_name in form.fields:
              QParams["HabitatPh"] = form.cleaned_data['HabitatPh']

       field_name = 'HabitatGrowingMedium'
       if field_name in form.fields:
              QParams["HabitatGrowingMedium"] = form.cleaned_data['HabitatGrowingMedium']

       field_name = 'HabitatSoil'
       if field_name in form.fields:
              QParams["HabitatSoil"] = form.cleaned_data['HabitatSoil']

       field_name = 'MonthFound'
       if field_name in form.fields:
              QParams["Season"] = form.cleaned_data['MonthFound']

       field_name = 'CapColour'
       if field_name in form.fields:
              QParams["CapColour"] = form.cleaned_data['CapColour']

       field_name = 'CapShape'
       if field_name in form.fields:
              QParams["CapShape"] = form.cleaned_data['CapShape']

       field_name = 'CapRim'
       if field_name in form.fields:
              QParams["CapRim"] = form.cleaned_data['CapRim']

       field_name = 'CapTexture'
       if field_name in form.fields:
              QParams["CapTexture"] = form.cleaned_data['CapTexture']

       field_name = 'CapBruiseColour'
       if field_name in form.fields:
              QParams["CapBruiseColour"] = form.cleaned_data['CapBruiseColour']

       field_name = 'CapCutColour'
       if field_name in form.fields:
              QParams["CapCutColour"] = form.cleaned_data['CapCutColour']

       field_name = 'CapWidth'
       if field_name in form.fields:
              QParams["CapWidth"] = form.cleaned_data['CapWidth']

       field_name = 'StipeColour'
       if field_name in form.fields:
              QParams["StipeColour"] = form.cleaned_data['StipeColour']

       field_name = 'StipeBruiseColour'
       if field_name in form.fields:
              QParams["StipeBruiseColour"] = form.cleaned_data['StipeBruiseColour']

       field_name = 'StipeCutColour'
       if field_name in form.fields:
              QParams["StipeCutColour"] = form.cleaned_data['StipeCutColour']

       field_name = 'StipeLength'
       if field_name in form.fields:
              QParams["StipeLength"] = form.cleaned_data['StipeLength']

       field_name = 'StipeThickness'
       if field_name in form.fields:
              QParams["StipeThickness"] = form.cleaned_data['StipeThickness']
 
       field_name = 'StipeShape'
       if field_name in form.fields:
              QParams["StipeShape"] = form.cleaned_data['StipeShape']

       field_name = 'StipeReticulationPresent'
       if field_name in form.fields:
              QParams["StipeReticulationPresent"] = form.cleaned_data['StipeReticulationPresent']

       field_name = 'StipeReticulationColour'
       if field_name in form.fields:
              QParams["StipeReticulationColour"] = form.cleaned_data['StipeReticulationColour']
 
       field_name = 'StipeBase'
       if field_name in form.fields:
              QParams["StipeBase"] = form.cleaned_data['StipeBase']

       field_name = 'StipeTexture'
       if field_name in form.fields:
              QParams["StipeTexture"] = form.cleaned_data['StipeTexture']

       field_name = 'StipeRing'
       if field_name in form.fields:
              QParams["StipeRing"] = form.cleaned_data['StipeRing']

       field_name = 'PoresPresent'
       if field_name in form.fields:
              QParams["PoresPresent"] = form.cleaned_data['PoresPresent']

       field_name = 'PoreColour'
       if field_name in form.fields:
              QParams["PoreColour"] = form.cleaned_data['PoreColour']

       field_name = 'PoreShape'
       if field_name in form.fields:
              QParams["PoreShape"] = form.cleaned_data['PoreShape']
 
       field_name = 'PoreBruiseColour'
       if field_name in form.fields:
              QParams["PoreBruiseColour"] = form.cleaned_data['PoreBruiseColour']

       field_name = 'TubeColour'
       if field_name in form.fields:
              QParams["TubeColour"] = form.cleaned_data['TubeColour']

       field_name = 'TubeShape'
       if field_name in form.fields:
              QParams["TubeShape"] = form.cleaned_data['TubeShape']

       field_name = 'TubeBruiseColour'
       if field_name in form.fields:
              QParams["TubeBruiseColour"] = form.cleaned_data['TubeBruiseColour']

       field_name = 'PoreMilk'
       if field_name in form.fields:
              QParams["PoreMilk"] = form.cleaned_data['PoreMilk']

       field_name = 'GillsPresent'
       if field_name in form.fields:
              QParams["GillsPresent"] = form.cleaned_data['GillsPresent']

       field_name = 'GillsColour'
       if field_name in form.fields:
              QParams["GillsColour"] = form.cleaned_data['GillsColour']

       field_name = 'GillsBruiseColour'
       if field_name in form.fields:
              QParams["GillsBruiseColour"] = form.cleaned_data['GillsBruiseColour']
 
       field_name = 'GillsCutColour'
       if field_name in form.fields:
              QParams["GillsCutColour"] = form.cleaned_data['GillsCutColour']

       field_name = 'GillsAttachment'
       if field_name in form.fields:
              QParams["GillsAttachment"] = form.cleaned_data['GillsAttachment']

       field_name = 'GillsArrangement'
       if field_name in form.fields:
              QParams["GillsArrangement"] = form.cleaned_data['GillsArrangement']

       field_name = 'GillsMilk'
       if field_name in form.fields:
              QParams["GillsMilk"] = form.cleaned_data['GillsMilk']

       field_name = 'FleshCapColour'
       if field_name in form.fields:
              QParams["FleshCapColour"] = form.cleaned_data['FleshCapColour']

       field_name = 'FleshCapBruiseColour'
       if field_name in form.fields:
              QParams["FleshCapBruiseColour"] = form.cleaned_data['FleshCapBruiseColour']

       field_name = 'FleshCapCutColour'
       if field_name in form.fields:
              QParams["FleshCapCutColour"] = form.cleaned_data['FleshCapCutColour']

       field_name = 'FleshStipeColour'
       if field_name in form.fields:
              QParams["FleshStipeColour"] = form.cleaned_data['FleshStipeColour']

       field_name = 'FleshStipeBruiseColour'
       if field_name in form.fields:
              QParams["FleshStipeBruiseColour"] = form.cleaned_data['FleshStipeBruiseColour']

       field_name = 'FleshStipeCutColour'
       if field_name in form.fields:
              QParams["FleshStipeCutColour"] = form.cleaned_data['FleshStipeCutColour']

       field_name = 'SporeColour'
       if field_name in form.fields:
              QParams["SporeColour"] = form.cleaned_data['SporeColour']

       field_name = 'OtherCommonNames'
       if field_name in form.fields:
              QParams["OtherCommonNames"] = form.cleaned_data['OtherCommonNames']

       field_name = 'OtherLatinNames'
       if field_name in form.fields:
              QParams["OtherLatinNames"] = form.cleaned_data['OtherLatinNames']

       field_name = 'Kingdom'
       if field_name in form.fields:
              QParams["Kingdom"] = form.cleaned_data['Kingdom']              

       field_name = 'Phyum'
       if field_name in form.fields:
              QParams["Phyum"] = form.cleaned_data['Phyum']

       field_name = 'SubPhyum'
       if field_name in form.fields:
              QParams["SubPhyum"] = form.cleaned_data['SubPhyum']

       field_name = 'Class'
       if field_name in form.fields:
              QParams["Class"] = form.cleaned_data['Class']

       field_name = 'SubClass'
       if field_name in form.fields:
              QParams["SubClass"] = form.cleaned_data['SubClass']

       field_name = 'Order'
       if field_name in form.fields:
              QParams["Order"] = form.cleaned_data['Order']

       field_name = 'Family'
       if field_name in form.fields:
              QParams["Family"] = form.cleaned_data['Family']

       field_name = 'Genus'
       if field_name in form.fields:
              QParams["Genus"] = form.cleaned_data['Genus']              

       field_name = 'PoisonType'
       if field_name in form.fields:
              QParams["PoisonType"] = form.cleaned_data['PoisonType']
 
       field_name = 'CulinaryRating'
       if field_name in form.fields:
              QParams["CulinaryRating"] = form.cleaned_data['CulinaryRating']

       field_name = 'Odour'
       if field_name in form.fields:
              QParams["Odour"] = form.cleaned_data['Odour']

       field_name = 'Taste'
       if field_name in form.fields:
              QParams["Taste"] = form.cleaned_data['Taste']

       field_name = 'StatusStatusData'
       if field_name in form.fields:
              QParams["StatusStatusData"] = form.cleaned_data['StatusStatusData']

       field_name = 'StatusWhereFound'
       if field_name in form.fields:
              QParams["StatusWhereFound"] = form.cleaned_data['StatusWhereFound']

       field_name = 'StatusRecordedInUK'
       if field_name in form.fields:
              QParams["StatusRecordedInUK"] = form.cleaned_data['StatusRecordedInUK']

       return QParams
from usersettings.models import Show
from django.db.models import Q

def  FungiToSearch(Fungi, ShowOnlyUKOccurences, ShowMacromycetes):
    if ShowOnlyUKOccurences and ShowMacromycetes:
        FungiToShow = Fungi.objects.filter(Q(UKSpecies__iexact="Yes") & Q(Macromycetes__iexact="Yes"))
        FungiCount = Fungi.objects.filter(Q(UKSpecies__iexact="Yes") & Q(Macromycetes__iexact="Yes")).count()
        ResultInfo = 'UK Large Fungi'
      
    elif ShowOnlyUKOccurences and not ShowMacromycetes:
        FungiToShow = Fungi.objects.filter(Q(UKSpecies__iexact="Yes"))
        FungiCount = Fungi.objects.filter(Q(UKSpecies__iexact="Yes")).count()
        ResultInfo = 'UK Fungi'

    elif not ShowOnlyUKOccurences and ShowMacromycetes:
        FungiToShow = Fungi.objects.filter(Q(Macromycetes__iexact="Yes"))
        FungiCount = Fungi.objects.filter(Q(Macromycetes__iexact="Yes")).count()
        ResultInfo = 'Large Fungi'
      
    else:
        if not ShowOnlyUKOccurences and not ShowMacromycetes:
            FungiToShow = Fungi.objects.all()
            FungiCount = Fungi.objects.all().count()
            ResultInfo = 'All Fungi'

    return (FungiToShow,FungiCount,ResultInfo)
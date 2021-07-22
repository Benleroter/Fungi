from django.shortcuts import render
from usersettings.models import ShowSearchFields
from fungi.views.fieldstodisplay import FieldsToDisplay
from fungi.forms import  UserSearchForm
from fungi.views.getparamsfromform import GetParamsFromForm
from fungi.views.editedQparams import EditedQParams
from fungi.views.runsearch import RunSearch
import copy 
import re



def Search(request):
    UserSearchFields = ShowSearchFields.objects.get(user_id= request.user)
    if request.method == 'POST':
        fieldsToDisplay = FieldsToDisplay(UserSearchFields)
        DynamicSearchForm = type('DynamicSearchForm', (UserSearchForm,), fieldsToDisplay)
        form = DynamicSearchForm(request.POST)
        if form.is_valid():
            QParams = GetParamsFromForm(form)
            QParams = EditedQParams(QParams)
            FungiFound = RunSearch(QParams)
            FungiFoundCount = len(FungiFound)
            if FungiFoundCount== 0:
                QParams2 = copy.deepcopy(QParams)
                for key, value in QParams2.items() :
                    res = key
                    s = re.sub(r"(\w)([A-Z])", r"\1 \2", res)
                    new_key = s
                    old_key = res
                    QParams[new_key] = QParams.pop(old_key)
                context = {
                    'SearchTerms': QParams,
                    'SearchTermsCount' : len(QParams)
                }
                return render(request, 'fungi/nosearchresults.html', context)
                
            context = {
                'search_fungi_results': FungiFound,
                'resultscount' : FungiFoundCount,
            }
            
            return render(request, 'fungi/search_results_new.html',  context)


    # if a GET (or any other method) we'll create a blank form
    else:
        fieldsToDisplay = FieldsToDisplay(UserSearchFields)
        DynamicSearchForm = type('DynamicSearchForm', (UserSearchForm,), fieldsToDisplay)
        form = DynamicSearchForm(request.POST)

    return render(request, 'fungi/searchform.html', {'form': form})
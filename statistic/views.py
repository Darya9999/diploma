from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from statistic.models import Stat
from statistic.forms.forms import StatForm
# Create your views here.
def showAnkets(request):
    return render( request, 'index.html', { 'anketaFields' : Stat.objects.all() } )

def post_new(request):
	if request.method == "POST":
		form = StatForm(request.POST)
		if form.is_valid():
			anketa = form.save(commit=False)
			kolvoballov = 0
			if anketa.kind_obr == 'no':
				kolvoballov -= 10
			if anketa.kind_obr == 'neprof':
				kolvoballov += 5
			if anketa.kind_obr == 'prof':
				kolvoballov += 10

			if anketa.kind_exp == 'no':
				kolvoballov -= 10
			if anketa.kind_exp == 'neprof':
				kolvoballov += 3
			if anketa.kind_exp == 'prof1to3':
				kolvoballov += 5
			if anketa.kind_exp == 'profup3':
				kolvoballov += 10

			if anketa.sud == True:
				kolvoballov -= 10

			if anketa.exp_concurent == True:
				kolvoballov += 5

			if anketa.age < 20:
				kolvoballov -= 3
			if anketa.age > 45:
				kolvoballov -= 5

			if anketa.recomendacii == True:
				kolvoballov += 3

			if anketa.profdop == True:
				kolvoballov += 3

			if anketa.sredball == 3:
				kolvoballov += 3
			if anketa.sredball == 4:
				kolvoballov += 4
			if anketa.sredball == 5:
				kolvoballov += 5
			anketa.kollball = kolvoballov
			anketa.save()
			return redirect('/statistic/')
	else:
		form = StatForm()
	return render(request, 'index.html', {'form': form}) 

def show_ankets(request):
    return render( request, 'ankets.html', { 'anketaFields' : Stat.objects.all() } )

def delete_elem(request):
    Stat.objects.filter(id= request.GET.get("idelem") ).delete()
    return render( request, 'ankets.html', { 'anketaFields' : Stat.objects.all() } )  

def update_elem(request):
	#Получить ID из запроса
	idAnket = int( request.GET.get("id") )
		
	updateAnket = Stat.objects.get( id=idAnket )
	updateAnket.name = request.GET.get("name")
	updateAnket.sename = request.GET.get("sename")
	updateAnket.surname = request.GET.get("surname")
	if ( request.GET.get("sud") == "true"):
		updateAnket.sud = True
	else:
		updateAnket.sud = False
	
	obr = "no"
	if ( request.GET.get("obr") == "prof"):
		obr = request.GET.get("obr")
	if ( request.GET.get("obr") == "neprof"):
		obr = request.GET.get("obr")
	updateAnket.kind_obr = obr

	updateAnket.age = int( request.GET.get("age") )

	exp = "no"
	if ( request.GET.get("exp") == "prof1to3"):
		exp= request.GET.get("exp")
	if ( request.GET.get("exp") == "profup3"):
		exp = request.GET.get("exp")
	if ( request.GET.get("exp") == "neprof"):
		exp = request.GET.get("exp")
	updateAnket.kind_exp = exp

	if ( request.GET.get("concurent") == "true"):
		updateAnket.exp_concurent = True
	else:
		updateAnket.exp_concurent = False

	if ( request.GET.get("recom") == "true"):
		updateAnket.recomendacii = True
	else:
		updateAnket.recomendacii = False

	if ( request.GET.get("profdop") == "true"):
		updateAnket.profdop = True
	else:
		updateAnket.profdop = False

	updateAnket.sredball = int( request.GET.get("sredball") )


	kolvoballov = 0
	if updateAnket.kind_obr == 'no':
		kolvoballov -= 10
	if updateAnket.kind_obr == 'neprof':
		kolvoballov += 5
	if updateAnket.kind_obr == 'prof':
		kolvoballov += 10

	if updateAnket.kind_exp == 'no':
		kolvoballov -= 10
	if updateAnket.kind_exp == 'neprof':
		kolvoballov += 3
	if updateAnket.kind_exp == 'prof1to3':
		kolvoballov += 5
	if updateAnket.kind_exp == 'profup3':
		kolvoballov += 10

	if updateAnket.sud == True:
		kolvoballov -= 10

	if updateAnket.exp_concurent == True:
		kolvoballov += 5

	if updateAnket.age < 20:
		kolvoballov -= 3
	if updateAnket.age > 45:
		kolvoballov -= 5

	if updateAnket.recomendacii == True:
		kolvoballov += 3

	if updateAnket.profdop == True:
		kolvoballov += 3

	if updateAnket.sredball == 3:
		kolvoballov += 3
	if updateAnket.sredball == 4:
		kolvoballov += 4
	if updateAnket.sredball == 5:
		kolvoballov += 5

	updateAnket.kollball = kolvoballov

	updateAnket.save()

	return render( request, 'ankets.html', { 'anketaFields' : Stat.objects.all() } )

def delete_all(request):
    Stat.objects.all().delete()
    return render( request, 'ankets.html', { 'anketaFields' : Stat.objects.all() } )

def graph(request):

    return render( request, 'graph.html', { 'anketaFields' : Stat.objects.all() } )  

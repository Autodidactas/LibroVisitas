from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse
from .models import *
from .forms import *
import simplejson as json

def index(request):
	comentarios = Comentario.objects.all()
	ctx = {'comentarios':comentarios}
	return render_to_response('index.html', ctx)

def libro(request):
	comentarios = Comentario.objects.all()
	comentario_form = ComentarioForm()
	ctx = {'comentarios':comentarios, 'comentario_form':comentario_form}
	return render_to_response('libro.html', ctx)

@csrf_exempt
def nuevo_comentario(request):
	if request.method == "POST":
		comentario_form = ComentarioForm(request.POST)
		if comentario_form.is_valid():
			comentario = comentario_form.save()

		return HttpResponse(json.dumps({'autor':comentario.autor, 'comentario':comentario.comentario, 'cuenta_comentarios':Comentario.objects.all().count()}), mimetype='application/json')
	else:
		raise Http404
# coding: utf-8
from django.shortcuts import redirect

from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login, REDIRECT_FIELD_NAME
from django.http import HttpResponseRedirect
from www.forms import RegForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
#from www.models import Users, Rating, UserActivity, Categories, Tovar, Pictures, Comments, Bets
from www.models import Categories, Tovar, Bets





def main(request, cat='0'):
    cat = int(cat)
    cat_list = Categories.objects.all()
    usr='' # повідомлення про кривий логін. треба якось покращити
    #обрроблка форми логіну
   # bet = Bets.objects.filter(user = request.user)
    if 'RR' in  request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect ('/')
            else:
                usr = 'dasvados'
        else:
            usr = 'login invalid'

    #вивід списку категорій
    try:
        cat_id = Categories.objects.get(id__exact=cat)
    except Categories.DoesNotExist:
        tovar_list = Tovar.objects.all()
    else:
        tovar_list = Tovar.objects.filter(category_id=cat)



    if request.user.is_authenticated():
        bets = Bets.objects.filter(user = request.user)





    return TemplateResponse(request, 'main.html', {'tovar_list': tovar_list, 'cat_list':cat_list, 'err':usr, 'tovar_bets':bets})



def tovar(request, tovar_id='0'):
    usr=''
    cat_list = Categories.objects.all()
    if 'RR' in  request.POST:

        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                usr = 'dasvados'
        else:
            usr = 'login invalid'
  #   blocks(request)
    try:
        tovar_id = int(tovar_id)
        tovar_page = Tovar.objects.get(id=tovar_id)
        return TemplateResponse(request, 'tovar.html', {'tovar': tovar_page,'err':usr, 'cat_list':cat_list})
    except Tovar.DoesNotExist:
        return redirect('/')


def registration(request, template_name='registration.html',
            redirect_field_name=REDIRECT_FIELD_NAME,
            form_class=RegForm, extra_context=None,
            callback=None, autologin=True):

    redirect_to = request.REQUEST.get(redirect_field_name, '')

    form = form_class(request.POST or None)
    if form.is_valid():
        user = form.save()

        if autologin:
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            login(request, user)

        if callback:
            callback(request, user)

        return HttpResponseRedirect(redirect_to)

    context = {
        'form': form
    }
    context.update(extra_context or {})
    return TemplateResponse(request, template_name, context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse


from django.contrib import messages

from .forms import  CreateUserForm, UpdateUserForm


def login_view(request):
	if request.user.is_authenticated:
	    return redirect('bloghome')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('bloghome')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'account/login.html', context)

def register_view(request):
    if request.user.is_authenticated:
        return redirect('bloghome')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('account:login')
			

        context = {'form':form}
        return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('bloghome')

from django.contrib.auth.models import User

# @login_required(login_url='/account/login/')
@user_passes_test(lambda user: user.is_staff,login_url='/account/login/')
def dashboard_view(request):
    # user = get_user_model()
    allUsers= User.objects.values()
    template_name = 'account/dashboard.html'
    context = {'user_obj': allUsers}
    return render(request, template_name, context)


    # template_name = 'account/dashboard.html'
    # post = get_object_or_404(User, pk=pk)
    # form = UpdateUserForm(request.POST or None, request.FILES or None, instance=post)
    # if request.method == 'POST':
    #     form = UpdateUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # user = form.cleaned_data.get('username')
    #         messages.success(request, 'Profile updated successfully ' + user)

    #         return redirect(template_name)
        

    # context = {'form':form,'obj': title}
    # return render(request, 'account/userupdate.html', context)

def userupdate_view(request, pk):
    title = 'user update page'
    # template_name = 'account/dashboard.html'
    post = get_object_or_404(User, pk=pk)
    form = UpdateUserForm(request.POST or None, request.FILES or None, instance=post)
    # author = request.user
    # if request.method == "POST":
    if form.is_valid():
        print ("coming here")
        # form.instance.author = author
        form.save()
        # return redirect(template_name)
        return redirect (reverse('account:dashboard'))
    context = {
        'obj': title,
        'form': form
    }
    return render(request, 'account/userupdate.html', context)

# to get user logged in user permission
# delete this view in production
def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:

        username:     {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff:     {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active:    {request.user.is_active}
    """

    return HttpResponse(text, content_type="text/plain")

@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f"Hello {username}")
    messages.add_message(request, messages.WARNING, "You should login ass superuser")

    return HttpResponse("Messages added", content_type="text/plain")

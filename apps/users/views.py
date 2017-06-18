from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


from social_django.models import UserSocialAuth

from .forms import UserForm, UserUpdateForm


class CreateUser(SuccessMessageMixin, CreateView):
    """
    Create a new user
    """
    model = get_user_model()
    template_name = "users/user_new.html"
    form_class = UserForm
    success_url = reverse_lazy('tenant_login')
    success_message = "Su registro fue exitoso"
    # send_mail('welcome', ["dejuata@hotmail.com"], context={'Name': "Bob Marley"})


class EditUser(SuccessMessageMixin, UpdateView):
    """
    Edit user data
    """
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = "users/user_edit.html"
    success_url = '/'
    success_message = "Sus datos fueron actualizados con exito"

    def get_redirect_url(self):
        if 'pk' in self.request.GET:
            return reverse('usuario:usuario_edit', args=(self.request.GET['pk'],))
        else:
            raise Http404()

    def get(self, request, *args, **kwargs):
        user = request.user
        form_class = UserUpdateForm(instance=user)

        try:
            facebook_login = user.social_auth.get(provider='facebook')
        except UserSocialAuth.DoesNotExist:
            facebook_login = None

        try:
            twitter_login = user.social_auth.get(provider='twitter')
        except UserSocialAuth.DoesNotExist:
            twitter_login = None

        can_disconnect = (user.social_auth.count() > 1 )

        return render(request, "users/user_edit.html", {
            'form': form_class,
            'twitter_login': twitter_login,
            'facebook_login': facebook_login,
            'can_disconnect': can_disconnect
        })

    # def post(self, request, *args, **kwargs):
    #     pk = request.POST['pk']
    #     user = get_user_model().objects.get(pk=pk)
    #     user.save(update_fields=["email", 'first_name', 'last_name'])
    #     # form = UserUpdateForm(request.POST)
    #     # form.save()
    #     print(user)
    #     return render(request, "users/user_edit.html")


class ProfileUserTenant(TemplateView):
    """
    Shows user data
    """
    template_name = "users/user_tenant_profile.html"
    form_class = UserForm


def settings(request):
    user = request.user

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    can_disconnect = (user.social_auth.count() > 1 )

    return render(request, "users/user_edit.html", {
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })


def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse_lazy('usuario:usuario_settings'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, "users/user_password.html", {'form': form})

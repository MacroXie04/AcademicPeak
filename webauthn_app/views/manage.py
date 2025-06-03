from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from webauthn_app.models import PasskeyCredential
from django.shortcuts import render, redirect
from webauthn_app.forms.PasswordChangeForm import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


@method_decorator(login_required, name='dispatch')
class PasskeyListView(ListView):
    model = PasskeyCredential
    context_object_name = 'passkeys'
    template_name = 'manage/manage_passkeys.html'

    def get_queryset(self):
        return PasskeyCredential.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class PasskeyDeleteView(DeleteView):
    model = PasskeyCredential
    success_url = reverse_lazy('manage_passkeys')
    template_name = 'manage/delete_passkey.html'

    def get_queryset(self):
        return PasskeyCredential.objects.filter(user=self.request.user)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'manage/change_password.html', {'form': form})

@login_required
def manage_account(request):
    return render(request, 'manage/manage_account.html')
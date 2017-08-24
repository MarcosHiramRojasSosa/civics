from django.shortcuts import render
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from registration.views import ActivationView as BaseActivationView
from registration.models import RegistrationProfile
from registration import signals

from apps.models.models import City, Initiative, Event
from apps.models import categories


class Dashboard(View):
    """
    Get initiative profile

    """

    @method_decorator(login_required)
    def get(self, request):
        initiative = Initiative.objects.filter(user=request.user).first()
        if initiative:
            events      = Event.objects.filter(initiative=initiative).all()
            return render(request, 'users/dashboard.html', locals())

        return HttpResponseRedirect( reverse('modelforms:create_initiative') )


class DashboardStaff(View):
    """
    Get user profile

    """

    @method_decorator(staff_member_required)
    def get(self, request):
        initiatives = Initiative.objects.filter(user=request.user).order_by('name')
        if initiatives:
            events      = Event.objects.filter(initiative__in=initiatives).all()
            return render(request, 'users/dashboard-staff.html', locals())

        return HttpResponseRedirect( reverse('modelforms:create_initiative') )


class ActivationView(BaseActivationView):
    """
    Custom activation view that redirects user to Create Initiative form

    """

    registration_profile = RegistrationProfile

    def activate(self, *args, **kwargs):
        """
        Given an an activation key, look up and activate the user
        account corresponding to that key (if possible).

        After successful activation, the signal
        ``registration.signals.user_activated`` will be sent, with the
        newly activated ``User`` as the keyword argument ``user`` and
        the class of this backend as the sender.

        """
        activation_key = kwargs.get('activation_key', '')
        site = get_current_site(self.request)
        activated_user = (self.registration_profile.objects
                          .activate_user(activation_key, site))
        if activated_user:
            signals.user_activated.send(sender=self.__class__,
                                        user=activated_user,
                                        request=self.request)
        return activated_user

    def get_success_url(self, user):
        return ('modelforms:create_initiative', (), {})

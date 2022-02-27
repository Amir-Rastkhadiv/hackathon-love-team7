from django.shortcuts import render, get_object_or_404
from bottles.models import Letter, Reply
from .models import Profile

from .forms import ProfileForm

from django.views import generic


# Create your views here.

def profiles(request):
    """
    dlkcvjadl
    """
    model = Profile
    profile = get_object_or_404(Profile, user=request.user)

    form = ProfileForm(instance=profile)


    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, template, context)


class inbox(generic.ListView):
    """
    docstring
    """
    model = Letter

    template_name = "profiles/inbox.html"

    def get_context_data(self, **kwargs):
        context = super(inbox, self).get_context_data(**kwargs)
        user_letter_list = Letter.objects.filter(author=self.request.user)
        unreplied_letters = user_letter_list.filter(has_reply=False)
        letter_with_unseen_reply = user_letter_list.filter(has_unseen_reply=True)
        letter_with_seen_reply = user_letter_list.filter(has_unseen_reply=False).filter(has_reply=True)
        user_reply_list = Reply.objects.filter(name=self.request.user)
        # user_reply_list
        context['unreplied_letters'] = unreplied_letters
        context['letter_with_unseen_reply'] = letter_with_unseen_reply
        context['letter_with_seen_reply'] = letter_with_seen_reply
        context['replys'] = user_reply_list
        return context 


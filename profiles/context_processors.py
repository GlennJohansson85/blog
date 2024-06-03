# profiles/context_processors.py
from .models import Profile, Friendship

def profile_context(request):
    profile_picture_url = None
    friends = []

    if request.user.is_authenticated:
        try:
            profile_picture_url = request.user.profile_picture.url if request.user.profile_picture else None
            friends = Friendship.objects.filter(user_email=request.user.email).select_related('friend')
        except Profile.DoesNotExist:
            # If Profile doesn't exist
            pass

    return {
        'profile_picture_url': profile_picture_url,
        'friends': friends
    }
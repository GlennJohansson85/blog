from .models import UserProfile

def profile_picture(request):
    profile_picture_url = None
    if request.user.is_authenticated:
        try:
            user_profile = request.user.userprofile
            profile_picture_url = user_profile.profile_picture.url if user_profile.profile_picture else None
        except UserProfile.DoesNotExist:
            # If UserProfile doesn't exist, handle it gracefully
            pass

    return {'profile_picture_url': profile_picture_url}
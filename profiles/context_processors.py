from .models import Profile

def profile_picture(request):
    profile_picture_url = None
    if request.user.is_authenticated:
        try:
            profile_picture_url = request.user.profile_picture.url if request.user.profile_picture else None
        except Profile.DoesNotExist:
            # If Profile doesn't exist, handle it gracefully
            pass

    return {'profile_picture_url': profile_picture_url}
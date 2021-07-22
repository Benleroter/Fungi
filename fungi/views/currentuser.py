def CurrentUser(request):
        currentuser = Show.objects.get(user_id= request.user)

        return currentuser
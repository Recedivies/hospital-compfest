from django.shortcuts import redirect

def admin_only(view_func):
  def wrapper_func(request, *args, **kwargs):
    if request.user.is_superuser:
      return view_func(request, *args, **kwargs)
    else:
      return redirect('account:logged_in')
  return wrapper_func

def user_only(view_func):
  def wrapper_func(request, *args, **kwargs):
    if not request.user.is_superuser:
      return view_func(request, *args, **kwargs)
    else:
      return redirect('account:dashboard')
  return wrapper_func
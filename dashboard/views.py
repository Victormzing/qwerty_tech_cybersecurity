from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import AdminLog, Inquiry
from blog.models import BlogPost
from django.contrib.auth.models import User


def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    total_users = User.objects.count()
    total_posts = BlogPost.objects.count()
    total_inquiries = Inquiry.objects.count()
    recent_logs = AdminLog.objects.order_by('-timestamp')[:5]
    
    context = {
        "total_users": total_users,
        "total_posts": total_posts,
        "total_inquiries": total_inquiries,
        "recent_logs": recent_logs,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)

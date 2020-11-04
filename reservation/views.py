from donation.models import ResourcePost
from .models import ReservationPost
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "reservation/reservation_home.html")


class PostListView(ListView):
    # Basic list view
    model = ResourcePost
    # Assign tempalte otherwise it would look for post_list.html
    # as default template
    template_name = "reservation/reservation_home.html"

    # Set context_attribute to post object
    context_object_name = "posts"

    # Add ordering attribute to put most recent post to top
    ordering = ["-date_created"]

    # filters = {'status':'AVAILABLE'}

    # Add pagination
    paginate_by = 5


class ReservationPostListView(ListView):
    # Basic list view
    model = ReservationPost
    # Assign tempalte otherwise it would look for post_list.html
    # as default template
    template_name = "reservation/reservation_list.html"

    # Set context_attribute to post object
    context_object_name = "posts"

    # Add ordering attribute to put most recent post to top
    ordering = ["-date_created"]

    # Add pagination
    paginate_by = 5


def confirmation(request):
    return render(request, "reservation/reservation_confirmation.html")


def reservation_function(request, id):
    if request.method == "POST":
        selected_timeslot = request.POST.get("dropoff_time")
        resource_post = ResourcePost.objects.get(id=id)
        if selected_timeslot == "1":
            selected_time = resource_post.dropoff_time_1
        elif selected_timeslot == "2":
            selected_time = resource_post.dropoff_time_2
        elif selected_timeslot == "3":
            selected_time = resource_post.dropoff_time_3
        donor_id = User.objects.get(id=resource_post.donor_id)
        helpseeker_id = request.user
        reservation = ReservationPost(
            dropoff_time_request=selected_time,
            post=resource_post,
            donor=donor_id,
            helpseeker=helpseeker_id,
        )
        reservation.save()
        resource_post.status = "PENDING"
        resource_post.save()
    return redirect("reservation:reservation-confirmation")


# Reservation Detail View


class PostDetailView(DetailView):
    # Basic detail view
    model = ResourcePost
    template_name = "reservation/reservation_request.html"

class ReservationDetailView(DetailView):
    # Basic detail view
    model = ReservationPost
    template_name = "reservation/reservation_detail.html"
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from donation.models import ResourcePost

# from places.fields import PlacesField
from django.urls import reverse
from django.db.models.signals import post_save


# Create your models here.
class ReservationPost(models.Model):

    dropoff_time_request = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(ResourcePost, on_delete=models.CASCADE)
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="donor_id")
    helpseeker = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="helpseeker_id"
    )

    # TODO: generate reservation ID token as primary key?
    # TODO: return reservation ID in __str__
    # def __str__(self):
    # return self.title

    def give_notifications(sender, instance, *args, **kwargs):
        reservationpost = instance
        reservepost = reservationpost.post
        helpseker = reservationpost.helpseeker
        notify = Notification(
            post=reservationpost, sender=helpseker, receiver=reservepost.donor
        )
        notify.save()

    # Reverse would return the full url as a string and
    # let the view redirect for us

    def get_absolute_url(self):
        # return the path of the specific post
        return reverse("reservation-detail", kwargs={"pk": self.pk})


class Notification(models.Model):
    NOTIFICATION_STATUS = ((1, "ACCEPT"), (2, "REJECT"), (3, "PENDING"))

    post = models.ForeignKey(
        ReservationPost,
        on_delete=models.CASCADE,
        related_name="noti_post",
        blank=True,
        null=True,
    )
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="noti_from_user"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="noti_to_user"
    )
    notificationstatus = models.IntegerField(
        choices=NOTIFICATION_STATUS, default=NOTIFICATION_STATUS[2][0]
    )
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    """def get_unseen_messages_status(self):
        notifications = Notification.objects.all()
        for notification in notifications:
            if notification.is_seen==False:
                return True
        return False"""


post_save.connect(ReservationPost.give_notifications, sender=ReservationPost)

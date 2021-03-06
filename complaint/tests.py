from django.test import TestCase
from django.urls import reverse
from complaint.apps import ComplaintConfig
from complaint.models import Complaint
from django.utils import timezone


class ComplaintConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(ComplaintConfig.name, "complaint")


class ComplaintViewTests(TestCase):
    def test_map_view_works(self):
        response = self.client.get(reverse("issue-complaint"))
        self.assertEqual(response.status_code, 200)

    def test_right_complaint_post_request(self):
        holder = self.client.post(
            reverse("issue-complaint"),
            data={
                "subject": "Subject1",
                "message": "I have a problem",
                "image": "",
            },
        )
        self.assertEqual(holder.status_code, 200)


class ComplaintModelTests(TestCase):
    def test_complaint_contains_correct_info(self):
        test_complaint_1 = Complaint(
            subject="I hate math",
            message="I hate math",
            uploaded_at=timezone.now(),
            image=None,
        )
        test_complaint_1.save()

        response = self.client.get(reverse("issue-complaint"))
        self.assertEqual(response.status_code, 200)

    def test_complaint_contains_no_data(self):
        form = Complaint()
        self.assertFalse(form.save())

    def test_complaint_contains_wrong_message_data(self):
        form = Complaint(
            subject="hi all,",
            message="",
            uploaded_at=timezone.now(),
            image=None,
        )
        self.assertFalse(form.save())

    def test_complaint_contains_wrong_subject_data(self):
        form = Complaint(
            subject="",
            message="yippie",
            uploaded_at=timezone.now(),
            image=None,
        )
        self.assertFalse(form.save())

    def test_complaint_contains_without_subject_message_data(self):
        form = Complaint(
            uploaded_at=timezone.now(),
            image=None,
        )
        self.assertFalse(form.save())

    def test_complaint_contains_without_image(self):
        form = Complaint(
            subject="hi all,",
            message="yippie",
            uploaded_at=timezone.now(),
        )
        self.assertFalse(form.save())

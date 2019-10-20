# -*- coding: utf8 -*-
import json
from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase


class TagsTestCase(APITestCase):
    def setUp(self):
        self.user = mommy.make("User")
        self.book = mommy.make("shelves.Book")
        self.client.force_login(self.user)

    def test_setting_book_tags(self):
        response = self.client.post(
            reverse("book-tags-list", kwargs={"book_id": self.book.id}),
            data=json.dumps({"tags": ["tag1", "tag2"]}),
            content_type="application/json",
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_setting_book_tags_twice_with_same_data_does_not_duplicate(self):
        response = self.client.post(
            reverse("book-tags-list", kwargs={"book_id": self.book.id}),
            data=json.dumps({"tags": ["tag1", "tag2"]}),
            content_type="application/json",
        )
        self.book.refresh_from_db()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.book.tags.count(), 2)
        response = self.client.post(
            reverse("book-tags-list", kwargs={"book_id": self.book.id}),
            data=json.dumps({"tags": ["tag1", "tag2"]}),
            content_type="application/json",
        )
        self.book.refresh_from_db()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.book.tags.count(), 2)

    def test_deleting_tag(self):
        response = self.client.post(
            reverse("book-tags-list", kwargs={"book_id": self.book.id}),
            data=json.dumps({"tags": ["tag1", "tag2"]}),
            content_type="application/json",
        )
        self.book.refresh_from_db()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        response = self.client.delete(
            reverse("book-tags-detail", kwargs={"book_id": self.book.id, "text": "tag2"})
        )
        self.book.refresh_from_db()
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(self.book.tags.count(), 1)
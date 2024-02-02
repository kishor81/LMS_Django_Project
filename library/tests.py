from django.test import TestCase

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Book, BookDetails, BorrowedBooks

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def create_book(self):
        return Book.objects.create(
            Title='Test Book',
            ISBN='1234567890123',
            PublishedDate='2024-02-01',
            Genre='Fiction'
        )

    def create_user(self):
        return User.objects.create(
            username='testuser2',
            password='testpassword2',
            email='testuser2@example.com',
            MembershipDate='2024-02-01'
        )

    def test_create_user(self):
        url = '/api/create-user/'
        data = {'Name': 'John Doe', 'Email': 'john.doe@example.com', 'MembershipDate': '2022-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_all_users(self):
        url = '/api/list-all-users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_by_id(self):
        user = self.create_user()
        url = f'/api/get-user-by-id/{user.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_new_book(self):
        url = '/api/add-new-book/'
        data = {'Title': 'New Book', 'ISBN': '9876543210987', 'PublishedDate': '2023-01-01', 'Genre': 'Non-Fiction'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_all_books(self):
        url = '/api/list-all-books/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_by_id(self):
        book = self.create_book()
        url = f'/api/get-book-by-id/{book.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        self.client.logout()


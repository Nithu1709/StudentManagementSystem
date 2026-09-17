
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Student


class StudentAPITests(APITestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name='Asha',
            last_name='Menon',
            email='asha.menon@example.com',
            phone='9876543210',
            course='CSE',
            enrollment_date='2024-06-01',
            gpa=8.5,
        )
        self.list_url = '/api/students/'
        self.detail_url = f'/api/students/{self.student.id}/'

    def test_create_student_valid(self):
        payload = {
            'first_name': 'Rahul',
            'last_name': 'Verma',
            'email': 'rahul.verma@example.com',
            'phone': '9123456780',
            'course': 'IT',
            'enrollment_date': '2024-07-15',
            'gpa': 7.9,
        }
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)

    def test_create_student_missing_required_field(self):
        payload = {'first_name': 'NoEmail'}
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_student_duplicate_email(self):
        payload = {
            'first_name': 'Dup',
            'last_name': 'Licate',
            'email': self.student.email,
            'enrollment_date': '2024-07-15',
        }
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_read_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_single_valid(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.student.email)

    def test_read_single_invalid_id(self):
        response = self.client.get('/api/students/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_valid(self):
        response = self.client.patch(self.detail_url, {'gpa': 9.1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(str(self.student.gpa), '9.10')

    def test_update_invalid_id(self):
        response = self.client.patch('/api/students/9999/', {'gpa': 5.0}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_valid(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 0)

    def test_delete_invalid_id(self):
        response = self.client.delete('/api/students/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_search_filter(self):
        response = self.client.get(self.list_url, {'search': 'Asha'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

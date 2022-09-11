import pytest
from django.contrib.auth.models import User


@pytest.fixture
def sample_q_user(db):
    return User.objects.create_user(
        username='SampleUser',
        email='sample@email.com',
        password='password',
        first_name='FirstName',
        last_name='LastName'
    )
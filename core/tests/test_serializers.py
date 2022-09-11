import pytest
from core.serializers import (
    UserSerializer
)

@pytest.mark.django_db
def test_user_serializer(sample_q_user):
    serializer = UserSerializer(sample_q_user)

    assert 'id' in serializer.data
    assert serializer.data.get('id') == sample_q_user.id
    assert 'username' in serializer.data
    assert serializer.data.get('username') == sample_q_user.username
    assert 'email' in serializer.data
    assert serializer.data.get('email') == sample_q_user.email
    assert 'password' in serializer.data
    assert serializer.data.get('password') == sample_q_user.password
    assert 'first_name' in serializer.data
    assert serializer.data.get('first_name') == sample_q_user.first_name
    assert 'last_name' in serializer.data
    assert serializer.data.get('last_name') == sample_q_user.last_name
    assert 'user_fullname' in serializer.data
    assert serializer.data.get('user_fullname') == sample_q_user.get_full_name()
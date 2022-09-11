import pytest
from rest_framework.test import APIRequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from core.views import (
    LoginView,
    LogoutView
)


@pytest.mark.django_db
def test_login_get_logged_in_user_view(sample_q_user):
    """Test login return logged in user , response status code 200 ok."""
    factory = APIRequestFactory()
    view = LoginView.as_view()
    request = factory.get('auth/login/')
    request.user = sample_q_user
    response = view(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_view(sample_q_user):
    """Test login view, response status code 200 ok."""
    factory = APIRequestFactory()
    session_middleware = SessionMiddleware(factory)
    view = LoginView.as_view()
    request = factory.post('auth/login/', {
        'username': sample_q_user.username,
        'password': 'password'
    })
    session_middleware.process_request(request)
    request.session.save()
    response = view(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_no_user_view():
    """Test login view no user case, response status code 400 bad request."""
    factory = APIRequestFactory()
    session_middleware = SessionMiddleware(factory)
    view = LoginView.as_view()
    request = factory.post('auth/login/', {
        'username': 'name',
        'password': 'password'
    })
    session_middleware.process_request(request)
    request.session.save()
    response = view(request)

    assert response.status_code == 400


@pytest.mark.django_db
def test_login_wrong_pass_view(sample_q_user):
    """Test login view, response status code 200 ok."""
    factory = APIRequestFactory()
    session_middleware = SessionMiddleware(factory)
    view = LoginView.as_view()
    request = factory.post('auth/login/', {
        'username': sample_q_user.username,
        'password': 'passwordsd'
    })
    session_middleware.process_request(request)
    request.session.save()
    response = view(request)

    assert response.status_code == 400


@pytest.mark.django_db
def test_logout_view(sample_q_user):
    """Test logout view, response status code 200 ok."""
    factory = APIRequestFactory()
    session_middleware = SessionMiddleware(factory)
    message = 'Logged out.'
    view = LogoutView.as_view()
    request = factory.post('auth/logout/')
    request.user = sample_q_user
    session_middleware.process_request(request)
    request.session.save()
    response = view(request)

    assert response.status_code == 200
    assert response.data.get('message') == message
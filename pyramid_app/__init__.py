from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid.security import Authenticated, Allow, authenticated_userid
from sqlalchemy import engine_from_config
from .models import DBSession, Base, User, UserSearch


class Factory(object):
    __acl__ = [
        (Allow, Authenticated, 'view')
    ]

    def __init__(self, request):
        pass

def get_user(request):
    user_id = authenticated_userid(request)
    if user_id is not None:
        return DBSession.query(User).filter(User.id == user_id).first()

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    authn_policy = AuthTktAuthenticationPolicy('sosecret')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(
        settings=settings,
        root_factory = Factory
    )
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('search','/search')
    config.add_route('history', '/history')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('register', '/register')
    config.add_route('user_list', '/user_list')
    config.add_route('top_search', '/top_search')
    config.add_route('jsonview', '/json')
    config.add_request_method(get_user, 'user', reify = True)
    config.scan()
    return config.make_wsgi_app()

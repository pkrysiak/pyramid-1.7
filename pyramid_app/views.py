from datetime import datetime, timedelta
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from allegro.lib import allegro_api, NoItemException as AllegroNoItemEx
from nokaut.lib import nokaut_api, NoItemException as NokautNoItemEx
from forms import RegisterForm, LoginForm
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from sqlalchemy import desc
from .models import DBSession, User, UserSearch
from pyramid.security import remember, forget,authenticated_userid, NO_PERMISSION_REQUIRED

@view_config(
    route_name='home',
    renderer='pyramid_app:templates/search_box.mako'
)
def my_view(request):
    return {}


@view_config(
    route_name = 'search',
    renderer = 'pyramid_app:templates/search.mako',
    permission = 'view'

)
def result_view(request):

    def search():
        try :
            all_link, all_price = allegro_api(search_phrase)
        except AllegroNoItemEx:
            all_link, all_price = None, None

        try:
            nok_link, nok_price = nokaut_api(search_phrase, nokaut_key)
        except NokautNoItemEx:
            nok_link, nok_price = None, None

        return all_link, all_price, nok_link, nok_price

    search_phrase = request.GET.get('search_field')
    nokaut_key = request.registry.settings.get('nokaut.key')
    user = request.user

    data = DBSession.query(UserSearch)\
                    .filter(UserSearch.search_id == user.id)\
                    .filter(UserSearch.search_content == search_phrase).first()

    if data is not None:
        if data.last_update < (datetime.today() - timedelta(days=2)):
            data.all_link, data.all_price, data.nok_link, data.nok_price = search()

        data.search_quantity += 1
        DBSession.flush()
        return {
            'data' : data
        }
    else:
        all_link, all_price, nok_link, nok_price = search()

        data = UserSearch(
            search_id = user.id,
            search_content = search_phrase,
            all_link = all_link,
            all_price = all_price or 0,
            nok_link = nok_link,
            nok_price = nok_price or 0,
            search_quantity = 1
        )
        DBSession.add(data)
        DBSession.flush()


    return {
        'data' : data
    }


@view_config(
    route_name = 'history',
    renderer = 'pyramid_app:templates/history.mako',
    permission = 'view'
)

def history_view(request):
    user_id =  authenticated_userid(request)
    user_hist = DBSession.query(UserSearch)\
                         .filter(UserSearch.search_id == user_id).all()
    return {
        'user_hist': user_hist
    }


@view_config(route_name = 'top_search',
             renderer = 'pyramid_app:templates/top.mako',
             permission = 'view')
def top_search_view(request):
    top_search = DBSession.query(UserSearch)\
                          .order_by(desc(UserSearch.search_quantity)).limit(3)

    return {
        'top_search' : top_search
    }


@view_config(
    route_name = 'login',
    renderer = 'pyramid_app:templates/login.mako',
    permission = NO_PERMISSION_REQUIRED
)
def login_view(request):

    form = Form(request, schema = LoginForm)

    if request.method == 'POST' and form.validate():
        user = DBSession.query(User)\
                        .filter(User.username == form.data['login'])\
                        .filter(User.password == form.data['password']).first()

        headers = remember(request, user.id)
        return HTTPFound(location = '/', headers = headers)
    else:
        return {
            'render' : FormRenderer(form)
        }


@view_config(
    route_name = 'logout',
    renderer = 'pyramid_app:templates/base.mako'
)
def logut_view(request):
    headers = forget(request)
    return HTTPFound(
        location = '/', headers = headers
    )


@view_config(
    route_name = 'register',
    renderer = 'pyramid_app:templates/register.mako',
    permission = NO_PERMISSION_REQUIRED
)
def register_view(request):
    login = request.POST.get('login')

    form = Form(request,
                    schema = RegisterForm)

    if request.method == 'POST' and form.validate():
        new_user = User(
            username = form.data['login'],
            password = form.data['password'],
            group = 'viewer'
        )
        DBSession.add(new_user)
        user_id = DBSession.query(User).\
                    filter(User.username == new_user.username).first().id
        headers = remember(request, user_id)

        return  HTTPFound('/', headers = headers)
    else:
        return {
            'render' : FormRenderer(form)
        }

@view_config(
    route_name = 'jsonview',
    renderer = 'json',
)
def json_view(request):
    object_state = result_view(request)['data'].__dict__
    return {str(k) : str(v) for k, v in object_state.items()}


@view_config(
    route_name = 'user_list',
    renderer = 'pyramid_app:templates/user_list.mako'
)
def user_list_view(request):
    """ ZROBIONE TYLKO W CELU PODGLADU ..
    """
    users = DBSession.query(User).all()
    history = DBSession.query(UserSearch).all()

    return {
        'users': users,
        'history': history
    }
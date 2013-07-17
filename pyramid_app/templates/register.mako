
<%inherit file="base.mako"/>

<%block name="login_form">
    <div class="form_login">
        <div class="head_login">Register</div>
        ${render.errorlist()}
        <form id="reg_form" method="post" action="/register">
            <input class="input_text" type="text" name="login" value="login"/>
            <input class="input_text" type="password" name="password" value="password"/>
            <input class="input_text" type="password" name="confirm_password" value="password"/>
            <button class="btn btn-primary" type=submit>Register</button>
        </form>
    </div>
</%block>
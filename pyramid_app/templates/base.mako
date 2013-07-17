<!DOCTYPE HTML>
<html>
<head>
    <title></title>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="${request.static_url('pyramid_app:static/css/style.css')}">
</head>
<body>
    <div id="container">
        <div class="main_box">
            <div class="head">
                <div class="logo_img"><a href = "/"><img src="${request.static_url('pyramid_app:static/img/logo.png')}" alt="logo"/></a></div>
                <div class="logo_txt">
                    Compare products
                    <div class="logo_txt_small">We will help you find and compare products</div>
                </div>
                <div class="box_login">
                    % if not request.user:
                        <a class="btn btn-success" href="/register">Register</a>
                        <a class="btn" href="/login">Login</a>
                    %else:
                        <a class="btn" href="/logout">Logout</a>
                    %endif
                </div>
            </div>
            <div class="middle">
                <%block name="search_box"> </%block>
                <%block name="login_form"> </%block>
                <%block name="content"> </%block>
            </div>
        </div>
        <div class="footer">
            <img src="${request.static_url('pyramid_app:static/img/logo_stx.png')}" alt="logo_stx"/>
        </div>
    </div>
    <script src="${request.static_url("pyramid_app:static/js/jquery-1.8.3.min.js")}"></script>
    <script type="text/javascript">

    $(document).ready(function() {

        $('.more > button').click(function() {
            var tr = $(this).closest('tr');
            var $search =  tr.find('.name_list');
            var $all_price = tr.find($('td[name="all_price"]'));
            var $nok_price = tr.find($('td[name="nok_price"]'));
            var $last_update = tr.find($('td[name="last_update"]'));
            var $hits = tr.find($('td[name="hits"]'));
            var $all_link = tr.find('a[name="all_link"]');
            var $nok_link = tr.find('a[name="nok_link"]');
            var button = $(this);
            waiting(button);

           $.getJSON('/json?search_field='+ $search.text() , function(data){
              if (data.allegro_price == null){
                    data.allegro_price = '0.0';
              }
              if (data.nokaut_price == null){
                  data.nokaut_price = '0.0';
              }
              $all_price.text(data.allegro_price);
              $nok_price.text(data.nokaut_price);
              $all_link.attr('href', data.allegro_link);
              $nok_link.attr('href', data.nokaut_link);
              $last_update.text(data.last_update);
              $hits.text(data.search_quantity);

           }).done(function() { done(button); })
             .fail(function() { alert('Refreshing failed..'); });

        function waiting(obj){
            $(obj).hide();
            $(obj).parent().addClass('spinner');
        }

        function done(obj){
            $(obj).show()
            $(obj).parent().removeClass('spinner');
        }

        });
    });

    </script>
</body>
</html>
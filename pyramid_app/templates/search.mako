
<%inherit file="base.mako"/>

<%block name = "content">
    <div class="main_box_left">
        <div class="name_product">
            Product name: ${data.search_content}
            % if data.all_link is None and data.nok_link is None:
                <p id="upper_space"> No such item... </p>
            %else:
                <p id="upper_space"> Links:</p>
                <p id="upper_space"><a class="no_decoration" href = "${data.all_link or '#'}" > ${data.all_link or 'No such item in allegro..'} </a></p>
                <p id="upper_space"><a class="no_decoration" href = "${data.nok_link or '#'}" > ${data.nok_link or 'No such item in nokaut..'} </a></p>
                <p id="upper_space"> Thumb:</p>
                <p id="upper_space">
                <a href="${request.static_url(all_img)}" data-lightbox="${data.search_content}"><img src="${request.static_url(thumb)}"/></a>
                <a href="${request.static_url(nok_img)}" data-lightbox="${data.search_content}"></a>
                </p>
            % endif
        </div>
        <div class="box_photo">
            <p style="margin-top:250px"> <br></p>
       <!--     <img src="${request.static_url('pyramid_app:static/img/img_demo.jpg')}" alt="img_demo"/>-->
        </div>
    </div>
    <div class="main_box_right">
        <div class="compare_box">
            <img src="${request.static_url('pyramid_app:static/img/logo_allegro.png')}" alt="logo_allegro"/>
            <div class="price ${'win' if data.all_price < data.nok_price else ''}">${data.all_price}</div>
        </div>
        <div class="compare_box">
            <img src="${request.static_url('pyramid_app:static/img/logo_nokaut.png')}" alt="logo_nokaut"/>
            <div class="price ${'win' if data.nok_price < data.all_price else ''}">${data.nok_price}</div>
        </div>
    </div>
</%block>
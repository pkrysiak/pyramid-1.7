
<!-- zrobione tylko w celu podgladu .. -->

<%inherit file="base.mako"/>

<%block name = "content">
    <table cellpadding="0" celllspacing="0" border="0" class="list">
            %for user in users:
                <tr>
                    <td class="thumb"><!-- <img src="http://image.ceneo.pl/data/products/19719012/f-asus-x501a-xx145h.jpg" alt="img_demo"/> --></td>
                    <td class="name_list">${user.id}, ${user.username}, ${user.password}, ${user.group}</td>
                    <td class="price_list"></td>
                    <!-- <td class="more"><a href="#" class="link_more btn"></a></td> -->
                </tr>
            %endfor
            <tr><td><p style="color: red"> HISTORY</p></td></tr>
            %for record in history:
                <tr>
                    <td class="thumb"><!-- <img src="http://image.ceneo.pl/data/products/19719012/f-asus-x501a-xx145h.jpg" alt="img_demo"/> --></td>
                    <td class="name_list">${record.search_id}, ${record.search_content}, ${record.all_link},
                                          ${record.all_price}, ${record.nok_link}, ${record.nok_price}, ${record.search_quantity}</td>
                    <td class="price_list"></td>
                    <!-- <td class="more"><a href="#" class="link_more btn"></a></td> -->
                </tr>

            %endfor
    </table>
</%block>
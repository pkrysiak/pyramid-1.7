
<%inherit file="base.mako"/>

<%block name = "content">

    <p class="name_product" style="margin-top: 15px"> Top 3 searched products: </p>
    <table cellpadding="0" celllspacing="0" border="0" class="list">
            %for search in top_search:
                <tr>
                    <td class="thumb"><!-- <img src="http://image.ceneo.pl/data/products/19719012/f-asus-x501a-xx145h.jpg" alt="img_demo"/> --></td>
                    <td class="name_list">${search.search_content}</td>
                    <td class="name_list">${search.search_quantity} times.</td>
                </tr>
            %endfor
    </table>
</%block>
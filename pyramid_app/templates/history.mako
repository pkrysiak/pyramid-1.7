
<%inherit file="base.mako"/>

<%block name = "content">
    <table cellpadding="0" celllspacing="0" border="0" class="list">
            <tr>
                <td class="name_list1"> Search phrase: </td>
                <td class="name_list1"> allegro price: </td>
                <td class="name_list1"> nokaut price:</td>
                <td class="name_list1"> updated: </td>
                <td class="name_list1"> hits: </td>
                <td class="name_list1"> Link Allegro: </td>
                <td class="name_list1"> Link Nokaut: </td>
                <td class="name_list1"> &nbsp </td>
            </tr>
            %for hist in user_hist:
                <tr id="history_row">
                    <td class="name_list" name="search_content">${hist.search_content}</td>
                    <td class="price_list" name="all_price"> ${hist.all_price} </td>
                    <td class="price_list" name="nok_price"> ${hist.nok_price} </td>
                    <td class="price_list" name="last_update"> ${hist.last_update_str}</td>
                    <td class="price_list" name="hits"> ${hist.search_quantity}</td>
                    <td class="more"><a href="${hist.all_link}" name="all_link">Link Allegro</a></td>
                    <td class="more"><a href="${hist.nok_link}" name="nok_link">Link Nokaut</a></td>
                    <td class="more"> <button id="refresh"> refresh </button> </td>
                </tr>
            %endfor
    </table>
</%block>
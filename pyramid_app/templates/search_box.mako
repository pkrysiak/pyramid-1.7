
<%inherit file="base.mako"/>

<%block name="search_box">
    <div class="box_search">
            <form action="/search">
                <div class="search">
                    <input id="input_field" type="text" name="search_field" value="enter a product name"/>
                </div>
                <button class="btn_search btn btn-primary" type="submit">Search</button>
            </form>
            <a class="btn" href="/top_search">Top 3 searched</a>
            % if request.user:
                <a class="btn" href="/history">History</a>
            % endif
            <div class="clear"></div>
    </div>
</%block>
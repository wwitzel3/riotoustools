<%def name="avatar(request)">
<%
    from riotoustools.lib import gravatar
%>
<div class="avatar">
    <img src="${gravatar.get_url_from_email(request)}" width="100px" height="100px" />
    % if owner:
    <a href="http://gravatar.com">change me</a>
    % endif
</div>
</%def>
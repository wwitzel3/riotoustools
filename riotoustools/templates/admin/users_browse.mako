<%inherit file="../base.mako"/>

<div id="center-content">
<h3>Select a user to edit.</h3>
<ul>
    % for u in request.context:
    <li><a href="${request.resource_url(u)}">(${u.id}) ${u.email}</a></li>
    % endfor
</ul>

</div>
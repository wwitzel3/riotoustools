<%inherit file="base.mako"/>

<div id="center-content">
% if request.user:
<h3>Edit your own!</h3>
<p><a href="#">Click here to start editing your own 101 in 1001 list right now!</p>
% else:
<p><a href="#">Signup to create your own list!</a></p>
% endif

<h3>Click a list to view it!</h3>
<ul>
    % for l in request.context:
    <li><a href="${request.resource_url(l)}">${l.name}</a></li>
    % endfor
</ul>

</div>
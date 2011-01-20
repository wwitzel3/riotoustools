<%inherit file="base.mako"/>

<div id="center-content">
<h3>Edit your own!</h3>
<p><a href="/dayzero/${user.lists[0].id}">Click here to start editing your own 101 in 1001 list right now!</p>

<h3>Click a list to view it!</h3>
<ul>
    % for l in dayzero_lists:
    <li><a href="/dayzero/${l.id}">${l.name}</a></li>
    % endfor
</ul>

</div>
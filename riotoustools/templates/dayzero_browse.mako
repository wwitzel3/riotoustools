<%inherit file="base.mako"/>

<div id="center-content"> 
<h3>Click a list to view it!</h3>
<ul>
    % for l in dayzero_lists:
    <li><a href="/dayzero/${l.id}">${l.name}</a></li>
    % endfor
</ul>

</div>
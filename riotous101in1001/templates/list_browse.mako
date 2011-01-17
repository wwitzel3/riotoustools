<%inherit file="base.mako"/>

<div id="center-content"> 
<h3>Click a list to view it!</h3>
<ul>
    % for l in lists:
    <li><a href="/list/${l.id}">${l.name}</a></li>
    % endfor
</ul>

</div>
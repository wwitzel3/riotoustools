<%inherit file="../base.mako"/>

<div id="center-content">
<h3>Click a calendar to view it!</h3>
<ul>
    % for l in lifecal_list:
    <li><a href="/lifecal/${l.id}">${l.id}</a></li>
    % endfor
</ul>

</div>
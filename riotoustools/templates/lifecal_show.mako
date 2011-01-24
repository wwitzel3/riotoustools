<%inherit file="base.mako"/>

<div id="center-content">
${calendar}
</div>

<%def name='head_js()'>
<script type="text/javascript" src="/static/lifecal.js"></script>
</%def>

<%def name='head_css()'>
<link href="/static/lifecal.css" rel="stylesheet" type="text/css" /> 
<link href="/static/calendar.css" rel="stylesheet" type="text/css" />
</%def>
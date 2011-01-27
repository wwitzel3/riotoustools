<%inherit file="base.mako"/>

<div id="center-content"> 
<div class="day-zero-list-info">
<fieldset>
<ol>
<li>
    <label class="day-zero-label">Owner:</label>
    <p class="inline-block day-zero-info-owner">${owner_name()}</p>
</li>
<li>    
    <label class="day-zero-label">Name:</label>
    <p class="inline-block day-zero-item-text ${'editable' if owner else ''}">${request.context.name}</p>
</li>
<li>
    <label class="day-zero-label">Start Date:</label>
    <p class="inline-block ${'editable' if owner else ''}">${request.context.start_at.strftime('%Y.%m.%d')}</p>
</li>
<li>
    <label class="day-zero-label">Finish Date:</label>
    <p class="inline-block ${'editable' if owner else ''}">${request.context.end_at.strftime('%Y.%m.%d')}</p>
</li>
</ol>
</fieldset>
</div>

% if request.context.user == request.user:
    <input type="hidden" name="day-zero-item-add-action" value="${request.resource_url(request.context)}add" />
% endif

<ol id="day-zero-list" start="${0 if owner else 1}">
    % if owner:
    <li class="hover new"><span class="notice">Click here to add a new item</span></li>
    % endif
    
    % for i, item in enumerate(request.context.items):
    <li class="day-zero-item">
        <div class="day-zero-item-container">
            <form class="inline-block" name="day-zero-item-form" action="${request.resource_url(request.context)}">
            <input type="hidden" name="completed" value="${item.completed}" />
            <input type="hidden" name="item_id" value="${item.id}" />
            <p class="day-zero-item-text ${'editable' if request.context.user == request.user else ''} ${'item-complete' if item.completed else ''}">${item.description}</p>
            <div class="day-zero-item-buttons">
                % if owner:
                <input class="button edit" type="image" src="/static/icons/pencil.png" />
                <input class="button accept" type="image" src="/static/icons/accept.png" />
                <input class="button remove" type="image" src="/static/icons/delete.png" />
                % endif
            </div>
            <div class="day-zero-item-longtext"> 
                <p class="day-zero-item-description ${'multi-editable' if request.context.user == request.user else ''}">
                % if item.long_description:
                    ${item.long_description}
                % elif owner:
                    <span class="notice">Double-click to enter a long description</span>
                % endif
                </p>
                
                <label class="day-zero-label day-zero-item-label" for="day-zero-item-timestamp-added">Added:</label>
                <p class="day-zero-item-timestamp" name="day-zero-item-timestamp-added">${item.created_at.strftime("%Y.%m.%d %H:%M")}</p>

                % if item.completed_at:
                <label class="day-zero-label day-zero-item-label" for="day-zero-item-timestamp-completed">Completed:</label>
                <p class="day-zero-item-timestamp" name="day-zero-item-timestamp-completed">${item.completed_at.strftime("%Y.%m.%d %H:%M")}</p>
                % endif
            </div>
            </form>
        </div>
    </li>
    % endfor
    % if len(request.context.items) >= 1:
        <li class="hover new"><span class="notice">Click here to add a new item</span></li>
    % endif
</ol>
</div>

<%def name='owner_name()'>
    % if request.context.user.name:
        ${request.context.user.name}
    % else:
        ${request.context.user.email}
    % endif
</%def>

<%def name='head_js()'>
<script type="text/javascript" src="${request.static_url('riotoustools:static/jquery.tmpl.min.js')}"></script>
<script type="text/javascript" src="${request.static_url('riotoustools:static/dayzero.js')}"></script>
</%def>


<%def name='head_css()'>
<link href="/static/dayzero.css" rel="stylesheet" type="text/css" /> 
</%def>
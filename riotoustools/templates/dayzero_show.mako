<%inherit file="base.mako"/>

<div id="center-content"> 
<div class="day-zero-list-info">
    <label class="day-zero-label">Owner:</label>
    <p class="inline-block day-zero-info-owner">${owner_name()}</p>
    <label class="day-zero-label">Name:</label>
    <p class="inline-block day-zero-item-text ${'editable' if dayzero_list.user == user else ''}">${dayzero_list.name}</p>
    <label class="day-zero-label">Start Date:</label>
    <p class="inline-block ${'editable' if dayzero_list.user == user else ''}">${dayzero_list.start_at.strftime('%Y.%m.%d')}</p>
    <label class="day-zero-label">Finish Date:</label>
    <p class="inline-block ${'editable' if dayzero_list.user == user else ''}">${dayzero_list.end_at.strftime('%Y.%m.%d')}</p>
</div>

<ol id="day-zero-list">
    % for item in dayzero_list.items:
    <li class="day-zero-item">
        <div class="day-zero-item-container">
            <form class="inline-block" name="day-zero-item-form" action="/dayzeroitem/${item.id}/edit">
            <input type="hidden" name="completed" value="${item.completed}" />
            <p class="day-zero-item-text ${'editable' if dayzero_list.user == user else ''} ${'item-complete' if item.completed else ''}">${item.description}</p>
            <div class="day-zero-item-buttons">
                % if dayzero_list.user == user:
                <input class="button edit" type="image" src="/static/icons/pencil.png" />
                <input class="button accept" type="image" src="/static/icons/accept.png" />
                <input class="button remove" type="image" src="/static/icons/cancel.png" />
                % endif
            </div>
            <div class="day-zero-item-longtext"> 
                <p class="day-zero-item-description ${'multi-editable' if dayzero_list.user == user else ''}">
                % if item.long_description:
                    ${item.long_description}
                % else:
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
</ol>
</div>

<%def name='owner_name()'>
    % if dayzero_list.user.name:
        ${dayzero_list.user.name}
    % else:
        ${dayzero_list.user.email}
    % endif
</%def>
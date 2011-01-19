<%inherit file="base.mako"/>

<div id="center-content"> 
<h3>Viewing ${dayzero_list.name}'s 101 in 1001 list</h3>
<ol id="day-zero-list">
    % for item in dayzero_list.items:
    <li class="day-zero-item">
        <div class="day-zero-item-container">
            <p class="day-zero-item-text editable ${'item-complete' if i==3 else ''}">${item.description}</p>
            <div class="day-zero-item-buttons">
                <input class="button edit" type="image" src="/static/icons/edit_desc.png" />
                <input class="button accept" type="image" src="/static/icons/accept.png" />
                <input class="button cancel" type="image" src="/static/icons/cancel.png" />
            </div>
            <div class="day-zero-item-longtext">
                <p class="day-zero-item-description multi-editable">This holds content.</p>
                
                <label class="day-zero-item-label" for="day-zero-item-timestamp-added">Added:</label>
                <p class="day-zero-item-timestamp" name="day-zero-item-timestamp-added">2010.10.10 14:45</p>

                <label class="day-zero-item-label" for="day-zero-item-timestamp-completed">Completed:</label>
                <p class="day-zero-item-timestamp" name="day-zero-item-timestamp-completed">2010.12.10 14:25</p>
            </div>
        </div>
    </li>
    % endfor
</ol>
</div>
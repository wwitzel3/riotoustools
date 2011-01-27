<%inherit file="../base.mako"/>

<div id="center-content">
    <h4>Welcome</h4>

    % if request.user:
    <h4>Your Information</h4>
        ${request.user}
    % endif
</div>
<%inherit file="../base.mako"/>

<div id="center-content">
    %if request.session.peek_flash():
        <h3>${request.session.pop_flash()[0]}</h3>
    %endif
    
    <h4>Welcome</h4>
    <p>You are seeing this because you are not logged in to the Riotous Living
    tools website. You can create an account or login using the forms below. If
    you aren't sure what you should have an account then you can <a href="/about">read more on our
    About page</a>.
    </p>
    
    ${login_form}
    
    ${signup_form}

</div>
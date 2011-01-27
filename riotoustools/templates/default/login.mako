<%inherit file="../base.mako"/>

<div id="center-content">
    %if session.peek_flash():
        <h3>${session.pop_flash()[0]}</h3>
    %endif
    
    <h4>Welcome</h4>
    <p>You are seeing this because you are not logged in to the Riotous Living
    tools website. You can create an account or login using the forms below. If
    you aren't sure what you should have an account then you can <a href="/about">read more on our
    About page</a>.
    </p>
    
    <div id="login-form" class="login-forms">
        <form name='login' action='/' method='post'>
        <fieldset>
        <legend>Login</legend>
        <ol>
        <li>
            <label for="login-email">Email:</label>
            <input type='text' id="login-email" name='email' />
        </li>
        <li>
            <label for="login-password">Password:</label>
            <input type='password' id="login-password" name='password' />
        </li>
        <li>
            <input type='submit' name='form.login' value='Login' />
            <input type='hidden' name='next' value='' />
        </li>
        </ol.>
        </fieldset>
        </form>
    </div>
    
    <div id="create-user-form" class="login-forms">
        <form name='create' action='/create_user' method='post'>
        <fieldset>
        <legend>Signup</legend>
        <ol>
        <li>
            <label for="create-email">Email:</label>
            <input type='text' id="create-email" name='email' />
        </li>
        <li>
            <label for="create-name">Name:</label>
            <input type='text' id="create-name" name='name' />
        </li>
        <li>
            <label for="create-password">Password:</label>
            <input type='password' id="create-password" name='password' />
        </li>
        <li>
            <input type='submit' name='form.create' value='Signup' />
            <input type='hidden' name='next' value='' />
        </li>
        </ol>
        </fieldset>
        </form>
    </div>
</div>
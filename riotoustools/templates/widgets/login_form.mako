<div id="login-form" class="login-forms">
    <form name='login' action='${request.resource_url(request.context)}login' method='post'>
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
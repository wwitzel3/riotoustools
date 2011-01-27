<div id="create-user-form" class="login-forms">
    <form name='create' action='${request.resource_url(request.context)}' method='post'>
    <fieldset>
    <legend>Signup</legend>
    <ol>
    <li>
        <label for="create-email">* Email:</label>
        <input type='text' id="create-email" name='email' />
        <form:error name="email" />
    </li>
    <li>
        <label for="create-name">* Display Name:</label>
        <input type='text' id="create-name" name='name' />
    </li>
    <li>
        <label for="create-password">* Password:</label>
        <input type='password' id="create-password" name='password' />
    </li>
    <li>
        <label for="create-password-verify">Retype Password:</label>
        <input type='password' id="create-password-verify" name='password_verify' />
    </li>
    <li>
        <input type='submit' name='form.create' value='Signup' />
        <input type='hidden' name='next' value='' />
    </li>
    </ol>
    </fieldset>
    </form>
</div>
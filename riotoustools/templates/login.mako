<%inherit file="base.mako"/>

<div id="center-content">
    %if session.peek_flash():
        <h3>${session.pop_flash()[0]}</h3>
    %endif
    
    <div id="login-form" class="login-forms">
        <form name='login' action='/' method='post'>
        <fieldset>
        <legend>Login</legend>
            <label for="login-email">Email:</label>
            <input type='text' id="login-email" name='email' />
            
            <label for="login-password">Password:</label>
            <input type='password' id="login-password" name='password' />
            <input type='submit' name='form.login' value='Login' />
        </fieldset>
        </form>
    </div>
    
    <div id="create-user-form" class="login-forms">
        <form name='create' action='/create_user' method='post'>
        <fieldset>
        <legend>Signup</legend>
            <label for="create-email">Email:</label>
            <input type='text' id="create-email" name='email' />
            
            <label for="create-name">Name:</label>
            <input type='text' id="create-name" name='name' />
            
            <label for="create-password">Password:</label>
            <input type='password' id="create-password" name='password' />
            
            <input type='submit' name='form.create' value='Signup' />
        </fieldset>
        </form>
    </div>
</div>
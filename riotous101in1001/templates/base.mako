<!DOCTYPE html 
     PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />

<title>riotousliving.com - ${self.title()}</title>

<link href="/static/style.css" rel="stylesheet" type="text/css" /> 
<link href="/static/weareawesome.css" rel="stylesheet" type="text/css" /> 

<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.1/jquery.min.js"></script>
<script type="text/javascript" src="/static/javascript.js"></script>

</head>

<body>
    <div id="header">
        <div id="banner">
            <div class="container">
            <p id="logo"><a href="/">riotousliving.com 101 in 1001</a></p>
            
            <ul id="nav-index">
                <li><a href="/">Home</a></li>
                <li><a href="/">Create A List</a></li>
                <li><a href="/">Browse Lists</a></li>
                <li><a href="/">About</a></li>
            </ul>
            </div>
        </div>
    </div>
    <div class="clear"></div>
    
    <div id="content">
        <div class="container">
            ${next.body()}
        <div class="clear"></div>
        </div>
    </div>
    <div class="clear"></div>
    
    <div id="footer">
        <div class="container">
            <ul id="nav-bottom">
                <li><a href="/">Blog</a></li>
                <li><a href="/">Contact</a></li>
                <li><a href="/">Privacy</a></li>
            </ul>
            <p id="copyright">&copy; 2010 riotousliving.com</p>
        </div>
    </div>
</body>
</html>

<%def name='title()'>
    101 in 1001
</%def>
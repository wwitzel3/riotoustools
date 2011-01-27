from pyramid.url import static_url

def get_url_from_email(request):
    # import code for encoding urls and generating md5 hashes
    import urllib, hashlib

    # Set your variables here
    size = 100

    # construct the url
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(request.context.user.email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':'wavatar', 's':str(size)})
    
    return gravatar_url
def view_root(context, request):
    return {'items':list(context), 'project':'riotous101in1001'}

def view_model(context, request):
    return {'item':context, 'project':'riotous101in1001'}

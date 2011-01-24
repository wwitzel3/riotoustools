$.template('completed-template', [
    ' <label class="day-zero-label day-zero-item-label" for="day-zero-item-timestamp-completed">Completed:</label> ',
    ' <p class="day-zero-item-timestamp" name="day-zero-item-timestamp-completed">${completed_at}</p> '].join('')
);

$.template('notcompleted-template', [
    ' <p class="day-zero-item-description multi-editable">{{if long_description}}${long_description}{{else}} ',
    '<span class="notice">Double-click to enter a long description</span>{{/if}}</p> ',
    ' <label class="day-zero-label day-zero-item-label" for="day-zero-item-timestamp-added">Added:</label> ',
    ' <p class="day-zero-item-timestamp" name="day-zero-item-timestamp-added">${created_at}</p> '].join('')
);

$.template('item-template', [
    '<li style="display:none" class="day-zero-item new">',
    '<div class="day-zero-item-container">',
    '<form class="inline-block" name="day-zero-item-form" action="/dayzeroitem/${id}">',
    '<input type="hidden" name="completed" value="${completed}" />',
    '<p class="day-zero-item-text editable">${description}</p>',
    '<div class="day-zero-item-buttons">',
    '<input class="button edit" type="image" src="/static/icons/pencil.png" />',
    '<input class="button accept" type="image" src="/static/icons/accept.png" />',
    '<input class="button remove" type="image" src="/static/icons/delete.png" />',
    '</div><div class="day-zero-item-longtext">',
    '<p class="day-zero-item-description multi-editable">',
    '<span class="notice">Double-click to enter a long description</span></p>',
    '<label class="day-zero-label day-zero-item-label" for="day-zero-item-timestamp-added">Added:</label>',
    '<p class="day-zero-item-timestamp" name="day-zero-item-timestamp-added">${created_at}</p>',
    '</div></form></div></li>'].join('')
);

$.template('item-new-template', [
    '<div class="day-zero-item-container">',
    '<form class="inline-block" name="day-zero-item-add">',
    '<input type="text" name="description" value="" />',
    '<button class="add">Save</button>',
    '<button class="cancel">Cancel</button>',
    '</form></div>'].join('')
);

$('.accept').live('click', function(o) {
    /* Using live so the event binds to list items as they are added dynamically.
       Grab the surrounding parent div for the target input.
       Select the child p tag of that parent div.
       Apply the item-complete style to the p tag.
       Send an AJAX request to PUT/UPDATE the list item as completed in the database.
    */
    o.stopPropagation(); o.preventDefault();
    var container = $(o.target).parents('div.day-zero-item-container');
    var item_text = container.find('.day-zero-item-text.editable');
    var form = container.find('form[name=day-zero-item-form]');
    var completed = $(form).find('input[name=completed]');

    if (completed.val() == "True")
        completed.val('False');
    else
        completed.val('True');
        
    $.post(form.attr('action')+'/edit', form.serialize(), function(data) {
        if (data.status) {
            var item_long_text = $(container).find('.day-zero-item-longtext');
            if (data.completed)
                item_long_text.append($.tmpl('completed-template', data));
            else
                item_long_text.html($.tmpl('notcompleted-template', data));
        }
    });
    item_text.toggleClass('item-complete');
    return false;
});

$('.hover.new').live('click', function(o) {
    o.stopPropagation(); o.preventDefault();
    var item_container = $(o.target).parents('.day-zero-item-container');
    if ($(item_container).find('input[name=description]').length != 0) {
        o.stopPropagation();
        return false;
    }
    $(o.target).html($.tmpl('item-new-template'));
    return false;
});

$('.add').live('click', function(o) {
    o.stopPropagation(); o.preventDefault();
    var item = $('.hover.new');
    $(item).html('<span class="notice">Click here to add a new item</span>');
    
    var action = $('input[name=day-zero-item-add-action]').val();
    var form = $(o.target).parents('.day-zero-item-container').find('form[name=day-zero-item-add]');
    var dayzero_list = $('#day-zero-list');
    
    $.post(action, form.serialize(), function (data) {
        if (data.status) {
            if ($('#day-zero-list').children('li').length == 1) {
                dayzero_list.append($.tmpl('item-template', data));
                dayzero_list.append('<li class="hover new"><span class="notice">Click here to add a new item</span></li>');
            } else {
                $('#day-zero-list').children('li:last').before($.tmpl('item-template', data));
            }
            $('.day-zero-item.new').fadeIn(500, function() {
                $('.day-zero-item.new').removeClass('new');
            });
        }
    });

    return false;    
});

$('.remove').live('click', function(o) {
    o.stopPropagation(); o.preventDefault();
    var confirmed = confirm("Are you sure you want to remove this item?");
    if (confirm) {
        var form = $(o.target).parents('.day-zero-item-container').find('form[name=day-zero-item-form]');
        $.post(form.attr('action')+'/remove', form.serialize(), function(data) {
            if (data.status) {
                if ($('#day-zero-list').children('li').length == 3) {
                    $('#day-zero-list').children('li:last').fadeOut(500, function () { $(this).remove(); });
                }
                var item = $(o.target).parents('.day-zero-item');
                $(item).fadeOut(500, function () { $(this).remove(); });
            }
        });
    }
    return false;
});

$('.day-zero-item-text').live('click', function(o) {
    var item_container = $(o.target).parents('.day-zero-item-container');
    if ($(item_container).find('input[name=description]').length != 0) {
        o.stopPropagation();
        return false;
    }
    var item_description = $(o.target).parents('.day-zero-item-container').find('.day-zero-item-longtext');
    item_description.slideToggle("slow");
});

$('.edit').live('click', function(o) {
    var item_container = $(o.target).parents('.day-zero-item-container');
    var self = $(item_container).find('.day-zero-item-text.editable');
    self.value = self.text();
    self.html([
        '<input type="text" name="description" value="'+ self.value + '" />',
        '<button class="save">Save</button>',
        '<button class="cancel">Cancel</button>'
    ].join(''));
    $(item_container).find('.button.edit').css('display', 'none');
    return false;
});

$('.multi-editable').live('dblclick', function(o) {
    var item_container = $(o.target).parents('.day-zero-item-container');
    if ($(item_container).find('textarea[name=long_description]').length != 0) {
        o.stopPropagation();
        return false;
    }
    var self = $(o.target);
    self.value = self.text();
    self.html([
        '<textarea name="long_description">',
        self.value,
        '</textarea><button class="save">Save</button>',
        '<button class="cancel">Cancel</button>'
    ].join(''));
});

$('.save').live('click', function (o) {
    o.stopPropagation(); o.preventDefault();
    var item_container = $(o.target).parents('.day-zero-item-container');
    var form = $(item_container).find('form[name=day-zero-item-form]');
    $.post(form.attr('action')+'/edit', form.serialize(), function (data) {
        if (data.status) {
            var description = $(form).find('.day-zero-item-text');
            description.html(data.description);
            var long_description = $(form).find('.day-zero-item-description');
            if (data.long_description) {
                long_description.html(data.long_description);
            } else {
                long_description.html('<span class="notice">Double-click to enter a long description</span>');
            }
        }
    });
    $(item_container).find('.button.edit').css('display', 'inline-block');
    return false;
});

$('.cancel').live('click', function(o) {
    o.stopPropagation(); o.preventDefault();
    var item_container = $(o.target).parents('.day-zero-item-container');
    var form = $(item_container).find('form[name=day-zero-item-form]');
    $(form).each(function(){
       this.reset();
    });
    
    var description = $(form).find('input[name=description]');
    if (description.length != 0)
        $(form).find('.day-zero-item-text').html(description.val());
    
    var long_description = $(form).find('textarea[name=long_description]');
    if (long_description.length != 0)
        $(form).find('.day-zero-item-description').html(long_description.val());

    $(item_container).find('.button.edit').css('display', 'inline-block');
    return false;
});
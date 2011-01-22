$.template('completed-template', [
    ' <label class="day-zero-label day-zero-item-label" for="day-zero-item-timestamp-completed">Completed:</label> ',
    ' <p class="day-zero-item-timestamp" name="day-zero-item-timestamp-completed">${completed_at}</p> '].join('')
);

$.template('notcompleted-template', [
    ' <p class="day-zero-item-description multi-editable">This holds content.</p> ',
    ' <label class="day-zero-label day-zero-item-label" for="day-zero-item-timestamp-added">Added:</label> ',
    ' <p class="day-zero-item-timestamp" name="day-zero-item-timestamp-added">${created_at}</p> '].join('')
);

$('.accept').live('click', function(o) {
    /* Using live so the event binds to list items as they are added dynamically.
       Grab the surrounding parent div for the target input.
       Select the child p tag of that parent div.
       Apply the item-complete style to the p tag.
       Send an AJAX request to PUT/UPDATE the list item as completed in the database.
    */
    var container = $(o.target).parents('div.day-zero-item-container');
    var item_text = container.find('.day-zero-item-text.editable');
    var form = container.find('form[name=day-zero-item-form]');
    var completed = $(form).find('input[name=completed]');

    if (completed.val() == "True")
        completed.val('False');
    else
        completed.val('True');
        
    $.post(form.attr('action'), form.serialize(), function(data) {
        if (data.status) {
            var item_long_text = $(container).find('.day-zero-item-longtext');
            if (data.completed)
                item_long_text.append($.tmpl('completed-template', data));
            else
                item_long_text.html($.tmpl('notcompleted-template', data));
        }
    });
    item_text.toggleClass('item-complete');
});

$('.editable').live('click', function(o) {
    var item_description = $(o.target).parents('.day-zero-item-container').find('.day-zero-item-longtext');
    item_description.slideToggle("slow");
});

$('.editable').live('dblclick', function(o) {
    o.stopPropagation();
    var self = $(o.target);
    self.value = self.text();
    self.html('<input type="text" name="description" value="'+ self.value + '" /><button class="save">Save</button>');
});

$('.multi-editable').live('dblclick', function(o) {
    var self = $(o.target);
    self.value = self.text();
    self.html('<textarea name="item-description">' + self.value + '</textarea><button>Save</button><button>Cancel</button>');
});

$('.save').live('click', function (o) {
    o.stopPropagation();
    var form = $(o.target).parents('.day-zero-item-container').find('form[name=day-zero-item-form]');
    $.post(form.attr('action'), form.serialize(), function (data) {
        if (data.status) {
            var self = $(form).find('.day-zero-item-text');
            self.html($(self).find('input').val());
        }
    });
    return false;
});


$('input.button.accept').live('click', function(o) {
    /* Using live so the event binds to list items as they are added dynamically.
       Grab the surrounding parent div for the target input.
       Select the child p tag of that parent div.
       Apply the item-complete style to the p tag.
       Send an AJAX request to PUT/UPDATE the list item as completed in the database.
    */
    var item_text = $(o.target).parents('div.day-zero-item-container').find('.day-zero-item-text.editable');
    console.log(item_text);
    item_text.addClass('item-complete');
});

$('input.button.edit').live('click', function(o) {
    var item_description = $(o.target).parents('.day-zero-item-container').find('.day-zero-item-longtext');
    item_description.slideToggle("slow");
});

$('.editable').live('dblclick', function(o) {
    var self = $(o.target);
    self.value = self.text();
    self.html('<input type="text" name="item-text" value="'+ self.value + '" /><button>Save</button>');
});

$('.multi-editable').live('dblclick', function(o) {
    var self = $(o.target);
    self.value = self.text();
    self.html('<textarea name="item-description">' + self.value + '</textarea><button>Save</button><button>Cancel</button>');
});
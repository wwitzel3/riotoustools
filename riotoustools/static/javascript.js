$(document).ready(function () {
    $('input[name=next]').each(function() {
        $(this).val(window.location.pathname);
    });
});
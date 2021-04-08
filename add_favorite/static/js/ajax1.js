// функция - обработчик

function to_bookmarks()
{
    var current = $(this);
    var type = current.data('type');
    var pk = current.data('id');
    var action = current.data('action');

    $.ajax({
        url : type + "/" + pk + "/" + action + "/",
        type : 'POST',
        data : { 'obj' : pk },

        success : function (data) {
            $('.favorite_list').html(data.result)
            current.find("[data-count='" + action + "']").text(data.count);
        }
    });

    return false;
}

// Подключение обработчика
$(function() {
    $('[data-action="bookmark"]').click(to_bookmarks);
});

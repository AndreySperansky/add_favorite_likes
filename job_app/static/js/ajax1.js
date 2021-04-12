// функция - обработчик

$('.bookmark_list').on('click', 'button[type="button"]',  function () {
    var target_href = Event.target;

    $.ajax({
        url: "/job/vacancy/" + target_href + "/bookmark/",

        // data: {
        // Получаем из запроса поэтому не используем
        // },

        dataType: 'json',

        success: function (data) {
            $('.bookmark_list').html(data.result)
        }
    });
});




// Рабочий варант - заменяет текст внутри кнопки и количество лайков

$(document).ready(function(){

    $('.like-form').submit(function(e){
        e.preventDefault()
        console.log('works')
        
        const post_id = $(this).attr('id')
        console.log(post_id)

        const button = $(`.like-btn${post_id}`)
        console.log(button)
        
        const cls = button.attr('class')
        console.log(cls)
        
        const url = $(this).attr('action')
        console.log(url)
        
        // let value = $(this).data('value')
        // console.log(value)
        
        let res;
        const likes = $(`.like-count${post_id}`).text()
        const trimCount = parseInt(likes)
        console.log(trimCount + 1)

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'post_id': post_id,
            },

            success: function(response) {
                // console.log('success', response)
                if(button.hasClass('btn-outline-info')) {
                    $(`.like-btn${post_id}`).toggleClass('btn-outline-info btn-info')
                    res = trimCount + 1
                } else {
                    $(`.like-btn${post_id}`).toggleClass('btn-info btn-outline-info')
                    res = trimCount - 1
                }

                $(`.like-count${post_id}`).text(res)
            },

            error: function(response) {
                console.log('error', response)
            }
        })
        
        
        
    });

});


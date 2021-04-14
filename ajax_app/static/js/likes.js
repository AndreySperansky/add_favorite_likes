// Рабочий варант - заменяет текст внутри кнопки и количество лайков

$(document).ready(function(){

    $('.like-form').submit(function(e){
        e.preventDefault()
        // console.log('works')
        
        const post_id = $(this).attr('id')
        // console.log(post_id)
       
        const likeText = $(`.like-btn${post_id}`).text()
        const trim = $.trim(likeText)
        // console.log(trim)
        
        const url = $(this).attr('action')
        // console.log(url)
        
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
                if(trim === 'Unlike') {
                    $(`.like-btn${post_id}`).text('Like')
                    res = trimCount - 1
                } else {
                    $(`.like-btn${post_id}`).text('Unlike')
                    res = trimCount + 1
                }
                
                $(`.like-count${post_id}`).text(res)
            },
            
            error: function(response) {
                console.log('error', response)
            }
        })
        
        
        
    });

});


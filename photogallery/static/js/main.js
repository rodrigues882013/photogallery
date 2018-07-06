$(function(){

    function callback(event){
            var photo_id = $(this).data('id');

            $.ajax({
                url: event.data.url,
                data: {photo_id: photo_id},
                type: 'post',
                dataType: 'json',
                success: function(data) {
                    if (event.data.url === 'like')
                        $('.likes-' + photo_id).text(data.liked)
                },
                error: function (xhr, err, errorThrown) {
                  console.error('Error: %s', errorThrown)
                }
            });



    }


    $('.like').on('click', {'url': 'like'}, callback);


    $('.approve').on('click', {'url': 'approve'}, callback)

})
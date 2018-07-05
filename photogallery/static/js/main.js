$(function(){
    $('.like').on('click', function(evt){
        var photo_id = $(this).data('id');

        $.ajax({
		    url: 'like',
		    data: {like: 1, photo_id: photo_id},
		    type: 'post',
		    dataType: 'json',
		    success: function(data) {
                $('.likes-' + photo_id).text(data.liked)
		    },
		    error: function (xhr, err, errorThrown) {
              console.error('Error: %s', errorThrown)
            }
		});
    });

})
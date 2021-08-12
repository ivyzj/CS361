// first load the page
$(document).ready( function(){
    console.log("document ready");
    let searchParams = new URLSearchParams(window.location.search)
    let id = searchParams.get('page') 
    $.ajax({
        type: "GET",
        url: "/api/learning/" + id,
        success: function(res, status, xhr) {
            $.each(res, function (index, word) {
                let imgURL = 'https://cs361-micro.herokuapp.com/api/title/' + word
                $('#add-image').attr('src', imgURL)
            });
        },
    })
});
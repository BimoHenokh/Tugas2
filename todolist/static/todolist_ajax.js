$(document).ready(function(){
    $.getJSON("json/", function(data) {
        $.each(data, function(key, value) {
            responsive = '<div class="col-12 col-sm-6 col-lg-4 col-xxl-3">'
            card = '<div class="card">'
            card_body = '<div class="card-body border-primary" >'
            card_body_body = '<div class="card-body '
            card_body_title = '<h3 class="card-title">' + value.fields.title + '</h3>'
            card_body_date = '<h6 class="card-mb-2 text-muted">' + value.fields.date + '</h6>'
            card_body_description = '<p class="card-text">' + value.fields.description + '</p>'
            closing = '</div></div></div></div>'
            $("#show_ajax").append(responsive+card+card_body+card_body_body+card_body_title+card_body_date+card_body_description+closing)
        })
    });

    $("#submit_form").click(function(){

        input_title = $("#input_title").val()
        input_description = $("#input_description").val()
        csrftoken = Cookies.get('csrftoken');
        current_date = new Date().toJSON().slice(0, 10);

        data_send = {
            title : input_title,
            description : input_description,
            csrfmiddlewaretoken : csrftoken
        }
        $.post('add/', data_send)

        responsive = '<div class="col-12 col-sm-6 col-lg-4 col-xxl-3">'
        card = '<div class="card">'
        card_body = '<div class="card-body border-primary" >'
        card_body_body = '<div class="card-body '
        card_body_title = '<h3 class="card-title">' + input_title + '</h3>'
        card_body_date = '<h6 class="card-mb-2 text-muted">' + current_date + '</h6>'
        card_body_description = '<p class="card-text">' + input_description + '</p>'
        closing = '</div></div></div></div>'
        $("#show_ajax").append(responsive+card+card_body+card_body_body+card_body_title+card_body_date+card_body_description+closing)

    });

});
// memberikan crsf token https://sydjameer.medium.com/how-to-resolve-forbidden-403-if-django-csrf-mechanism-has-not-been-used-in-post-method-1aeeb8540404

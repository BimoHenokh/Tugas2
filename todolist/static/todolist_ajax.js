$(document).ready(function(){
    task_pk = 0;

    // Mengirim request GET
    $.getJSON("json/", function(data) {
        task_pk += data[data.length - 1].pk

        $.each(data, function(key, value) {
            task_pk = value.pk

            append_element = 
            '<div class="col-12 col-sm-6 col-lg-4 col-xxl-3" id="1">'+
                '<div class="card">'+
                    '<div class="card-body border-primary" >'+
                        '<div class="card-body '+
                            '<h3 class="card-title">' + value.fields.title + '</h3>'+
                            '<h6 class="card-mb-2 text-muted">' + value.fields.date + '</h6>'+
                            '<p class="card-text">' + value.fields.description + '</p>'+
                            '<button type="button" class="btn btn-primary" id="btn_pk'+task_pk+'" onclick=deleteFunction("'+task_pk+'")">Delete</button>'+
                        '</div>'+
                    '</div>'+
                '</div>'+
            '</div>';
            $("#show_ajax").append(append_element);
        })
        
    });

    // Mengirim request POST
    $("#submit_form").click(function(){

        input_title = $("#input_title").val();
        input_description = $("#input_description").val();
        csrftoken = Cookies.get('csrftoken');
        current_date = new Date().toJSON().slice(0, 10);

        data_send = {
            title : input_title,
            description : input_description,
            csrfmiddlewaretoken : csrftoken
        };
        $.post('add/', data_send);

        append_element = 
            '<div class="col-12 col-sm-6 col-lg-4 col-xxl-3" id="'+task_pk+'">'+
                '<div class="card">'+
                    '<div class="card-body border-primary" >'+
                        '<div class="card-body '+
                            '<h3 class="card-title">' + input_title + '</h3>'+
                            '<h6 class="card-mb-2 text-muted">' + current_date + '</h6>'+
                            '<p class="card-text">' + input_description + '</p>'+
                            '<button type="button" class="btn btn-primary" id="btn_pk'+task_pk+'" onclick=deleteFunction("'+task_pk+'") >Delete</button>'+
                        '</div>'+
                    '</div>'+
                '</div>'+
            '</div>';
        $("#show_ajax").append(append_element);
        $("#djangoForm").modal('hide');
        
    });

    

});

function deleteFunction() {
    
}
// memberikan crsf token https://sydjameer.medium.com/how-to-resolve-forbidden-403-if-django-csrf-mechanism-has-not-been-used-in-post-method-1aeeb8540404

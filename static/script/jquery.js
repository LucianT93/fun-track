function show_details(id) {
    $.ajax({
        method: "GET",
        url: '/task_detail/' + id,
        dataType: 'json'
    }).done(function (data) {
        $('#task_detail').load('/task_detail/' + id, data)
    })
}

function changeColor() {
    let color = document.getElementById('colorpicker').value;
    document.documentElement.style
        .setProperty('--button-color', color);
    document.getElementById('colorpicker').value = color;
}

$(document).ready(() => {
    $('#login_form').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: 'POST',
            url: "login_register/",
            data: {
                flag: $("#flag").val(),
                username: $('#user-login').val(),
                password: $('#password-login').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {
                if (data['message'] === 'success') {
                    location.reload()
                } else {
                    $('#login_error').show()
                }
            }
        })
    })
})

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

$(document).ready(function () {
    $('#login_form').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: 'POST',
            url: "login/",
            data: {
                username: $('#user-login').val(),
                password: $('#password-login').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {
                console.log(data)
                if (data['message'] === 'success') {
                    window.location.replace('/tasks/')
                } else {
                    $('#login_error').show()
                }
            }
        })
    })

    $('#register_form').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: 'POST',
            url: "register/",
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                username: $('#username_register').val(),
                email: $('#email_register').val(),
                password1: $('#pass1_register').val(),
                password2: $('#pass2_register').val(),
            },
            success: function (data) {
                if (data['message'] === 'success') {
                    $('#register_success').show()
                } else {
                    $('#register_error').show()
                }
            }
        })
    })
})


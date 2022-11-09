$(document).ready(function () {
    $(".btn").click(function () {
        $.ajax({
            method: "GET",
            url: '/task_detail/',
            dataType: 'json'
        }).done(function (data) {
            $('#task_detail').load('/task_detail_html/', data)
        })
    })
})


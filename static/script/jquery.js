function show_details(id) {
    $.ajax({
        method: "GET",
        url: '/task_detail/' + id,
        dataType: 'json'
    }).done(function (data) {
        $('#task_detail').load('/task_detail_html/', data)
    })
}
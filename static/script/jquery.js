function show_details(id) {
    $.ajax({
        method: "GET",
        url: '/task_detail/' + id,
        dataType: 'json'
    }).done(function (data) {
        $('#task_detail').load('/task_detail/'+id, data)
    })
}

function changeColor() {
    let color = document.getElementById('colorpicker').value;
    document.documentElement.style
        .setProperty('--button-color', color);
    document.getElementById('colorpicker').value = color;
}

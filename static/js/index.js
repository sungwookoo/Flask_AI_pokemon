function posting() {
    // let title = $('#title').val()
    let file = $('#file')[0].files[0]
    let file_title = 'upload'

    let form_data = new FormData()

    // form_data.append("title_give", title)
    form_data.append("file_give", file)
    form_data.append("file_title_give", file_title)

    $.ajax({
        type: "POST",
        url: "/api/feed_upload",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response["result"])
            window.location.reload()
        }
    });
}
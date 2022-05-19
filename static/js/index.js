function posting() {
    let title = $('#title').val()
    let file = $('#file')[0].files[0]
    let form_data = new FormData()

    form_data.append("title_give", title)
    form_data.append("file_give", file)

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

  // function find_img() {
  //   let title = $('#find_title').val()
  //   document.getElementById('link').href = '/fileshow/'+title
  // }


function logout() {
    $.ajax({
        type: "GET",
        url: "/api/logout",
        data: {},
        success: function (response) {
            if (response['result'] === 'success') {
                $.removeCookie('mytoken', response['token'])
                alert(response['msg'])
                window.location.href = '/';
            } else {
                alert(response['msg'])
                window.location.href = '/';
            }
        }
    })
}

function posting() {
    // let title = $('#title').val()
    let file = $('#file')[0].files[0]

    let form_data = new FormData()
    let opaci = 0;
    const lightbutton = document.querySelector('.light');
    function loading() {
        lightbutton.style.backgroundColor = "rgba(0,0,200,"+(1-opaci%1)+")";
        opaci += 0.01;
        raf = requestAnimationFrame(loading)
    }
    loading()
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
            if (response["result"]=='업로드 완료!') {
            window.location.replace('/result')
        }else {window.location.href='/'}
        }
    });
}


const reader = new FileReader();

reader.onload = (readerEvent) => {
    document.querySelector("#img_section").setAttribute("src", readerEvent.target.result);
    //파일을 읽는 이벤트가 발생하면 img_section의 src 속성을 readerEvent의 결과물로 대체함
};

document.querySelector("#file").addEventListener("change", (changeEvent) => {
    //upload_file 에 이벤트리스너를 장착

    const imgFile = changeEvent.target.files[0];
    reader.readAsDataURL(imgFile);
    //업로드한 이미지의 URL을 reader에 등록
})
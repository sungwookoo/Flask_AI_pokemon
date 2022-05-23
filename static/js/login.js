const loginbuttom = document.querySelector('#btn_login');
loginbuttom.addEventListener('click', sign_in)

function sign_in() {
    user_id = $('#user_id').val();
    password = $('#password').val();

    $.ajax({
        type: 'POST',
        url: '/login',
        data: {
            email_give: user_id,
            pw_give: password
        },
        success: function (response) {
            if (response['result'] == 'success') {
                $.cookie('mytoken', response['token'], {path: '/'});
                window.location.replace('/main')
            } else {
                var child = document.querySelector(".append_st");
                if (child.hasChildNodes()) {
                    child.removeChild(child.childNodes[0]);
                }
                var creat_sentence = document.createElement('p');
                var creat_text = document.createTextNode(response['msg']);
                creat_sentence.appendChild(creat_text);
                creat_sentence.classList.add('creatst');
                child.appendChild(creat_sentence);

            }
        }
    });
}

$('.container').keyup('keyup', function(event) {
    if(event.keyCode === 13) {
        $('#btn_login').click();
        }

});
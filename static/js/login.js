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
                alert(response['msg'])
            }
        }
    });
}


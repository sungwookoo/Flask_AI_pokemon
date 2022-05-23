$(document).ready(function () {
    getimgResult();
    getpokeResult();
    getaccResult();
})

function getimgResult() {
    $.ajax({
        type: "GET",
        url: "/api/get_imgresult",
        data: {},
        success: function (response) {
            let result_img = response['result_img'];
            let temp_img = `
                    <img id="result_pokemon" src="${result_img}" alt="result img" width="100%" height="100%">
                    `
            $('.result_display').append(temp_img);
        }
    })
}

function getpokeResult() {
    $.ajax({
        type: "GET",
        url: "/api/get_pokeresult",
        data: {},
        success: function (response) {
            let result_poke = response['result_poke'];
            let temp_poke = `<p>${result_poke} 포켓몬 입니다</p>`
            $('.result_desc').append(temp_poke);
        }
    })
}

function getaccResult() {
    $.ajax({
        type: "GET",
        url: "/api/get_accresult",
        data: {},
        success: function (response) {
            let result_acc = response['result_acc'];
            let temp_acc = `<p  style="margin-top : -30px">${result_acc}% 일치합니다</p> `
            $('.result_desc').append(temp_acc);
        }
    })
}
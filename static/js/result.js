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
                    <img id="result_pokemon" src="${result_img}" alt="result img">
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
            let result_img = response['result_img'];
            let url = result_img;
            url=url.split('/')[2];
            url=url.split('.')[0];
            let result_poke = response['result_poke'][0];
            let temp_poke = `<p id="dogam">축하드려요</br> '${url}'를 발견했어요!</p>`
            $('.dogam').append(temp_poke);
        }
    })
}

function getaccResult() {
    $.ajax({
        type: "GET",
        url: "/api/get_accresult",
        data: {},
        success: function (response) {
            let result_poke = response['result_poke'];
            let result_acc = response['result_acc'];
            let temp_poke = [];
            let temp_acc = [];
            let result_p;
            let result_a;
            let result_msg;
            for(var i=0; i<result_poke.length;i++){
                temp_poke.push(result_poke[i]);
            }
            for(var i=0; i< result_acc.length;i++){
                temp_acc.push(result_acc[i]);
            }
            for(var i=0; i< result_acc.length;i++){
                if (result_acc.length === 12) {
                    break;
                }
                result_p = temp_poke[i];
                result_a = temp_acc[i];
                result_a=result_a.toFixed(2);
                result_msg = `${result_p}(${result_a}%) `
                $('.desc').append(result_msg);
            }
        }
    })
}
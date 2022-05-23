let page = 1;
let global_total_feed = 0;

$(document).ready(function () {
    getProfile();
    getHistory();
})

function nextPage() {
    if (global_total_feed < 9 || (global_total_feed - (page * 8) <= 0)) {
        alert("마지막 페이지입니다.")
        return false;
    }
    page += 1;
    getHistory();
}

function prevPage() {
    if (page === 1) {
        alert("첫 페이지입니다.")
        return false;
    }
    page -= 1;
    getHistory();
}

function getProfile() {
    $('#profile_data').empty();
    $.ajax({
        type: "GET",
        url: "/api/get_user",
        data: {page: page},
        success: function (response) {
            console.log(response);
            let user = response['user'][0];
            let profile_img = "static/images/history.png";
            let name = user['nick_name'];
            // let user_id = user['user_id'];
            let temp_html = `
                <div class="profile_img"><img class="profile_pic" src="${profile_img}" alt="프로필"></div>
                <div class="profile_word">
                    <div class="profile_post_box">
                        <div class="profile_nickname">${name} 의 포켓몬 도감</div>
                    </div>
                </div> 
                <div class="profile_word">
                    <div class="profile_post_box">
                        <div class="profile_count">완성도: <span id="total_feed"></span></div>
                    </div>
                </div>
            `
            $('#profile_data').append(temp_html);
        }
    })
}

function getHistory() {
    $('#feed_data').empty();

    $.ajax({
        type: "GET",
        url: "/api/get_feed",
        data: {user_id: current_user_id, page: page},
        success: function (response) {
            console.log(response)
            let feeds = response['feed_list'];
            let user = response['user'];
            let total_feed = parseInt(response['total_feed']);
            $('#total_feed').html((total_feed/79*100).toFixed(2)+"% ("+total_feed+" of 79)");
            global_total_feed = parseInt(response['total_feed']);
            for (let k = 0; k < feeds.length; k++) {
                // if (current_user_id === feeds[k]['user_id']) {
                //     let feed_img_src = feeds[k]['feed_img_src'];
                    let feed_img_src = feeds[k]['_id'];
                    let temp_html = `
                        <div class="feed"><img src="${feed_img_src}" width="300" height="300"></div>
                        `
                    $('#feed_data').append(temp_html);

            }
            setBadge();
        }
    })
}

function setBadge() {
    $('#badge_data').empty();
    let temp_html = ``;
    let total_feed = parseInt($('#total_feed').text());
    total_feed = 99
    for(let i = 1; i <= 8 ; i++){
        if(total_feed >= i*8) {
            console.log("!")
            temp_html += `<img src="../static/images/badges/badge0`+i+`.png">`;
        }
    }
    $('#badge_data').append(temp_html);
}
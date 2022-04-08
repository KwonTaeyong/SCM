// 상단 이동 버튼
$(document).ready(function () {
    $('.go-top').toggle()

    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.go-top').fadeIn(200);
        } else {
            $('.go-top').fadeOut(300);
        }
    });
    $('.go-top').click(function () {
        event.preventDefault();

        $('html , body').animate({scrollTop: 0}, 10);
    });
});


// 폰트 사이즈 조절 버튼
function changeFont() {
    document.getElementById('demo').style.fontSize = '50px';
}

function downFont() {
    document.getElementById('demo').style.fontSize = '15px';
}


// 복사 버튼
function copyToClipboard(element) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $temp.remove();
}


// 일정 날짜 버튼
function date_cha(val) {
    var today = new Date()
    today.setDate(today.getDate() - val)
    $('#date1').val(formatDate(today))

}

// 날짜 date 형식 포맷
function formatDate(date) {

    var d = new Date(date),

        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;

    return [year, month, day].join('-');

}



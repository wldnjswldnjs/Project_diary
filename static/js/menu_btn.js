function new_post() {
    document.location.href = '/diary_main/create/'
}
function to_list() {
    document.location.href = '/diary_main/list/'
}

function delete_post() {
    //내가 어떤글을 삭제할지 알아야 함!
    // alert($('#post_id').text())
    let result = confirm("정말 삭제할까요?")
    // confirm 확인을 받기위한 대화창을 띄워줌 (True, False)결과가 떨어짐
    if(result) {
        let queryString = "?post_id=" + $('#post_id').text()
        // "?post_id =6"
        document.location.href = '/diary_main/delete/' + queryString
    }
}

function  like_post() {
    let queryString = "?post_id=" + $('#post_id').text()
    document.location.href = '/diary_main/like/' + queryString
}

// 댓글등록하는 AJAX
function create_comment() {
    $.ajax({
        async: true,
        url: "/diary_main/createComment/",
        type: 'GET',
        data: {
            board_id: $('#post_id').text(),
            comment_author: $('#c_name').val(),
            comment_content: $('#c_content').val()
        },
        dataType: 'json',   // 서버프로그램이 결과로 돌려주는 값은 JSON
        timeout: 3000,
        success: function (result) {
            let tr = $("<tr></tr>").attr('id', 'comment_' + result['c_id'])
            let author_td = $('<td></td>').text(result['c_author'])
            let content_td = $('<td></td>').text(result['c_content'])
            let btn_td = $('<td></td>')
            let btn = $('<button></button>').text('삭제').addClass('btn btn-danger')
            btn.on('click', function () {
                $.ajax({
                    async: true,
                    url: '/diary_main/commentDelete/',
                    type: 'GET',
                    data: {
                        comment_id: result['c_id']
                    },
                    dataType: 'json',
                    timeout: 3000,
                    success: function () {
                        alert('댓글 삭제 성공')
                        $('#comment_' + result['c_id']).remove()
                    },
                    error: function () {
                        alert('댓글 삭제 실패')
                    }
                })
            })

            btn_td.append(btn)
            tr.append(author_td)
            tr.append(content_td)
            tr.append(btn_td)
            $('tbody').prepend(tr)
        },
        error: function () {
            alert('먼가 이상해요')
        }

    })
}
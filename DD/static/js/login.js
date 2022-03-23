function Login(){
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let login_data = JSON.stringify({'email': email, 'password': password});
    $.ajax({
        url : "/D/check_login_data/",
        type: "POST",
        data:{
            'login_data': login_data,
            },
        dataType: 'json',
        // handle a successful response
        success : function(jsondata) {
            console.log(jsondata);
        },
        error : function(jsondata) {
            console.log('Error here in json:' + jsondata);
        }
    });
}
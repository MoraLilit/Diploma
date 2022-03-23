function ShowContentSubject(){
    const selectElement = document.getElementById('standard-select');
    let output = selectElement.options[selectElement.selectedIndex].text;
    document.querySelector('#title').textContent = output;
    let out2 = selectElement.options[selectElement.selectedIndex].value;
    document.querySelector('#description').textContent = out2;
    let data = JSON.stringify({'value': output});
    // jQuery
    $.ajax({
      url : "/D/get_specific_subject/",
        type: "GET",
        data:{
            'data': data,
            },
        dataType: 'json',
        // handle a successful response
        success : function(jsondata) {
            console.log(jsondata);
        },
        error : function(jsondata) {
            console.log('Error here in json:' + jsondata);
        }
    })
    //window.location.reload(true);
}

function onLoad(title, description, theories){
    document.querySelector('#title').textContent = title;
    document.querySelector('#description').textContent = description;
}

function editSubject(){
    document.getElementById("subject-title").value = document.querySelector('#title').textContent;
    document.getElementById("subject-description").type = 'text';
    document.getElementById("subject-description").value = document.querySelector('#description').textContent;
    document.querySelector('#description').textContent = '';
}


function uploadProfilePhoto(){
    let image = $("#choose-photo").get(0);
    let file = image.files;
    let image_data = JSON.stringify({'file': file, 'image': image});
    let formData = new FormData();
    formData.append('title' , file);
    alert(image);
    // jQuery
    $.ajax({
      url : "/D/profile_image/",
        type: "POST",
        data:{
            'image_data': formData,
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
    document.getElementById('profile-photo').nodeValue = file;
    //const file = document.getElementById('choose-photo').files[0];
    //alert(file);
    //document.getElementById('profile-photo').src = file;
}

function addNewSubject(){
    var newSubject = prompt("Enter title and description with / between : ", "Title/Description");
    document.write("You have entered : " + retVal);
    alert('Here we go, someday here will be something');
}

function addNewGroup(){
    alert('Here we go, someday here will be something');
}
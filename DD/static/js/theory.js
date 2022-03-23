function ShowContentSubject(){
    const selectElement = document.getElementById('standard-select');
    let output = selectElement.options[selectElement.selectedIndex].text;
    document.querySelector('#new-subject').value = output;
}

function editTheory(){
}
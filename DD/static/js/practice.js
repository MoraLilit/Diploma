function ShowContentPractice(){
    const selectElement = document.getElementById('standard-select');
    let output = selectElement.options[selectElement.selectedIndex].text;
    document.querySelector('#title').textContent = output;
    let out2 = selectElement.options[selectElement.selectedIndex].value;
    document.querySelector('#description').textContent = out2;
    document.getElementById('container-form').style.display = 'block';
}
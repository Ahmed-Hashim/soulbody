console.log("im working")
tinymce.init({
    selector: '#id_en_description'
});
tinymce.init({
    selector: '#id_ar_description'
});
function expandInput() {
    var inputElement = document.getElementById("id_tags");
    inputElement.classList.add("expanded");
}
document.addEventListener('DOMContentLoaded', expandInput);


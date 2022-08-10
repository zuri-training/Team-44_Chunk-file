// const dropArea = document.querySelector('.drag-area'),
//   dragText = dropArea.querySelector('h3'),
//   button = dropArea.querySelector('button'),
//   input = dropArea.querySelector('input');
// let file; //this is a global variable and we'll use it inside multiple functions
// button.onclick = () => {
//   input.click(); //if user click on the button then the input also clicked
// };
// input.addEventListener('change', function () {
//   //getting user select file and [0] this means if user select multiple files then we'll select only the first one
//   file = this.files[0];
//   dropArea.classList.add('hover');
//   showFile(); //calling function
// });
// //If user Drag File Over DropArea
// dropArea.addEventListener('dragover', (event) => {
//   event.preventDefault(); //preventing from default behaviour
//   dropArea.classList.add('hover');
//   dragText.textContent = 'Release to Upload File';
// });
// //If user leave dragged File from DropArea
// dropArea.addEventListener('dragleave', () => {
//   dropArea.classList.remove('hover');
//   dragText.textContent = 'Drag & Drop to Upload File';
// });
// //If user drop File on DropArea
// dropArea.addEventListener('drop', (event) => {
//   event.preventDefault(); //preventing from default behaviour
//   //getting user select file and [0] this means if user select multiple files then we'll select only the first one
//   file = event.dataTransfer.files[0];
//   console.log(file);
//   showFile(); //calling function
// });
// function showFile() {
//   let fileType = file.type; //getting selected file type
//   let validExtensions = [
//     'application/json',
//     'text/csv',
//     'text/x-csv',
//     'application/x-csv',
//     'application/csv',
//     'text/x-comma-separated-values',
//     'text/comma-separated-values',
//     'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
//     'application/vnd.ms-excel',
//   ]; //adding some valid csv and json extensions in array
//   if (validExtensions.includes(fileType)) {
//     //if user selected file is an csv/json file
//     let fileReader = new FileReader(); //creating new FileReader object
//     fileReader.onload = () => {
//       let fileName = `${file.name}`;
//       dropArea.innerHTML = fileName;
//     };
//     fileReader.readAsText(file);
//     console.log(fileReader.readAsText(file));
//   } else {
//     alert('This is not a CSV/JSON File!');
//     dropArea.classList.add('error');
//     dragText.textContent = 'Drag & Drop to Upload File';
//   }
// }
// ************************ Drag and drop ***************** //
$(document).on("change", ".file-input", function () {
  var filesCount = $(this)[0].files.length;

  var textbox = $(this).prev();

  if (filesCount === 1) {
    var fileName = $(this).val().split("\\").pop();
    textbox.text(fileName);
  } else {
    textbox.text(filesCount + " files selected");
  }
});

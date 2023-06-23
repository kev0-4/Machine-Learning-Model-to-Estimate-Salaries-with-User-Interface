function getGender() { 
  var uiGender = document.getElementsByName("uiGender");
  for (var i = 0; i < uiGender.length; i++) {
    if (uiGender[i].checked) {
      return uiGender[i].value;
    }
  }
  return -1;
}
//WORKING - CHECKED
function getEducation() {
  var uiEducation = document.getElementsByName("uiEducation");
  for (var i = 0; i < uiEducation.length; i++) {
    if (uiEducation[i].checked) {
      return uiEducation[i].value;
    }
  }
  return -1;
}
//WORKING - CHECKED
function onClickedEstimateSalary() {
  console.log("Estimate salary button clicked");
  var age = document.getElementById("uiAge").value;
  var yoe = document.getElementById("uiYearsOfExperience").value;
  var gender = getGender();
  var education = getEducation();
  var position = document.getElementById("uiPosition").value;

  // Log the values
//   console.log("Age:", age);
//   console.log("Years of Experience:", yoe);
//   console.log("Gender:", gender);
//   console.log("Education:", education);
//   console.log("Position:", position);
  var url = "http://127.0.0.1:5000/predict_salary";
    //
  $.post(url, {
    Age : age,Gender : gender,Education : education,position : position,
    YOE : yoe
  },
  function(data, status){
    console.log(data.estimates_salary);
    var estSalary = document.getElementById("uiEstimateSalary");
    estSalary.innerHTML = "<h2>" + data.estimates_salary.toString() + "K</h2";
    console.log(status);
  }); 

}
//WORKING
function onPageLoad() {
  console.log("Document loaded");
  var url = "http://127.0.0.1:5000/get_position";
  fetch(url)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log("Got response for get_position request", data);
      if (data) {
        var position = data.position;
        var uiPosition = document.getElementById("uiPosition");
        for (var i = 0; i < position.length; i++) {
          var opt = new Option(position[i]);
          uiPosition.appendChild(opt);
        }
      } else {
        console.log("No data received");
      }
    })
    .catch(function (error) {
      console.log("Error occurred", error);
    });
}
//WORING - CHECKED
window.onload = onPageLoad;

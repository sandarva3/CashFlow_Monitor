var purchased = document.getElementById("purchased");
var notpurchased = document.getElementById("notpurchased");
var text = document.getElementById("text");
var number = document.getElementById("number");

purchased.addEventListener("change", function () {
  text.setAttribute("placeholder", "Enter Bought Item");
  number.setAttribute("placeholder", "Enter Your Expenditure");
});
notpurchased.addEventListener("change", function () {
  text.setAttribute("placeholder", "Enter Unbought Item");
  number.setAttribute("placeholder", "Enter Your Savings");
});

function isDateValid() {
  var dateField = document.getElementById("date");
  var todayField = document.getElementById("today");

  if (dateField.value == "" && !todayField.checked) {
    alert("You didn't provide date! Therefore today's date will be selected.");
    todayField.checked = true;
  } else if (dateField.value != "" && todayField.checked) {
    alert(
      "You provided multiple dates! Therfore today's date will be selected."
    );
    dateField.value = "";
  }
}

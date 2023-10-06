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

  if (todayField.checked) {
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, "0");
    var mm = String(today.getMonth() + 1).padStart(2, "0"); //January is 0!
    var yyyy = today.getFullYear();
    dateField.value = yyyy + "-" + mm + "-" + dd;
  }
}

document.getElementById("today").addEventListener("change", isDateValid());
window.onload = isDateValid();

document.querySelector("form").addEventListener("submit", function (e) {
  e.preventDefault(); // Prevent the default form submission

  var itemsArray = JSON.parse(localStorage.getItem("guestItems")) || [];

  var newItem = {
    date: document.getElementById("date").value,
    purchased: document.getElementById("purchased").checked
      ? document.getElementById("text").value
      : "-",
    wasted: document.getElementById("purchased").checked
      ? document.getElementById("number").value
      : "-",
    not: document.getElementById("notpurchased").checked
      ? document.getElementById("text").value
      : "-",
    saved: document.getElementById("notpurchased").checked
      ? document.getElementById("number").value
      : "-",
  };

  itemsArray.push(newItem); // Add the new item to the array

  localStorage.setItem("guestItems", JSON.stringify(itemsArray)); // Update local storage

  window.location.href = "/"; // Redirect to the guest home page
});

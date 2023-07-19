
// Function to handle adding a class
document.getElementById("addClassForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var classInput = document.getElementById("classInput").value;

    // Make an AJAX request to the Django view
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/add-class/", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            alert(xhr.responseText);
            // Clear the class input field after successful submission
            document.getElementById("classInput").value = "";
        }
    };
    xhr.send("class_name=" + classInput);
});

// Function to handle adding a student
document.getElementById("addStudentForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var studentInput = document.getElementById("studentInput").value;
    var classSelect = document.getElementById("classSelect").value;

    // Make an AJAX request to the Django view
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/add-student/", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            alert(xhr.responseText);
            // Clear the student input field after successful submission
            document.getElementById("studentInput").value = "";
        }
    };
    xhr.send("student_name=" + studentInput + "&class_name=" + classSelect);
});

// Function to populate the class select dropdown
window.onload = function() {
    var classSelect = document.getElementById("classSelect");

    // Make an AJAX request to fetch the available classes
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/get-classes/", true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var classes = JSON.parse(xhr.responseText);

            // Populate the class select dropdown
            classes.forEach(function(_class) {
                var option = document.createElement("option");
                option.value = _class.id;
                option.text = _class.name;
                classSelect.appendChild(option);
            });
        }
    };
    xhr.send();
};

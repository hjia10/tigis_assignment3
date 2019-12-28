//  Web Database Visualiser - JavaScript Code

// DOM Elements

function changeColour(identifier, colour) {
    bit = document.getElementById(identifier)
    bit.style.color = colour
}

$('#field1').on("click", function() {
    $('#field1').css.stroke = blue;
    $('#field1').css.fill = blue;

});


var test = 2
postData(test)

var answer = document.getElementById('button1');
answer.addEventListener("click", () => {
    alert("Hello, World!");
});


function postData(input) {
    window.alert("postdata");
    var jqXHR = $.ajax({
        type: "POST",
        url: "~/playground.py",
        async: false,
        data: { param: input },
    });
    window.alert("endme")
    window.alert(jqXHR.responseText);
    return jqXHR.responseText;
}

function callbackFunc(response) {
    // do something with the response
    console.log(response);
}
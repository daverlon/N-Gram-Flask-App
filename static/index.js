
document.getElementById("copy-button").onclick = function() {
    var txt = document.getElementById("output-textbox").value;
    navigator.clipboard.writeText(txt)
}

document.getElementById("clear-button").onclick = function() {
    document.getElementById("output-textbox").value = "";
}

function getElonTweet() {
    fetch('/gen_elon_tweet')
        .then(response => response.json())
        .then(data => {
            document.getElementById('output-textbox').value = data.text;
        })
        .catch(error => console.error('Error:', error));
}

function getMcDonaldsReview() {
    fetch('/get_mcdonalds_review')
        .then(response => response.json())
        .then(data => {
            document.getElementById('output-textbox').value = data.text;
        })
        .catch(error => console.error('Error:', error));
}

function getAirlineReview() {
    fetch('/get_airline_review')
        .then(response => response.json())
        .then(data => {
            document.getElementById('output-textbox').value = data.text;
        })
        .catch(error => console.error('Error:', error));
}
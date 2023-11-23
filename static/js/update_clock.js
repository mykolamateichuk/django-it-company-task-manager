function updateClock() {
    var currentTime = new Date();
    var hours = currentTime.getHours();
    var minutes = currentTime.getMinutes();

    // Add leading zero if needed
    minutes = (minutes < 10 ? "0" : "") + minutes;

    var timeString = hours + ':' + minutes;

    console.log("update")
    document.getElementById('clock').innerHTML = timeString;
}

// Update the clock every minute
setInterval(updateClock, 5000);

// The days of the week are: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
function getDayName(dateString) {
    let dayName = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday"][new Date(dateString).getUTCDay()];
    // Write your code here
    
    
    return dayName;
}

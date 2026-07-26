// AWS Serverless Visitor Counter
// Connects Frontend with API Gateway

// Replace this URL with your API Gateway Invoke URL
const API_URL = "YOUR_API_GATEWAY_URL";


async function getVisitorCount() {

    try {

        const response = await fetch(API_URL);

        const data = await response.json();

        document.getElementById("visitor-count").innerText =
            data.visitorCount;

    } 
    catch (error) {

        console.error("Error fetching visitor count:", error);

        document.getElementById("visitor-count").innerText =
            "Error";

    }

}


// Call function when website loads
getVisitorCount();

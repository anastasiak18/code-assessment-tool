document.getElementById("generateFeedback").addEventListener("click", () => {
    const code = document.getElementById("codeInput").value;

    fetch("http://127.0.0.1:5000/api/analyse-code", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ code }),
    })
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("feedback").innerText = data.feedback;
        })
        .catch((error) => {
            console.error("Error:", error);
        });
});
